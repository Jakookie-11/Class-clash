import os
import menues
import json
import sys
import msvcrt

import confic
from pfade import ressourcen_pfad
from urllib.request import urlopen


def menue(liste, spieler_name=None,):

    while True:

        os.system(confic.terminal_clear)

        #---printen der Wahlen---#
        for schlüssel in liste:
            print(schlüssel)

        #--zusätze für manche menüs---#
        if liste == menues.profil_menue:
            print()
            print(f"Aktuelle Passwort_art: {confic.passwort_art}")
            print()

        if liste == menues.audio_menue:
            print()

            if confic.ton == True:
                print(f"Ton        : An")
            else:
                print(f"Ton        : Aus")

            if confic.main_musik == True:
                print(f"Main Musik : An")
            else:
                print(f"Main Musik : Aus")

        #---Wahl---#
        auswahl = input("Wahl? ")

        if auswahl == "0":
            return(0)
        elif auswahl == "1":
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
        with ressourcen_pfad("version.txt").open("r", encoding="utf-8") as datei:
            return datei.read().strip()
    except FileNotFoundError:
        return "0.0.0"



def versionen_vergleichen():
    try:
        online_version = online_version_abrufen()

        with ressourcen_pfad("version.txt").open("r", encoding="utf-8") as datei:
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




def passwort_eingeben(prompt="Passwort: "):
    print(prompt, end="", flush=True)
    zeichen = []

    while True:
        taste = msvcrt.getwch()

        if taste in ("\r", "\n"):  # Enter
            print()
            return "".join(zeichen)

        if taste == "\b":  # Backspace
            if zeichen:
                zeichen.pop()
                sys.stdout.write("\b \b")
                sys.stdout.flush()
            continue

        if taste in ("\x00", "\xe0"):  # Sondertasten ignorieren
            msvcrt.getwch()
            continue

        if taste == "\x03":  # Strg+C
            raise KeyboardInterrupt

        if taste.isprintable():
            zeichen.append(taste)
            sys.stdout.write("*")
            sys.stdout.flush()




def ganzzahl_einlesen(prompt, minimum, maximum):
    while True:
        wahl = input(prompt).strip()

        if wahl.isdigit() and minimum <= int(wahl) <= maximum:
            return int(wahl)

        print(f"Bitte eine Zahl zwischen {minimum} und {maximum} eingeben.")
        zeilen_loeschen(2)