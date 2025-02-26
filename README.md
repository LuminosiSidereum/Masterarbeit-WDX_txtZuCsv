# WDX CSV Ersteller

## Funktionsweise
Dieses Programm verarbeitet `.txt`-Dateien, die Messdaten enthalten, und konvertiert sie in `.csv`-Dateien mit standardisierten Dateinamen.  
Dabei werden die benötigten Parameter aus der Konfigurationsdatei `config.json` ausgelesen und in die Dateibenennung integriert.  

## Nutzung des Skripts
### Eingabedaten
- Das Skript erwartet `.txt`-Dateien im selben Verzeichnis, die Messdaten enthalten.
- Die Dateinamen müssen mit `_map` enden und an erster Stelle eine Zahl enthalten, die in der `config.json` definiert ist.
- Die `config.json` muss im selben Verzeichnis liegen und folgende Struktur haben:
  ```json
  {
      "basicFileName": "0000-10-06-240927",
      "1": "N",
      "2": "Fe",
      "3": "Zr"
  }
- "basicFileName" gibt den allgemeinen Präfix für die erzeugten .csv-Dateien an.
- Die Zahlen (z. B. "1", "2", "3") stehen für Elemente, die aus der txt-Datei extrahiert werden.

### Ausführung
- Stelle sicher, dass sich die .txt-Dateien und die config.json im selben Verzeichnis wie das Skript befinden.
- Stelle sicher, dass die config.json die korrekten Parameter enthält. 
- Starte das Skript `wdx_csv_ersteller.py`.
- Gib die Verzeichnisnummer der Messdateien ein, wenn das Programm danach fragt.
- Das Skript verarbeitet alle passenden .txt-Dateien und speichert sie als .csv.
### Ausgabe
- Die generierten .csv-Dateien enthalten die umformatierten Messdaten.
- Die neuen Dateinamen haben folgendes Muster:
    {basicFileName}-{Verzeichnisnummer}_{ErsteZifferDerDatei}_{Element}.csv
    Beispiel für eine Datei mit "1" als Startziffer:
    0000-10-06-240927-12_N.csv