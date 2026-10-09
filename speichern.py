import json
import os
import time
from datetime import datetime

import confic

import charaktere
import ressourcen
import spiel_starten
import herausforderungen


def alle_kampangen_laden():
    from kampange import alle_kampangen
    return alle_kampangen




def spiel_speichern(spieler, ist_erstellung = False):
    os.makedirs("saves", exist_ok=True)

    confic_setup_speichern()

    if not ist_erstellung and confic.start_zeit is not None:
        confic.end_zeit = int(time.time())
        confic.time_played_in_seconds += confic.end_zeit - confic.start_zeit
        confic.start_zeit = confic.end_zeit

    gespeicherter_herausforderungs_fortschritt = herausforderungen.Herausforderungs_fortschritt_speichern()
    gespeicherter_herausforderungs_kaempf_fortschritt = herausforderungen.Herausforderungs_kampf_fortschritt_speichern()

    spiel_starten.alle_statuseffekte_resetten()
    spiel_starten.alle_faehigkeits_abklingzeiten_resetten()
    spiel_starten.HP_zuruecksetzen()

    gespeicherte_charaktere = {}

    for name, charakter in charaktere.Charaktere.items():
        if getattr(charakter, "kampf_klon", False):
            continue
        if charakter.klasse != "npc":
            if charakter.klasse != "down_in_mars_gegner":
                gespeicherte_charaktere[name] = {
                    "name": charakter.name,
                    "level": charakter.level,
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
        "spieler_name"                       : spieler,
        "Erstellungsdatum"                   : erstellungsdatum,
        "Letztes_Speichern"                  : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "time_played_in_seconds"             : confic.time_played_in_seconds,
        "ressourcen"                         : ressourcen.ressourcen,
        "charaktere"                         : list(gespeicherte_charaktere.values()),
        "kampangen_fortschritt"              : gespeicherter_fortschritt,
        "Herausforderungs_Fortschritt"       : gespeicherter_herausforderungs_fortschritt,
        "Herausforderungs_Kampf_Fortschritt" : gespeicherter_herausforderungs_kaempf_fortschritt,
        "gewonnene_kaempfe"                  : confic.gewonnene_kaempfe,
    }

    with open(datei, "w", encoding="utf-8") as datei_ausgabe:
        json.dump(daten, datei_ausgabe)



def confic_setup_laden():
    os.makedirs("saves", exist_ok=True)
    datei = "saves/confic_setup.json"

    if not os.path.exists(datei):
        confic.first_start_configurator = True
        confic.terminal_clear = "clear"
        confic.passwort_sichtbarkeit = False
        confic.passwort_sichtbarkeitshinweis_anzeigen = True
        confic_setup_speichern()
        return

    with open(datei, "r", encoding="utf-8") as datei_lesen:
        daten = json.load(datei_lesen)

    confic.first_start_configurator = daten.get("starter_menue", True)
    confic.terminal_clear = daten.get("terminal_clear", "cls")
    confic.passwort_sichtbarkeit = daten.get("passwort_sichtbarkeit", False)
    confic.passwort_sichtbarkeitshinweis_anzeigen = daten.get("passwort_sichtbarkeitshinweis_anzeigen", True)



def confic_setup_speichern():
    os.makedirs("saves", exist_ok=True)
    datei = "saves/confic_setup.json"

    daten = {
        "starter_menue"  : confic.first_start_configurator,
        "terminal_clear" : confic.terminal_clear,
        "passwort_sichtbarkeit" : confic.passwort_sichtbarkeit,
        "passwort_sichtbarkeitshinweis_anzeigen" : confic.passwort_sichtbarkeitshinweis_anzeigen
    }

    with open(datei, "w", encoding="utf-8") as datei_ausgabe:
        json.dump(daten, datei_ausgabe)



def spiel_laden(spieler):
    datei = f"saves/{spieler}.json"

    if not os.path.exists(datei):
        return

    with open(datei, "r", encoding="utf-8") as datei_lesen:
        daten = json.load(datei_lesen)

    ressourcen.ressourcen                          = daten.get("ressourcen", ressourcen.ressourcen)
    herausforderungen.Herausforderungs_fortschritt_laden(daten.get("Herausforderungs_Fortschritt", []))
    confic.gewonnene_kaempfe                       = daten.get("gewonnene_kaempfe", confic.gewonnene_kaempfe)
    confic.time_played_in_seconds                   = daten.get("time_played_in_seconds", confic.time_played_in_seconds)

    gespeicherte_level = _charakter_level_normalisieren(
        daten.get("charaktere", {})
    )

    for name, charakter in charaktere.Charaktere.items():
        if charakter.klasse == "npc" or charakter.klasse == "down_in_mars_gegner":
            continue
        charaktere.charakter_auf_level_setzen(
            charakter,
            gespeicherte_level.get(name, charakter.basis_level)
        )

    for kampange in alle_kampangen_laden():
        kampangen_daten = daten.get("kampangen_fortschritt", {})
        kampange.fortschritt = kampangen_daten.get(kampange.nummer, kampange.fortschritt)


def spielstand_charaktere_laden(spieler):
    datei = f"saves/{spieler}.json"

    if not os.path.exists(datei):
        raise FileNotFoundError(f"Kein Spielstand für {spieler} gefunden.")

    with open(datei, "r", encoding="utf-8") as datei_lesen:
        daten = json.load(datei_lesen)

    return _charakter_level_normalisieren(daten.get("charaktere", {}))


def _charakter_level_normalisieren(gespeicherte_charaktere):
    if isinstance(gespeicherte_charaktere, dict):
        level_daten = {
            name: werte.get("level", 1) if isinstance(werte, dict) else werte
            for name, werte in gespeicherte_charaktere.items()
        }
    elif isinstance(gespeicherte_charaktere, list):
        level_daten = {}
        for eintrag in gespeicherte_charaktere:
            if not isinstance(eintrag, dict) or not isinstance(
                eintrag.get("name"), str
            ):
                raise ValueError("Ungültiger Charaktereintrag im Spielstand.")
            level_daten[eintrag["name"]] = eintrag.get("level")
    else:
        raise ValueError("Ungültiges Charakterformat im Spielstand.")

    for name, level in level_daten.items():
        if not isinstance(name, str) or type(level) is not int or level < 1:
            raise ValueError(f"Ungültiges Level für Charakter {name}.")

    return level_daten