import urllib.request
import shutil
import os
import zipfile

stazioni_aria = "https://www.dati.lombardia.it/resource/ib47-atvt.json?"
aria_anno_corrente = "https://www.dati.lombardia.it/api/views/nicp-bhqi/rows.csv?accessType=DOWNLOAD"
url_aria = ["https://www.dati.lombardia.it/api/views/j2mz-aium/files/051e8277-077d-4e04-bc2a-56023f349152?filename=sensori_aria_2019.zip",
            "https://www.dati.lombardia.it/api/views/4t9j-fd8z/files/4b3390e3-681c-43ee-bd88-ccb779cc6d6d?filename=sensori_aria_2018.zip",
            "https://www.dati.lombardia.it/api/views/fdv6-2rbs/files/f4c00e96-ef57-4762-8b44-cf4a1bf85c70?filename=sensori_aria_2017.zip",
            "https://www.dati.lombardia.it/api/views/7v3n-37f3/files/011167bb-4cba-46d6-83ad-d225ee1fe39a?filename=sensori_aria_2016.zip",
            "https://www.dati.lombardia.it/api/views/bpin-c7k8/files/6d72e186-804a-4e76-bf7a-16117eeb8e69?filename=sensori_aria_2015.zip",
            "https://www.dati.lombardia.it/api/views/69yc-isbh/files/487864fb-1f8c-4a28-9949-c4d64adacd29?filename=sensori_aria_2014.zip",
            "https://www.dati.lombardia.it/api/views/hsdm-3yhd/files/ce297c9e-59bd-48f3-b4fb-f1baf7e93840?filename=sensori_aria_2013.zip",
            "https://www.dati.lombardia.it/api/views/wr4y-c9ti/files/72c5105a-e1f3-46fe-873b-f3dd449fd6ca?filename=sensori_aria_2012.zip",
            "https://www.dati.lombardia.it/api/views/5mut-i45n/files/6cdf8360-beea-42e7-b9d4-774e06147d6c?filename=sensori_aria_2011.zip",
            "https://www.dati.lombardia.it/api/views/wp2f-5nw6/files/e780233e-18fc-4e46-8417-7bb2af435f73?filename=sensori_aria_2008-2010.zip",
            "https://www.dati.lombardia.it/api/views/h3i4-wm93/files/5774cc67-801c-4ce6-a5de-d43208d83f2d?filename=sensori_aria_2005-2007.zip",
            "https://www.dati.lombardia.it/api/views/5jdj-7x8y/files/533e1a0d-393f-4b4c-80ba-30e49908ca8b?filename=sensori_aria_2001-2004.zip",
            "https://www.dati.lombardia.it/api/views/wabv-jucw/files/2dcfa5a5-27ad-491a-904b-5c3a7453d9f7?filename=sensori_aria_1996-2000.zip",
            "https://www.dati.lombardia.it/api/views/puwt-3xxh/files/a90d15c6-4daf-4a36-bf34-1954f125d644?filename=sonde_aria_1968-1995.zip" ]

