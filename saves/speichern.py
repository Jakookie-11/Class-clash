import json
import os
from datetime import datetime

import confic

import charaktere
import ressourcen




def spiel_speichern(spieler):

    gespeicherte_charaktere = {}

    for name, charakter in charaktere.Charaktere.items():
        gespeicherte_charaktere[name] = {
            "hp" : charakter.hp,
            "max_hp" : charakter.max_hp,
            "max_max_hp" : charakter.max_max_hp,
            "schaden" : charakter.schaden,
            "level" : charakter.level
        }

    datei = f"saves/{spieler}.json"

    #---Erstellungsdatum holen---#
    if os.path.exists(datei):
        alte_datei = open(datei, "r")
        alte_daten = json.load(alte_datei)
        alte_datei.close()

        erstellungsdatum = alte_daten["Erstellungsdatum"]
    else:
        erstellungsdatum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    datei = open(datei, "w")

    daten = {
        "spieler_name"    : spieler,
        "Erstellungsdatum" : erstellungsdatum,
        "Letztes_Speichern" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ressourcen"      : ressourcen.ressourcen,
        "charaktere"      : gespeicherte_charaktere
    }

    json.dump(daten, datei)

    datei.close()



def confic_setup_laden():
    datei = f"saves/confic_setup.json"
    datei = open(datei, "r")

    daten = json.load(datei)

    datei.close()

    confic.first_start_configurator = daten["starter_menue"]
    confic.terminal_clear = daten["terminal_clear"]



def confic_setup_speichern():
    datei = f"saves/confic_setup.json"
    datei = open(datei, "w")

    daten = {
        "starter_menue"  : confic.first_start_configurator,
        "terminal_clear" : confic.terminal_clear
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
        charakter.max_hp = gespeicherte_charaktere["max_hp"]
        charakter.max_max_hp = gespeicherte_charaktere["max_max_hp"]
        charakter.schaden = gespeicherte_charaktere["schaden"]
        charakter.level = gespeicherte_charaktere["level"]