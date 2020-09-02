import urllib.request
import shutil
import os
import zipfile
import glob
import pandas as pd
import datetime as dt

accessi_giornalieri = ["https://dati.comune.milano.it/dataset/8937eb87-2356-40ba-bd82-e0fabe38b598/resource/c2f46ef8-9ee8-4883-807d-93adeb1b9931/download/ingressi_areac_2020-07-22.csv",
						#"https://dati.comune.milano.it/dataset/8e52436a-410a-4d0b-9c0d-a74dbe0d8dd6/resource/eaf59664-895f-4cf4-86bc-5c9c88a47989/download/v2_accessigiornalieri_areacundefined_2016.csv",
						"https://dati.comune.milano.it/dataset/134141e6-5e39-4900-ad3f-4d7c5bf411e3/resource/3526a5ba-d1c5-4f32-949a-f0404dde9a91/download/v2_accessigiornalieri_areacundefined_2015.csv",
						"https://dati.comune.milano.it/dataset/0083deed-5af1-46d1-a603-0d10f1500fc6/resource/f3bca815-cb88-4807-9bad-5c851ba3145a/download/v2_accessigiornalieri_areacundefined_2014.csv",
						"https://dati.comune.milano.it/dataset/b597f3b0-1616-4117-97c4-64e1d619edac/resource/62d55f92-afe9-432b-8fb6-178247cf66ff/download/v2_accessigiornalieri_areacundefined_2013.csv",
						"https://dati.comune.milano.it/dataset/55a1dbf1-0442-48df-bffe-4f2615b1c473/resource/497a8344-12db-4c1a-a0a9-fbdb2ee47370/download/v2_accessigiornalieri_areacundefined_2012.csv"]

accessi2017 = ["https://dati.comune.milano.it/dataset/e2c1f81d-aa7f-4b21-87c1-c2fdc73fa9b9/resource/b02117de-33fc-44f3-bf78-51012af61983/download/ds884_ingressi_areac_2017_12.zip",
				"https://dati.comune.milano.it/dataset/35578b80-ad62-4b7d-b88b-7ac151053d59/resource/4f8a059f-b62c-4f58-a57b-0cc426c15fdf/download/ds883_ingressi_areac_2017_11.zip",
				"https://dati.comune.milano.it/dataset/171081ca-62a1-4d25-bf01-2fef9bed31ea/resource/01bc7b9d-0e40-4238-a3dc-262bdb68753d/download/ds882_ingressi_areac_2017_10.zip",
				"https://dati.comune.milano.it/dataset/320f5acc-de7c-4f9e-9e0d-8e1f1905d5c4/resource/c6442360-1ae7-4988-b8b8-db3de0a815cc/download/ds881_ingressi_areac_2017_9.zip",
				"https://dati.comune.milano.it/dataset/ab4fc9b0-12e6-43c4-ac09-6a32e64afacc/resource/f2b54ef5-f78c-4b4e-a6a5-38d55d9f735e/download/ds880_ingressi_areac_2017_8.zip",
				"https://dati.comune.milano.it/dataset/1a5bcb92-09e2-4342-8f8b-f2f8db862996/resource/5e757171-9eba-4c49-9175-da732488d92e/download/ds879_ingressi_areac_2017_7.zip",
				"https://dati.comune.milano.it/dataset/77a7e1fe-dcba-458f-a071-a60ce8ba0d24/resource/ad3bdf8c-b6e6-42b9-b3f3-90d7d42efaa6/download/ds878_ingressi_areac_2017_6.zip",
				"https://dati.comune.milano.it/dataset/41f36e0d-bef5-48d7-b636-6ce8c0507bb0/resource/ee599519-b8fb-4974-8762-725e47b0ab54/download/ds877_ingressi_areac_2017_5.zip",
				"https://dati.comune.milano.it/dataset/63fd0404-c65b-4f11-b4e7-0a9073a0c4ad/resource/6da9cbf5-7a23-4da3-8fbf-0e49a5e385ea/download/ds876_ingressi_areac_2017_4.zip",
				"https://dati.comune.milano.it/dataset/f78c3063-6216-4cfc-9f8f-ed2dce8ae9c9/resource/ed18dea2-f146-4496-a964-39100367b217/download/ds875_ingressi_areac_2017_3.zip",
				"https://dati.comune.milano.it/dataset/2d73fa8e-d8d7-4db0-b5c8-299c7836bf22/resource/5de1105f-6acb-4bf9-a557-0bede7481867/download/ds874_ingressi_areac_2017_2.zip",
				"https://dati.comune.milano.it/dataset/17350891-e4aa-43dc-b4df-8824fbbbfbed/resource/d2167d59-52d2-44d8-a995-e742f0ef5efa/download/ds873_ingressi_areac_2017_1.zip"]

