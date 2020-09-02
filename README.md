# Normalizzazione dati inquinamento atmosferico 

## Cos'è la normalizzazione dei dati dell'inquinamento atmosferico? 
Le concentrazioni degli inquinanti atmosferici sono fortemente influenzate dalle condizioni meteorologiche, che possono favorirne l'accumulo o la dispersione, e questo porta ad avere grande variabilità nei valori misurati anche in giornate molto vicine. Per normalizzazione dei dati dell'inquinamento si intende quindi quel processo, basato sull'utilizzo dell'algoritmo di machine learning Random Forest, che ci permette di ricavare, partendo dalla serie storica registrata da un sensore, l'andamento delle concentrazioni di tale inquinante indipendentemente dalle condizioni meteorologiche di ogni giornata. Così facendo diventa poi più semplice fare analisi sugli andamenti delle concentrazioni e sull'efficacia delle misure prese per il loro contenimento.

## Cosa troviamo in questo repository? 
Nella cartella src sono contenuti sia i file sorgenti del codice utilizzato per il recupero dei dati dai dataset pubblici di ARPA Lombardia che per la creazione dei modelli con Random Forest e il ricavo delle serie normalizzate.  
Sono inoltre contenuti alcuni notebook in cui sono svolte delle analisi sugli andamenti degli inquinanti dopo aver ricavato le serie normalizzate, così da vedere quali vantaggi e quali considerazioni ci permette di fare questo approccio.  

## Istruzioni 
Per eseguire il codice è necessario aver installato Python3 ed i package [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) e [Sickit-learn](https://scikit-learn.org/stable/index.html)

Inoltre per poter consultare i notebook è necessario aver installato [IPython](https://ipython.org) e [Jupyter Notebook](https://jupyter.org)

Per prima cosa è importante eseguire lo script di build **build.py**, che si occuperà di preparare dei dati pre-generati necessari per poter eseguire il codice contenuto nei notebook senza dover aspettare la lunga generazione delle serie normalizzate. 

	./build.py

Successivamente è possibile eseguire tutto il codice contenuto nel notebook **AnalisiIntroduttive.ipynb**, in cui vengono analizzati, tramite l'uso della normalizzazione, gli andamenti dei principali inquinanti nei capoluoghi lombardi.

	jupyter notebook src/AnalisiIntroduttive.ipynb

Con comandi simili è possibile anche consultare i notebook AnalisiTraffico.ipynb e AnalisiCovid.ipynb, in cui viene applicata la nostra tecnica di normalizzazione dei dati per provare ad analizzare l'impatto del traffico e del lockdown durante l'epidemia di COVID-19 sulle concentrazioni degli inquinanti.

Se siete interessati a provare a svolgere ulteriori analisi sui dati messi a disposizione da ARPA Lombardia, lo script **alldata.py**, contenuto nella cartella 'src', si occupa di fare il download di tutti i dataset, sia per quanto riguarda gli inquinanti, che le variabili meteorologiche che i dataset di Area C, e il processamento in file CSV per singolo sensore (WARNING: è un processo molto lento, sul mio notebook i7, 8GB di RAM richiede circa 1 ora). Una volta generati questi file è possibile usare il codice contenuto nei file di questa cartella per applicare la normalizzazione ai dati di interesse, ripetendo le modalità illustrate nei notebook.

## Link utili
- [Dataset sensori meteo](https://www.dati.lombardia.it/browse?q=sensori%20meteo&sortBy=relevance)
- [Dataset sensori aria](https://www.dati.lombardia.it/browse?q=sensori%20aria&sortBy=relevance)
- [Dataset ingressi Area C](https://dati.comune.milano.it/organization/comunedimilano?q=area+c&sort=score+desc%2C+metadata_modified+desc)

## Contenuto file 
Breve descrizione del contenuto dei file presenti nella cartella 'src' (TODO per prossimi commit è sicuramente la documentazione di tutto questo codice).

### Air Normalizer.py
Classe creata per gestire tutti gli aspetti relativi alla normalizzazione dei dati sull'inquinamento: split dei dati in training e testing set, creazione del modello, valutazione delle sue performance e dell'importanza delle variabili e generazione della timeseries normalizzata.

### RandomForest.ipynb
Nel notebook sono state fatte una serie di prove per verificare l'applicabilità dell'algoritmo random forest per ottenere la normalizzazione dei dati sull'inquinamento atmosferico. Sono stati analizzati i modelli creati per due inquinanti - PM10 e NOx - per testare i possibili miglioramenti da applicare prima di passare ad usare la tecnica per le analisi successive, oltre che a controllare eventuali differenze sui risultati ottenuti per i diversi inquinanti. 

### Analisi introduttive.ipynb
In questo notebook sono svolte una serie di analisi sull'andamento delle serie normalizzate dei principali inquinani atmosferici nei capoluoghi di provincia lombardi. In questo notebook viene quindi usata la normalizzazione per valuitarne vantaggi e risultati ottenibili dalla sua applicazione.

### AnalisiTraffico.ipynb
In questo notebook sono svolte una serie di analisi per verificare come la nsotra tecnica possa essere utilizzata per verificare l'impatto del traffico sulle concentrazioni degli inquinanti e quale sia stato l'effetto di alcune misure limitative prese nella città di Milano.

### AnalisiCovid.ipynb
In questo notebook vengono fatte una serie di analisi per verificare, tramite l'uso di random forest, quale sia stato l'impatto del lockdown sulle concentrazioni degli inquinanti.

### get_data.py
Si occupa di scaricare gli archivi zip dal sito di Regione Lombardia e di estrarre i CSV in una cartella specifica dalla quale saranno poi prelevati per essere elaborati.

### get_data_areac.py
Script che si occupa di recuperare i dataset degli ingressi in Area C, pubblicati dal comune di Milano, e di organizzarli in un file csv pronto per essere utilizzato nella costruzione dei modelli di random forest.

### process_csv.py
Partendo dai CSV annuali scaricati in precedenza vengono generati i CSV di tutti i sensori

### info_stazioni.py
Man mano saranno aggiunte funzionalità necessarie per sapere varie informazioni sulle stazioni di rilevamento e sui sensori, come ad es. i sensori di una stazione dato il suo id, o le stazioni di un determinato posto

### data_preparation.py
Funzioni per preparare la tabella dei dati necessaria per poter applicare l'algoritmo random forest per ottenere la timeseries normalizzata.

### sensori_capoluoghi.csv
File CSV contenente gli ID dei sensori di ciascun capoluogo per tutte le variabili e gli inquinanti usati nelle nostre analisi.
