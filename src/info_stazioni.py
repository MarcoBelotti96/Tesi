#! /usr/bin/env python3
import pandas as pd

stazioni_aria = pd.read_json("https://www.dati.lombardia.it/resource/ib47-atvt.json?$limit=1500")
stazioni_meteo  = pd.read_json("https://www.dati.lombardia.it/resource/nf78-nj6b.json?$limit=1500")

# Funzioni di utility generale per cercare gli id dei sensori su cui andare a fare le analisi

def get_stazioni_byname(df, name_pattern):
	df["mask"] = df["nomestazione"].str.contains(name_pattern)
	df = (df[df["mask"] == True]).drop("mask", axis = 1)
	return df

def get_sensori_byid(df, id_stazione):
	df = df[df.idstazione == id_stazione]
	return df

def get_stazioni_aria_byname(name_pattern):
	return get_stazioni_byname(stazioni_aria, name_pattern)

def get_stazioni_meteo_byname(name_pattern):
	return get_stazioni_byname(stazioni_meteo, name_pattern)

def get_sensori_aria_byid(id_stazione):
	return get_sensori_byid(stazioni_aria, id_stazione)

def get_sensori_meteo_byid(id_stazione):
	return get_sensori_byid(stazioni_meteo, id_stazione)