stazioni_meteo  = "https://www.dati.lombardia.it/resource/nf78-nj6b.json?"
meteo_mese_corrente = "https://www.dati.lombardia.it/api/views/647i-nhxk/rows.csv?accessType=DOWNLOAD"
url_meteo = ["https://www.dati.lombardia.it/api/views/erjn-istm/files/60005865-2103-44c0-a67f-5dba34a6175a?filename=sensori_meteo_2020.zip",
             "https://www.dati.lombardia.it/api/views/wrhf-6ztd/files/2ecea348-3c84-4380-82f9-ec8dc9c0222c?filename=sensori_meteo_2019.zip",
             "https://www.dati.lombardia.it/api/views/sfbe-yqe8/files/3328ba4d-b54a-4d2d-9b0f-7ac0112c89e0?filename=sensori_meteo_2018.zip",
             "https://www.dati.lombardia.it/api/views/vx6g-atiu/files/2fa6818f-15af-47b7-bac4-049f784b5108?filename=sensori_meteo_2017.zip",
             "https://www.dati.lombardia.it/api/views/kgxu-frcw/files/aebb7a81-6ae2-436c-8cf0-79183c4d5bae?filename=sensori_meteo_2016.zip",
             "https://www.dati.lombardia.it/api/views/knr4-9ujq/files/212b2d48-a6cf-49d4-a9eb-b6d24e475f84?filename=sensori_meteo_2015.zip",
             "https://www.dati.lombardia.it/api/views/fn7i-6whe/files/00fe3db6-8836-44f9-ae24-c0e972b96a47?filename=sensori_meteo_2014.zip",
             "https://www.dati.lombardia.it/api/views/76wm-spny/files/8ac843e8-3364-4499-b531-46f6c116b014?filename=sensori_meteo_2013.zip",
             "https://www.dati.lombardia.it/api/views/srpn-ykcs/files/aeaf95c2-0a2d-4648-93ec-e7baccebe459?filename=sensori_meteo_2011-2012.zip",
             "https://www.dati.lombardia.it/api/views/9nu5-ed8s/files/96c13001-016f-43a2-8d3d-439fe038d226?filename=sensori_meteo_2009-2010.zip",
             "https://www.dati.lombardia.it/api/views/6udq-c5ub/files/db7a86ff-0975-4646-aa3e-453a2af9b370?filename=sensori_meteo_2006-2008.zip",
			 "https://www.dati.lombardia.it/api/views/stys-ktts/files/b599de2c-51c8-423e-8523-fbf1ca3d54ef?filename=sensori_meteo_2001-2005.zip",
             "https://www.dati.lombardia.it/api/views/tj2h-b7vd/files/a96ddd81-2004-41aa-999a-ccaaae86e10d?filename=sensori_meteo_1989-2000.zip"]

def download_file_meteo():
    base_dir = "../data/meteo_raw"
    if not os.path.exists(base_dir): #se non esiste la dir di output la creo
        os.mkdir(base_dir)
    print("Downloading metereological raw data..")
    for url in url_meteo:
        filename = url.split("=")[1] #estraggo il nome del file
        filepath = base_dir + "/" + filename
        print("Downloading", filename)
        with urllib.request.urlopen(url) as response, open(filepath, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print("Extracting zip archive")
        with zipfile.ZipFile(filepath, 'r') as zip_ref: #estraggo l'archivio
            zip_ref.extractall(base_dir + "/")
        os.remove(filepath)
        print(filename, "done!")
    #il file del mese corrente va gestito in modo separato (viene automaticamente scaricato il csv)
    filename = "mese_corrente.csv"
    print("Downloading current month CSV file")
    with urllib.request.urlopen(aria_anno_corrente) as response, open(base_dir + "/" + filename, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


def download_file_aria():
    base_dir = "../data/aria_raw"
    if not os.path.exists(base_dir): #se non esiste la dir di output la creo
        os.mkdir(base_dir)
    print("Downloading air raw data..")
    for url in url_aria:
        filename = url.split("=")[1] #estraggo il nome del file
        filepath = base_dir + "/" + filename
        print("Downloading", filename)
        with urllib.request.urlopen(url) as response, open(filepath, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        #print("Extracting zip archive")
        with zipfile.ZipFile(filepath, 'r') as zip_ref: #estraggo l'archivio
            zip_ref.extractall(base_dir + "/")
        os.remove(filepath)
        print(filename, "done!")
    #il file dell'anno corrente va gestito in modo separato (viene automaticamente scaricato il csv)
    filename = "anno_corrente.csv"
    print("Downloading current year CSV file")
    with urllib.request.urlopen(aria_anno_corrente) as response, open(base_dir + "/" + filename, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


def download_files():
	if not os.path.exists("../data"):
		os.mkdir("../data")
	download_file_aria()
	download_file_meteo()

#download_files()
