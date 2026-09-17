import json
import os
from datetime import datetime

import confic

import charaktere
import ressourcen


def alle_kampangen_laden():
    from kampange import alle_kampangen
    return alle_kampangen




def spiel_speichern(spieler):
    os.makedirs("saves", exist_ok=True)

    gespeicherte_charaktere = {}

    for name, charakter in charaktere.Charaktere.items():
        gespeicherte_charaktere[name] = {
            "hp" : charakter.hp,
            "max_hp" : charakter.max_hp,
            "max_max_hp" : charakter.max_max_hp,
            "schaden" : charakter.schaden,
            "level" : charakter.level
        }

    gespeicherter_fortschritt = {}

    for kampange in alle_kampangen_laden():
        gespeicherter_fortschritt[kampange.nummer] = kampange.fortschritt

    datei = f"saves/{spieler}.json"

    #---Erstellungsdatum holen---#
    if os.path.exists(datei):
        with open(datei, "r", encoding="utf-8") as alte_datei:
            alte_daten = json.load(alte_datei)

        erstellungsdatum = alte_daten.get("Erstellungsdatum", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    else:
        erstellungsdatum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    daten = {
        "spieler_name"    : spieler,
        "Erstellungsdatum" : erstellungsdatum,
        "Letztes_Speichern" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ressourcen"      : ressourcen.ressourcen,
        "charaktere"      : gespeicherte_charaktere,
        "kampangen_fortschritt" : gespeicherter_fortschritt
    }

    with open(datei, "w", encoding="utf-8") as datei_ausgabe:
        json.dump(daten, datei_ausgabe)



def confic_setup_laden():
    os.makedirs("saves", exist_ok=True)
    datei = "saves/confic_setup.json"

    if not os.path.exists(datei):
        confic.first_start_configurator = True
        confic.terminal_clear = "clear"
        confic_setup_speichern()
        return

    with open(datei, "r", encoding="utf-8") as datei_lesen:
        daten = json.load(datei_lesen)

    confic.first_start_configurator = daten.get("starter_menue", True)
    confic.terminal_clear = daten.get("terminal_clear", "clear")



def confic_setup_speichern():
    os.makedirs("saves", exist_ok=True)
    datei = "saves/confic_setup.json"

    daten = {
        "starter_menue"  : confic.first_start_configurator,
        "terminal_clear" : confic.terminal_clear
    }

    with open(datei, "w", encoding="utf-8") as datei_ausgabe:
        json.dump(daten, datei_ausgabe)



def spiel_laden(spieler):
    datei = f"saves/{spieler}.json"

    if not os.path.exists(datei):
        return

    with open(datei, "r", encoding="utf-8") as datei_lesen:
        daten = json.load(datei_lesen)

    ressourcen.ressourcen = daten.get("ressourcen", ressourcen.ressourcen)

    for name, gespeicherte_charaktere in daten.get("charaktere", {}).items():
        if name not in charaktere.Charaktere:
            continue

        charakter = charaktere.Charaktere[name]

        charakter.hp = gespeicherte_charaktere.get("hp", charakter.hp)
        charakter.max_hp = gespeicherte_charaktere.get("max_hp", charakter.max_hp)
        charakter.max_max_hp = gespeicherte_charaktere.get("max_max_hp", charakter.max_max_hp)
        charakter.schaden = gespeicherte_charaktere.get("schaden", charakter.schaden)
        charakter.level = gespeicherte_charaktere.get("level", charakter.level)

    for kampange in alle_kampangen_laden():
        kampangen_daten = daten.get("kampangen_fortschritt", {})
        kampange.fortschritt = kampangen_daten.get(kampange.nummer, kampange.fortschritt)