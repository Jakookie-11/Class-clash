import csv
import ctypes
import json
import os
import time
from datetime import datetime

import confic

import charaktere
import ressourcen
import spiel_starten
import herausforderungen


LEADERBOARD_EMAIL = "dcs.acc_05@yahoo.com"


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
    gespeicherte_lautstaerke = confic.lautstaerke
    gespeicherter_ton = confic.ton
    gespeicherte_main_musik = confic.main_musik

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
        "lautstaerke"                        : gespeicherte_lautstaerke,
        "ton"                                : gespeicherter_ton,
        "main_musik"                         : gespeicherte_main_musik,
        "ressourcen"                         : ressourcen.ressourcen,
        "charaktere"                         : list(gespeicherte_charaktere.values()),
        "kampangen_fortschritt"              : gespeicherter_fortschritt,
        "Herausforderungs_Fortschritt"       : gespeicherter_herausforderungs_fortschritt,
        "Herausforderungs_Kampf_Fortschritt" : gespeicherter_herausforderungs_kaempf_fortschritt,
        "gewonnene_kaempfe"                  : confic.gewonnene_kaempfe,
    }

    with open(datei, "w", encoding="utf-8") as datei_ausgabe:
        json.dump(daten, datei_ausgabe)



def leaderboard_csv_exportieren(spieler):
    spiel_speichern(spieler)

    zeitstempel = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    export_datei = os.path.join("saves", f"leaderboard_export_{zeitstempel}.csv")

    with open(export_datei, "w", newline="", encoding="utf-8-sig") as datei_ausgabe:
        writer = csv.writer(datei_ausgabe, delimiter=";")
        writer.writerow(("Spielername", "Spielzeit in Sekunden", "Gewonnene Kämpfe"))
        writer.writerow((
            spieler,
            confic.time_played_in_seconds,
            confic.gewonnene_kaempfe,
        ))

    return export_datei


def leaderboard_email_entwurf_oeffnen(spieler, csv_datei):
    class MapiRecipDesc(ctypes.Structure):
        _fields_ = [
            ("ulReserved", ctypes.c_ulong),
            ("ulRecipClass", ctypes.c_ulong),
            ("lpszName", ctypes.c_char_p),
            ("lpszAddress", ctypes.c_char_p),
            ("ulEIDSize", ctypes.c_ulong),
            ("lpEntryID", ctypes.c_void_p),
        ]

    class MapiFileDesc(ctypes.Structure):
        _fields_ = [
            ("ulReserved", ctypes.c_ulong),
            ("flFlags", ctypes.c_ulong),
            ("nPosition", ctypes.c_ulong),
            ("lpszPathName", ctypes.c_char_p),
            ("lpszFileName", ctypes.c_char_p),
            ("lpFileType", ctypes.c_void_p),
        ]

    class MapiMessage(ctypes.Structure):
        _fields_ = [
            ("ulReserved", ctypes.c_ulong),
            ("lpszSubject", ctypes.c_char_p),
            ("lpszNoteText", ctypes.c_char_p),
            ("lpszMessageType", ctypes.c_char_p),
            ("lpszDateReceived", ctypes.c_char_p),
            ("lpszConversationID", ctypes.c_char_p),
            ("flFlags", ctypes.c_ulong),
            ("lpOriginator", ctypes.POINTER(MapiRecipDesc)),
            ("nRecipCount", ctypes.c_ulong),
            ("lpRecips", ctypes.POINTER(MapiRecipDesc)),
            ("nFileCount", ctypes.c_ulong),
            ("lpFiles", ctypes.POINTER(MapiFileDesc)),
        ]

    def mapi_text(text):
        return text.encode("mbcs", errors="replace")

    recipient_name = mapi_text(LEADERBOARD_EMAIL)
    recipient_address = mapi_text("SMTP:" + LEADERBOARD_EMAIL)
    subject = mapi_text(f"Class Clash Leaderboard-Daten: {spieler}")
    body = mapi_text(
        f"Hallo,\n\nanbei sind meine Leaderboard-Daten aus Class Clash.\n"
        f"Spielername: {spieler}\n"
    )
    attachment_path = mapi_text(os.path.abspath(csv_datei))
    attachment_name = mapi_text(os.path.basename(csv_datei))

    recipient = MapiRecipDesc(
        0, 1, recipient_name, recipient_address, 0, None
    )
    attachment = MapiFileDesc(
        0, 0, 0xFFFFFFFF, attachment_path, attachment_name, None
    )
    message = MapiMessage(
        0,
        subject,
        body,
        None,
        None,
        None,
        0,
        None,
        1,
        ctypes.pointer(recipient),
        1,
        ctypes.pointer(attachment),
    )

    try:
        mapi = ctypes.WinDLL("MAPI32.DLL")
        send_mail = mapi.MAPISendMail
    except OSError as fehler:
        raise OSError(
            "Windows Simple MAPI ist nicht verfügbar. Prüfe, ob ein "
            "MAPI-kompatibles E-Mail-Programm installiert und eingerichtet ist."
        ) from fehler
    except AttributeError as fehler:
        raise OSError(
            "Die Windows-MAPI-Schnittstelle zum Öffnen des E-Mail-Fensters fehlt."
        ) from fehler

    send_mail.argtypes = [
        ctypes.c_ulong,
        ctypes.c_void_p,
        ctypes.POINTER(MapiMessage),
        ctypes.c_ulong,
        ctypes.c_ulong,
    ]
    send_mail.restype = ctypes.c_ulong
    ergebnis = send_mail(
        0,
        None,
        ctypes.byref(message),
        0x00000008,
        0,
    )

    if ergebnis == 1:
        return False
    if ergebnis != 0:
        raise OSError(
            f"Das E-Mail-Fenster konnte nicht geöffnet werden (MAPI-Fehler {ergebnis})."
        )
    return True



