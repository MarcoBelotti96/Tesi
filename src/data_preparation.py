#! /usr/bin/env python3
import pandas as pd

dir_meteo = "../data/sensori_meteo_csv"
dir_aria = "../data/sensori_aria_csv"

#estrae le serie delle rilevazioni per un dato sensore e rinomina la colonna valore col nome della misura
def get_values_renamed(path, idsensore, nome_misura, agg_unit):
	df = pd.read_csv(path + "/" + str(idsensore) + ".csv", parse_dates=["Data"], dayfirst=True, index_col="Data")
	df = df.loc[df.Valore != -9999, ["Valore"]]
	df = df.groupby(pd.Grouper(freq=agg_unit)).mean() 
	df = df.rename(columns = {"Valore": nome_misura})
	return df

#preparazione del dataframe per applicare random forest
#-1 per i sensori che non si vogliono usare
# agg_unit: l'unità temporale su cui aggregare i dati (h, d, ...)
def prepare_data(id_aria, id_temp, id_prec, id_dirvento, id_velvento, id_umid, agg_unit):
	dfs = []
	df_aria = get_values_renamed(dir_aria, id_aria, "inquinante", agg_unit)
	dfs.append(df_aria)
	if(id_temp != -1):
		df_temp = get_values_renamed(dir_meteo, id_temp, "temperatura", agg_unit)
		dfs.append(df_temp)
	if(id_prec != -1):
		df_prec = get_values_renamed(dir_meteo, id_prec, "precipitazioni", agg_unit)
		dfs.append(df_prec)
	if(id_dirvento != -1):
		df_dirvento = get_values_renamed(dir_meteo, id_dirvento, "direzione_vento", agg_unit)
		#filtro dirvento variabile
		df_dirvento = df_dirvento[(df_dirvento["direzione_vento"] != 888) & (df_dirvento["direzione_vento"] != 8888)]
		#filtro dirvento calma
		df_dirvento = df_dirvento[(df_dirvento["direzione_vento"] != 777) & (df_dirvento["direzione_vento"] != 7777)]
		dfs.append(df_dirvento)
	if(id_velvento != -1):
		df_velvento = get_values_renamed(dir_meteo, id_velvento, "velocita_vento", agg_unit)
		dfs.append(df_velvento)
	if(id_umid != -1):
		df_umid = get_values_renamed(dir_meteo, id_umid, "umidita", agg_unit)
		dfs.append(df_umid)
	
	#concateno le rilevazioni dei vari sensori e aggiungo le variabili temporali	
	tot = dfs[0]
	for dfx in dfs[1:]:
		tot = tot.join(dfx)
	tot["day_of_year"] = tot.index.dayofyear
	tot["day_of_week"] = tot.index.dayofweek	

	#filtro le date per cui non ho rilevazioni per l'inquinante
	tot = tot.dropna(subset=["inquinante"])

	#riempio le altre misure mancanti con le medie
	tot = tot.fillna(tot.mean())

	return tot
