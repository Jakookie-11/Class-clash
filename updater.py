import os
import shutil
from urllib.request import urlopen
import zipfile
import sys
import time
import json
import funktions


os.makedirs("update", exist_ok=True)

url = funktions.daten_herunterladen()

antwort = urlopen(url)
inhalt = antwort.read()

datei = open("update/update.zip", "wb")
datei.write(inhalt)
datei.close()


datei = zipfile.ZipFile("update/update.zip", "r")
datei.extractall("update")
datei.close()


if os.path.exists("update/Class-clash-main/updater.py"):
    os.remove("update/Class-clash-main/updater.py")

if os.path.exists("update/Class-clash-main/saves"):
    shutil.rmtree("update/Class-clash-main/saves")

if os.path.exists("update/Class-clash-main/.vscode"):
    shutil.rmtree("update/Class-clash-main/.vscode")


for datei in os.listdir("."):

    if datei.endswith(".py") and datei != "updater.py":
        os.remove(datei)

    elif datei.endswith(".txt"):
        os.remove(datei)

    elif datei.endswith(".json"):
        os.remove(datei)

    elif datei.endswith(".zip"):
        os.remove(datei)


if os.path.exists("__pycache__"):
    shutil.rmtree("__pycache__")


for datei in os.listdir("update/Class-clash-main"):

    shutil.move(
        "update/Class-clash-main/" + datei,
        "."
    )


shutil.rmtree("update/")


import charaktere


for spieler in os.listdir("saves"):

    if (
        spieler.endswith(".json")
        and spieler != "confic_setup.json"
        and spieler != "passwoerter.json"
    ):

        datei = f"saves/{spieler}"
        datei = open(datei, "r")

        daten = json.load(datei)

        datei.close()


        for charakter in charaktere.Charaktere:

            if charakter not in daten["charaktere"]:

                neuer_charakter = charaktere.Charaktere[charakter]

                daten["charaktere"][charakter] = {
                    "hp": neuer_charakter.hp,
                    "max_hp": neuer_charakter.max_hp,
                    "max_max_hp": neuer_charakter.max_max_hp,
                    "schaden": neuer_charakter.schaden,
                    "level": neuer_charakter.level
                }


        datei = open(f"saves/{spieler}", "w")

        json.dump(daten, datei)

        datei.close()

import confic

with open("saves/confic_setup.json", "r") as datei:
    daten = json.load(datei)

confic.terminal_clear = daten["terminal_clear"]

os.system(confic.terminal_clear)

os.system(confic.terminal_clear)

time.sleep(2)

sys.exit()