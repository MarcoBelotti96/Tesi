#! /usr/bin/env python3
import pandas as pd

stazioni_aria = "https://www.dati.lombardia.it/resource/ib47-atvt.json?$limit=1500"
stazioni_meteo  = "https://www.dati.lombardia.it/resource/nf78-nj6b.json?$limit=1500"

# Funzioni di utility generale per cercare gli id dei sensori su cui andare a fare le analisi

def get_stazioni_byname(df, name_pattern):
	df = pd.read_json(stazioni_aria)
	df["mask"] = df["nomestazione"].str.contains(name_pattern)
	df = (df[df["mask"] == True]).drop("mask", axis = 1)
	return df

def get_sensori_byid(df, id_stazione):
	df = df[df.idstazione == id_stazione]
	return df

stazioni = pd.read_json(stazioni_aria)
print(get_sensori_byid(stazioni, 584))
