import os
import time
import zipfile
import shutil

import confic
from urllib.request import urlopen

def menue(bibliothek, spieler_name=None,):

    while True:

        os.system(confic.terminal_clear)

        #---printen der Wahlen---#
        for schlüssel, wert in bibliothek.items():
            print(schlüssel)

        #---Wahl---#
        auswahl = input("Wahl? ")

        if auswahl == "1":
            return(1)
        elif auswahl == "2":
            return (2)
        elif auswahl == "3":
            return(3)
        elif auswahl == "4":
            return(4)
        elif auswahl == "4":
            return(4)
        elif auswahl == "5":
            return(5)
        elif auswahl == "6":
            return(6)
        elif auswahl == "7":
            return(7)
        elif auswahl == "8":
            return(8)
        else:
            continue




def bestaetigung_menue(wofür):

    brake = False
    ready = input("Fertig?")

    while brake == False:

        if ready == "ja":
            brake = True
            os.system(confic.terminal_clear)

        else:
            os.system(confic.terminal_clear)
            if isinstance(wofür, str):
                print(wofür)

                ready = input("Fertig?")

            elif isinstance(wofür, dict):
                for schlüssel, wert in wofür.items():
                    print(schlüssel)

                ready = input("Fertig? ")



def zeilen_loeschen(anzahl):
    for _ in range(anzahl):
        print("\033[1A\033[2K", end="")



def online_version_abrufen():
    url = "https://raw.githubusercontent.com/Jakookie-11/Class-clash/Version-information-and-asking/version.txt"

    antwort = urlopen(url)
    inhalt = antwort.read().decode("utf-8")

    return inhalt



def update_herunterladen():
    os.makedirs("update", exist_ok=True)
    url = "https://raw.githubusercontent.com/Jakookie-11/Class-clash/Version-information-and-asking/Class-clash-Version-information-and-asking.zip"

    antwort = urlopen(url)
    inhalt = antwort.read()

    datei = open("update/update.zip", "wb")
    datei.write(inhalt)
    datei.close()

    datei = zipfile.ZipFile("update/update.zip", "r")
    datei.extractall("update")
    datei.close()

    os.remove("update/update.zip")
    shutil.rmtree("update/Class-clash-Version-information-and-asking/saves")
    shutil.rmtree("update/Class-clash-Version-information-and-asking/.vscode")



def versionen_vergleichen():

    online_version = online_version_abrufen()

    aktuelle_version = confic.version

    if online_version == aktuelle_version:

        return True

    else:
        return False
