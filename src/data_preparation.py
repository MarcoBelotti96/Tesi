#! /us/bin/env python3
import pandas as pd

dir_meteo = "../data/sensori_meteo_csv"
dir_aria = "../data/sensori_aria_csv"

#estrare le serie delle rilevazioni per un dato sensore e rinomina la colonna valore col nome della misura
def get_values_renamed(path, idsensore, nome_misura):
	df = pd.read_csv(path + "/" + idsensore, parse_dates=["Data"], index_col="Data")
	df = df.loc[df.Valore != -9999, ["Valore"]]
	df = df.groupby(pd.Grouper(freq="d")).mean() 
	df = df.rename(columns = {"Valore", nome_misura})
	return df

#preparazione del dataframe per applicare random forest
def prepare_data(id_aria, id_temp, id_prec, id_dirvento, id_velvento, id_pressatmos, id_umid):
	#recupero le rilevazioni per le varie misure da usare nella normalizzazione
	df_aria = get_values_renamed(dir_aria, id_aria, "inquinante")
	df_temp = get_values_renamed(dir_meteo, id_temp, "temperatura")
	df_prec = get_values_renamed(dir_meteo, id_prec, "precipitazioni")
	df_direvento = get_values_renamed(dir_meteo, id_direvento, "direzione_vento")
	df_velvento = get_values_renamed(dir_meteo, id_velvento, "velocita_vento")
	df_pressatmos = get_values_renamed(dir_meteo, id_pressatmos, "press_atmos")
	df_umid = get_values_renamed(dir_meteo, id_umid, "umidita")
	dfs = [df_aria, df_temp, df_prec, df_dirvento, df_velvento, df_pressatmos, df_umid]
	
	#concateno le rilevazioni dei vari sensori e aggiungo le variabili temporali	
	tot = dfs[0]
	for dfx in dfs[1:]:
		tot = tot.join(dfx)
	tot["day_of_year"] = tot.index.dayofyear
	tot["day_of_week"] = tot.index.dayofweek	

	#filtro i giorni per cui non ho rilevazioni per l'inquinante o per la vel. del vento
	tot = tot[tot["inquinante"].notnull()]
	tot = tot[tot["velocita_vento"].notnull()]

	#riempio le altre misure mancanti con le medie
	tot = tot.fillna(tot.mean())

	return tot
