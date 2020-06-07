# Repository per le attività di tirocinio e realizzazione della tesi

Nella cartella src sono contenute le prime funzionalità sviluppate.

Per eseguire i file è necessario aver installato Python3 ed i package [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) e [Sickit-learn](https://scikit-learn.org/stable/index.html)

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
