#----------Tests----------#

import json
import confic

datei = f"saves/passwoerter.json"
datei = open(datei, "w")

for spieler, passwort in confic.passwoerter.items():
    passwort = passwort.decode("utf-8")
    confic.passwoerter[spieler] = passwort

daten = {
    "passwoerter": confic.passwoerter
}

json.dump(daten, datei)
datei.close()