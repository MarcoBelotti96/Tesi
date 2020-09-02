#Recupero dei dataset e processamento CSV
import get_data as gd
import process_csv as pc
import get_data_areac as gdac

if __name__ == "__main__":
	gd.download_files()
	pc.process_csv()
	gdac.download_files()
	gdac.process_files() 