accessi2018 = ["https://dati.comune.milano.it/dataset/e0e472f7-7ea7-417d-a77e-565e9d5e093e/resource/afaa97ef-e52b-4ce6-bccb-cf888c2bf5bc/download/ds896_ingressi_areac_2018_12.zip",
				"https://dati.comune.milano.it/dataset/73a5868c-afe2-45b5-a003-4d6cadf241e2/resource/526dc39a-3834-4cd7-8fca-5ce750785ecc/download/ds895_ingressi_areac_2018_11.zip",
				"https://dati.comune.milano.it/dataset/7f2ebe59-31ab-4719-9d2b-2db64048d9f1/resource/ed12c3c6-6d30-44f7-a1d0-7ec0d2713782/download/ds894_ingressi_areac_2018_10.zip",
				"https://dati.comune.milano.it/dataset/c847045d-efde-44b9-b0ea-5341410ff553/resource/d12f4ebe-fea7-4155-a63c-d2147988a90a/download/ds893_ingressi_areac_2018_9.zip",
				"https://dati.comune.milano.it/dataset/c555a129-7c99-478d-87e4-6e0761ca3e3b/resource/1dccf756-3b9b-46f7-a4ab-50842fb28dc7/download/ds892_ingressi_areac_2018_8.zip",
				"https://dati.comune.milano.it/dataset/e7b05d58-9538-418b-8ca7-052084adf301/resource/388e3bd0-1901-40c6-99ac-cd3ba42d05cf/download/ds891_ingressi_areac_2018_7.zip",
				"https://dati.comune.milano.it/dataset/b65eb5aa-41d3-4820-b396-f46dcf4dbf01/resource/bb418d5d-4f8a-4cdb-b35d-f712dfbcae2d/download/ds890_ingressi_areac_2018_6.zip",
				"https://dati.comune.milano.it/dataset/b140223f-5f7f-4949-8277-4efd0196c14a/resource/b171feff-8d1c-41f2-8fef-81cf29850d47/download/ds889_ingressi_areac_2018_5.zip",
				"https://dati.comune.milano.it/dataset/7258f1ad-cf0e-4077-8d5e-36f6aa28555e/resource/4988182a-311a-4160-b879-65b03e8b5830/download/ds888_ingressi_areac_2018_4.zip",
				"https://dati.comune.milano.it/dataset/10713ab6-9e4e-4227-947b-8d46ec35869b/resource/296ce181-c57e-480c-aec7-5663e0543b4a/download/ds887_ingressi_areac_2018_3.zip",
				"https://dati.comune.milano.it/dataset/c743d1a2-343a-474e-ac13-b8855c27904e/resource/423da2bc-a3fb-4297-9700-d8e423605c0c/download/ds886_ingressi_areac_2018_2.zip",
				"https://dati.comune.milano.it/dataset/e5aaf7d2-dd30-4706-a059-8a4e5de209fb/resource/06c5ab4f-e460-4515-b861-0f4047a815af/download/ds885_ingressi_areac_2018_1.zip"]
	
path = "../data/areaC"

def download_files():
	if not os.path.exists(path):
		os.mkdir(path)

	for url in accessi_giornalieri:
		filename = url.split("/")[-1]
		filepath = path + "/" + filename
		print(f"Downloading {filename}...")
		with urllib.request.urlopen(url) as response, open(filepath, "wb") as out_file:
			shutil.copyfileobj(response, out_file)

	for url in accessi2017 + accessi2018:
		filename = url.split("/")[-1] 
		filepath = path + "/" + filename
		print(f"Downloading {filename}...")
		with urllib.request.urlopen(url) as response, open(filepath, 'wb') as out_file:
			shutil.copyfileobj(response, out_file)
		print("Extracting zip archive")
		with zipfile.ZipFile(filepath, 'r') as zip_ref:
			zip_ref.extractall(base_dir + "/")
		os.remove(filepath)
		
def process_files():
	dfs = []
	dfs.append(process_files1215())
	dfs.append(process_files1718())
	dfs.append(process_current_year())

	tot = pd.concat(dfs)
	tot = tot.loc[tot.ingressi_areac != 0, ["ingressi_areac"]]
	
	#visto che i dati del 2016 sono errati, riempio le date dell'anno con la media della stessa data degli altri anni
	for date in pd.date_range(start = "2016-01-01", end = "2016-12-31"):
		tot.loc[date, "ingressi_areac"] = tot.loc[(tot.index.day == date.day) & (tot.index.month == date.month)].ingressi_areac.mean()

	tot.ingressi_areac = tot.ingressi_areac.astype("int64")
	tot.index.name = "data"
	tot.to_csv(path + "/areac_alldata.csv")

	return tot

def process_files1215():
	files = glob.glob(path + "/*2012*.csv")
	files = files + glob.glob(path + "/*2013*.csv")
	files = files + glob.glob(path + "/*2014*.csv")
	files = files + glob.glob(path + "/*2015*.csv")
	dfs = []
	for file in files:
		print(f"Processing {file}")
		data = pd.read_csv(file, sep=";", parse_dates=["timeIndex"], index_col="timeIndex")
		data = data.loc[:, ["totale"]]
		data = data.rename(columns = {"totale": "ingressi_areac"})
		dfs.append(data)
	return pd.concat(dfs)

def date_parser_1718(s):
	s = s.split(" ")[0]
	return dt.datetime(int(s.split("/")[0]), int(s.split("/")[1]), int(s.split("/")[2]))

def process_files1718():
	files = glob.glob(path + "/*2017*.csv")
	files = files + glob.glob(path + "/*2018*.csv")
	dfs = []
	for file in files:
		print(f"Processing {file}")
		data = pd.read_csv(file, parse_dates=["dataora"], date_parser=date_parser_1718, index_col="dataora")
		data = data.loc[:, ["numero_transiti"]]
		data = data.rename(columns = {"numero_transiti": "ingressi_areac"})
		data = data.groupby(pd.Grouper(freq="d")).sum()
		dfs.append(data)
	return pd.concat(dfs)


def process_current_year():
	files = glob.glob(path + "/*2020*.csv")
	print(f"Processing {files[0]}")
	data = pd.read_csv(files[0], sep=";", parse_dates=["data_giorno"], index_col="data_giorno")
	data = data.rename(columns = {"numero_transiti_giornalieri": "ingressi_areac"})
	return data

#download_files()
#process_files()
