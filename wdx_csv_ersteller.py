import pandas as pd
import json
import os
import sys
import shutil
import time
from pathlib import Path

def createCSVFileName(filename:str,dirNum:str,config:dict)->str:
    if filename[0] in ["1","2","3"]:
        filename:str  = f"{config["basicFileName"]}-{dirNum}_{filename[0]}_{config[filename[0]]}.csv"
    return filename

def main(directorycontent:list)->None:
    try:
        with open("config.json", "r") as configfile:
            config:dict = json.load(configfile)
    except:
        print("Konfigurationsdatei nicht gefunden oder beschädigt.")
        print("Das Programm wird beendet.")
        time.sleep(3)
        quit()
        
    validDirectory:bool = False
    while validDirectory == False:
        inputDirectoryNumber:str = input("Bitte geben Sie die Verzeichnisnummer der Maps an: ")
        inputDirectoryNumber.strip()
        if inputDirectoryNumber.isdigit() == False:
            print("Ungültige Eingabe!")
        else:
            validDirectory = True
            
    for os_file in directorycontent:
        file:Path = Path(os_file)
        if os.path.isfile(file) and file.suffix == ".txt" and file.stem.endswith("_map"):
            data:pd.DataFrame = pd.read_csv(file, sep="\t", header=None)
            newFileName:str = createCSVFileName(file.stem,inputDirectoryNumber, config)
            data.to_csv(newFileName, index=False, header=False)
            print(f"Erstellt: {newFileName}")
    
if __name__ == "__main__":
    # Setze das Arbeitsverzeichnis auf den Ordner der Python-Datei
    script_dir:str = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(script_dir)
    
    # Prüfe ob das Verzeichnis leer ist
    directorycontent:list = os.listdir()
    if len(directorycontent) == 0:
        print("Das Verzeichnis ist leer.")
        print("Das Programm wird beendet.")
        time.sleep(3)
        quit()
    main(directorycontent)
    input("Drücken Sie Enter zum Beenden...")