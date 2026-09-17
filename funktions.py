import os
import time
import zipfile
import shutil
import json

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
    try:
        url = "https://api.github.com/repos/Jakookie-11/Class-clash/releases/latest"
        with urlopen(url, timeout=5) as github_antwort:
            daten = json.loads(github_antwort.read().decode("utf-8"))

        if "tag_name" in daten:
            return daten["tag_name"]
    except Exception:
        pass

    return lokale_version_abrufen()



def lokale_version_abrufen():
    try:
        with open("version.txt", "r", encoding="utf-8") as datei:
            return datei.read().strip()
    except FileNotFoundError:
        return "0.0.0"



def versionen_vergleichen():
    try:
        online_version = online_version_abrufen()

        with open("version.txt", "r", encoding="utf-8") as datei:
            aktuelle_version = datei.read().strip()

        return online_version == aktuelle_version

    except FileNotFoundError:
        return True
    except Exception:
        return True




def daten_herunterladen():
    url = "https://api.github.com/repos/Jakookie-11/Class-clash/releases/latest"
    github_antwort = urlopen(url)
    
    daten = json.loads(github_antwort.read())

    for asset in daten["assets"]:
        if asset["name"] == "update.zip":
            url_to_return = asset["browser_download_url"]


    return url_to_return