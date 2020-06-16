# Repository per le attività di tirocinio e realizzazione della tesi

Per eseguire i file è necessario aver installato Python3 ed i package [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) e [Sickit-learn](https://scikit-learn.org/stable/index.html)

Inoltre per poter consultare i notebook è necessario aver installato [IPython](https://ipython.org) e [Jupyter Notebook](https://jupyter.org)

##Air Normalizer.py
Classe creata per gestire tutti gli aspetti relativi alla normalizzazione dei dati sull'inquinamento: split dei dati in training e testing set, creazione del modello, valutazione delle sue performance e dell'importanza delle variabili e generazione della timeseries normalizzata.

## RandomForest.ipynb
Nel notebook sono state fatte una serie di prove per verificare l'applicabilità dell'algoritmo random forest per ottenere la normalizzazione dei dati sull'inquinamento atmosferico. Sono stati analizzati i modelli creati per due inquinanti - PM10 e NOx - per testare i possibili miglioramenti da applicare prima di passare ad usare la tecnica per le analisi successive, oltre che a controllare eventuali differenze sui risultati ottenuti per i diversi inquinanti. 

## get_data.py
Si occupa di scaricare gli archivi zip dal sito di Regione Lombardia e di estrarre i CSV in una cartella specifica dalla quale saranno poi prelevati per essere elaborati.

## process_csv.py
Partendo dai CSV annuali scaricati in precedenza vengono generati i CSV di tutti i sensori

## info_stazioni.py
Man mano saranno aggiunte funzionalità necessarie per sapere varie informazioni sulle stazioni di rilevamento e sui sensori, come ad es. i sensori di una stazione dato il suo id, o le stazioni di un determinato posto

## data_preparation.py
Funzioni per preparare la tabella dei dati necessaria per poter applicare l'algoritmo random forest per ottenere la timeseries normalizzata.

## RandomForest.ipynb
Notebook in cui sto facendo le prove per verificare l'applicabilità dell'algoritmo random forest per normalizzare le concentrazioni degli inquinanti.
