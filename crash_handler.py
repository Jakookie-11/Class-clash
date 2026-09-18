import os
import hashlib
import traceback
from datetime import datetime


CRASH_ORDNER = "crash_logs"


def crash_speichern(spieler):

    os.makedirs(CRASH_ORDNER, exist_ok=True)

    jetzt = datetime.now()

    datum = jetzt.strftime("%Y-%m-%d")
    uhrzeit = jetzt.strftime("%H:%M:%S")

    # Kompletter Fehler inklusive Traceback
    fehler_text = traceback.format_exc()

    # Eindeutige ID für denselben Fehler
    fehler_id = hashlib.sha256(
        fehler_text.encode("utf-8")
    ).hexdigest()

    # Prüfen, ob dieser Fehler bereits existiert
    for dateiname in os.listdir(CRASH_ORDNER):

        if not dateiname.endswith(".txt"):
            continue

        dateipfad = os.path.join(
            CRASH_ORDNER,
            dateiname
        )

        with open(
            dateipfad,
            "r",
            encoding="utf-8"
        ) as datei:

            inhalt = datei.read()

        if f"Fehler-ID: {fehler_id}" in inhalt:

            return (
                dateiname,
                fehler_id,
                os.path.abspath(dateipfad)
            )

    # Neue Nummer für den Crash-Report suchen
    nummer = 1

    while True:

        dateiname = f"crash_{nummer:03d}.txt"

        dateipfad = os.path.join(
            CRASH_ORDNER,
            dateiname
        )

        if not os.path.exists(dateipfad):
            break

        nummer += 1

    # Crash-Report erstellen
    with open(
        dateipfad,
        "w",
        encoding="utf-8"
    ) as datei:

        datei.write(
            "========================================\n"
        )
        datei.write(
            "       CLASS CLASH CRASH REPORT\n"
        )
        datei.write(
            "========================================\n\n"
        )

        datei.write(
            f"Spieler: {spieler}\n"
        )

        datei.write(
            f"Datum: {datum}\n"
        )

        datei.write(
            f"Uhrzeit: {uhrzeit}\n"
        )

        datei.write(
            f"Fehler-ID: {fehler_id}\n"
        )

        datei.write(
            "Status: NICHT_GESENDET\n\n"
        )

        datei.write(
            "----------------------------------------\n"
        )
        datei.write(
            "FEHLER / TRACEBACK\n"
        )
        datei.write(
            "----------------------------------------\n\n"
        )

        datei.write(fehler_text)

    return (
        dateiname,
        fehler_id,
        os.path.abspath(dateipfad)
    )