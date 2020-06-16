import pandas as pd
import time
import glob
import os

chunksize = 10 ** 6


def process_csv_meteo():
    if not os.path.exists("../data/sensori_meteo_csv"): #se non esiste la dir di output la creo
        os.mkdir("../data/sensori_meteo_csv")

    files = glob.glob("../data/meteo_raw/*.csv") #tutti i file grezzi
    print("Processing of CSV meteo data starting..")
    start = time.time()
    for f in files:
        print("Processing file", f)
        for chunk in pd.read_csv(f, chunksize=chunksize): #leggo 10^6 righe del file in un dataframe
            print("Chunk read. Extracting indexes..")
            id_sensori = chunk['IdSensore'].unique() #estraggo gli id presenti nel file
            for sensore in id_sensori:
                sensore_df = chunk[chunk.IdSensore == sensore] #seleziono la parte di dataframe che mi serve
                file_sensore = f"../data/sensori_meteo_csv/{sensore}.csv"
                file_exist = os.path.isfile(file_sensore)
                sensore_df.to_csv(file_sensore, mode='a', header=not file_exist, index=False) #devo scrivere l'header solo quando creo il file
                #print("File", sensore, " written..")

    print("Process done in %s seconds" % (time.time() - start))

#possibile ottimizzazione?
def process_csv_aria():
    if not os.path.exists("../data/sensori_aria_csv"):
        os.mkdir("../data/sensori_aria_csv")

    files = glob.glob("../data/aria_raw/*.csv")
    print("Processing of CSV air data starting..")
    start = time.time()
    for f in files:
        print("Processing file", f)
        for chunk in pd.read_csv(f, chunksize=chunksize):
            print("Chunk read. Extracting indexes..")
            id_sensori = chunk['IdSensore'].unique()
            for sensore in id_sensori:
                sensore_df = chunk[chunk.IdSensore == sensore]
                file_sensore = f"../data/sensori_aria_csv/{sensore}.csv" 
                file_exist = os.path.isfile(file_sensore)
                sensore_df.to_csv(file_sensore, mode='a', header=not file_exist, index=False)
                #print("File", sensore, " written..")

    print("Process done in %s seconds" % (time.time() - start))


def process_csv():
    process_csv_aria()
    process_csv_meteo()

#process_csv()
