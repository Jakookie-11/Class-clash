import os
import getpass
import json
import bcrypt

import speichern
import menues
import ressourcen
import confic


PASSWOERTER_DATEI = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "saves",
    "passwoerter.json",
)


def _passwoerter_laden():
    if not os.path.exists(PASSWOERTER_DATEI):
        return {"passwoerter": {}}

    with open(PASSWOERTER_DATEI, "r", encoding="utf-8") as datei:
        daten = json.load(datei)

    if not isinstance(daten, dict):
        raise ValueError("Die Passwortdatei muss ein JSON-Objekt enthalten.")

    return daten


def shop_passwort_pruefen(passwort):
    """Prueft ein eingegebenes Shop-Passwort gegen den gespeicherten Hash."""
    daten = _passwoerter_laden()
    gespeichertes_passwort = daten.get("shop_passwort")

    if not isinstance(gespeichertes_passwort, str):
        return False

    return bcrypt.checkpw(
        passwort.encode("utf-8"),
        gespeichertes_passwort.encode("utf-8"),
    )

def shop(spieler_name):

    while  True:
        os.system(confic.terminal_clear)
        print("══════════════════════════════")
        print("             Shop")
        print("══════════════════════════════")
        print()
        print("═══════════Guthaben═══════════")
        ressourcen.ressourcen_anzeigen()
        print("══════════════════════════════")
        print()
        print("Zu Kaufen:")
        print()

        for schlüssel, wert in menues.shop_menue.items():
            print(schlüssel)

        wahl = input("Wahl? ")

        if wahl in {"1", "2", "3", "4"}:
            passwort = getpass.getpass("Shop-Passwort: ")

            if not shop_passwort_pruefen(passwort):
                print("Shop-Passwort falsch oder noch nicht eingerichtet.")
                input("Enter...")
                continue

        if wahl == "1":
            ressourcen.ressourcen_verändern("Credits", 1000)

        elif wahl == "2":
            ressourcen.ressourcen_verändern("M_Credits", 1000)

        elif wahl == "3":
            ressourcen.ressourcen_verändern("Material 1", 20)

        elif wahl == "4":
            ressourcen.ressourcen_verändern("Energie", 20)

        elif wahl == "5":
            speichern.spiel_speichern(spieler_name)
            return 1

        else:
            print("Ungueltige Auswahl.")