def confic_setup_laden():
    os.makedirs("saves", exist_ok=True)
    datei = "saves/confic_setup.json"

    if not os.path.exists(datei):
        confic.first_start_configurator = True
        confic.terminal_clear = "clear"
        confic.passwort_art = "sternchen"
        confic.passwort_artshinweis_anzeigen = True
        confic_setup_speichern()
        return

    with open(datei, "r", encoding="utf-8") as datei_lesen:
        daten = json.load(datei_lesen)

    confic.first_start_configurator = daten.get("starter_menue", True)
    confic.terminal_clear = daten.get("terminal_clear", "cls")
    confic.passwort_art = daten.get("passwort_art", "sternchen")
    confic.passwort_artshinweis_anzeigen = daten.get("passwort_artshinweis_anzeigen", True)



def confic_setup_speichern():
    os.makedirs("saves", exist_ok=True)
    datei = "saves/confic_setup.json"

    daten = {
        "starter_menue"  : confic.first_start_configurator,
        "terminal_clear" : confic.terminal_clear,
        "passwort_art" : confic.passwort_art,
        "passwort_artshinweis_anzeigen" : confic.passwort_artshinweis_anzeigen
    }

    with open(datei, "w", encoding="utf-8") as datei_ausgabe:
        json.dump(daten, datei_ausgabe)



def spiel_laden(spieler):
    datei = f"saves/{spieler}.json"

    if not os.path.exists(datei):
        return

    with open(datei, "r", encoding="utf-8") as datei_lesen:
        daten = json.load(datei_lesen)

    herausforderungen.Herausforderungs_fortschritt_laden(daten.get("Herausforderungs_Fortschritt", []))
    ressourcen.ressourcen                          = daten.get("ressourcen", ressourcen.ressourcen)
    confic.gewonnene_kaempfe                       = daten.get("gewonnene_kaempfe", confic.gewonnene_kaempfe)
    confic.time_played_in_seconds                  = daten.get("time_played_in_seconds", confic.time_played_in_seconds)
    confic.lautstaerke                             = daten.get("lautstaerke", confic.lautstaerke)
    confic.ton                                     = daten.get("ton", confic.ton)
    confic.main_musik                              = daten.get("main_musik", confic.main_musik)

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