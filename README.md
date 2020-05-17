# Repository per le attività di tirocinio e realizzazione della tesi

Nella cartella src sono contenute le prime funzionalità sviluppate.

Per eseguire i file è necessario aver installato Python3 e il package [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) (installabile via pip, col comando 'pip3 -m install pandas')

## get_data.py
Si occupa di scaricare gli archivi zip dal sito di Regione Lombardia e di estrarre i CSV in una cartella specifica dalla quale saranno poi prelevati per essere elaborati.

## process_csv.py
Partendo dai CSV annuali scaricati in precedenza vengono generati i CSV di tutti i sensori

## info_stazioni.py
Man mano saranno aggiunte funzionalità necessarie per sapere varie informazioni sulle stazioni di rilevamento e sui sensori, come ad es. i sensori di una stazione dato il suo id, o le stazioni di un determinato posto

## data_preparation.py
Ho iniziato a scrivere un po' di codice per preparare la tabella dei dati da dare in pasto all'algoritmo Random Forest, che deve racchiudere, per ogni data, la concentrazione dell'inquinante scelto e le varie misurazioni metereologiche.
Da questa tabella poi si potrà ottenere la serie normalizzata.
