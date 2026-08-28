import json

import charaktere
import ressourcen




def spiel_speichern(spieler):

    gespeicherte_charaktere = {}

    for name, charakter in charaktere.Charaktere.items():
        gespeicherte_charaktere[name] = {
            "hp" : charakter.hp,
            "schaden" : charakter.schaden,
            "level" : charakter.level
        }

    datei = f"saves/{spieler}.json"

    datei = open(datei, "w")

    daten = {
        "spieler_name"    : spieler,
        "ressourcen"      : ressourcen.ressourcen,
        "charaktere"      : gespeicherte_charaktere
    }

    json.dump(daten, datei)

    datei.close()



def spiel_laden(spieler):

    datei = f"saves/{spieler}.json"

    datei = open(datei, "r")

    daten = json.load(datei)

    datei.close()

    ressourcen.ressourcen = daten["ressourcen"]

    for name, gespeicherte_charaktere in daten["charaktere"].items():

        charakter = charaktere.Charaktere[name]

        charakter.hp = gespeicherte_charaktere["hp"]
        charakter.schaden = gespeicherte_charaktere["schaden"]
        charakter.level = gespeicherte_charaktere["level"]