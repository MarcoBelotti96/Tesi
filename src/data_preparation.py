#! /usr/bin/env python3
import pandas as pd
import numpy as np
import info_stazioni as info
import datetime as dt

dir_meteo = "../data/sensori_meteo_csv"
dir_aria = "../data/sensori_aria_csv"
areac_filepath = "../data/areaC/areac_alldata.csv"

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
def prepare_data(id_aria, id_temp, id_prec, id_dirvento, id_velvento, id_umid, id_rad, **kwargs):
	agg_unit = kwargs.get("agg_unit", "d")
	use_areac = kwargs.get("use_areac", False)

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
	if(id_rad != -1):
		df_rad = get_values_renamed(dir_meteo, id_rad, "radiazione", agg_unit)
		dfs.append(df_rad)
	if(use_areac):
		dfs.append(pd.read_csv(areac_filepath, parse_dates=["data"], index_col="data"))
	
	#concateno le rilevazioni dei vari sensori e aggiungo le variabili temporali	
	tot = dfs[0]
	for dfx in dfs[1:]:
		tot = tot.join(dfx)
	tot["day_of_year"] = tot.index.dayofyear
	tot["day_of_week"] = tot.index.dayofweek	
	tot["epoch"] = tot.index.astype("int64")

	#filtro le date per cui non ho rilevazioni per l'inquinante
	tot = tot.dropna(subset=["inquinante"])

	#riempio le altre misure mancanti con le medie
	tot = tot.fillna(tot.mean())

	#aggiungo il conteggio dei giorni dall'ultima pioggia registrata
	count = 0
	for index, row in tot.iterrows():
		if(row.precipitazioni > 0):
			count = 0
		tot.loc[index, "giorni_senza_pioggia"] = count
		count += 1

	#filtro i dati a partire dalla data di messa in funzione del sensore più recente
	date_threshold = mindate(id_aria, id_temp, id_prec, id_dirvento, id_velvento, id_umid, id_rad, use_areac)
	tot = tot[tot.index >= date_threshold]

	return tot

def mindate(id_aria, id_temp, id_prec, id_dirvento, id_velvento, id_umid, id_rad, use_areac):
	dates = []
	dates.append(info.get_datastart_sensore_aria(id_aria))
	dates.append(info.get_datastart_sensore_meteo(id_temp))
	dates.append(info.get_datastart_sensore_meteo(id_prec))
	dates.append(info.get_datastart_sensore_meteo(id_dirvento))
	dates.append(info.get_datastart_sensore_meteo(id_velvento))
	dates.append(info.get_datastart_sensore_meteo(id_umid))
	dates.append(info.get_datastart_sensore_meteo(id_rad))
	if(use_areac):
		dates.append(dt.datetime(2012, 1, 1)) #data inizio area C: 2012-01-01
	
	dates.sort(reverse=True)
	return dates[0]
