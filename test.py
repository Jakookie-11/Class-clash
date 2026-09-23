import getpass
import json
import os

import bcrypt


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


def shop_passwort_erstellen():
    """Erstellt oder ersetzt das Passwort für alle Käufe im Shop."""
    while True:
        passwort = getpass.getpass("Neues Shop-Passwort: ")

        if len(passwort) < 6:
            print("Das Shop-Passwort muss mindestens 6 Zeichen lang sein.")
            continue

        bestaetigung = getpass.getpass("Shop-Passwort bestaetigen: ")
        if passwort != bestaetigung:
            print("Die Passwoerter stimmen nicht ueberein.")
            continue

        break

    os.makedirs(os.path.dirname(PASSWOERTER_DATEI), exist_ok=True)
    daten = _passwoerter_laden()
    daten["shop_passwort"] = bcrypt.hashpw(
        passwort.encode("utf-8"),
        bcrypt.gensalt(),
    ).decode("utf-8")

    with open(PASSWOERTER_DATEI, "w", encoding="utf-8") as datei:
        json.dump(daten, datei, ensure_ascii=False, indent=2)

    print("Shop-Passwort erfolgreich gespeichert.")


if __name__ == "__main__":
    shop_passwort_erstellen()
