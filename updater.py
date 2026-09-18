import os
import sys
import time
import shutil
import zipfile
import json
from urllib.request import urlopen
import subprocess


# ============================================================
# EINSTELLUNGEN
# ============================================================

GITHUB_API = "https://api.github.com/repos/Jakookie-11/Class-clash/releases/latest"

UPDATE_ORDNER = "update"
UPDATE_ZIP = "update.zip"


# ============================================================
# PROJEKTORDNER ERMITTELN
# ============================================================

PROJEKT_ORDNER = os.path.dirname(os.path.abspath(__file__))

UPDATE_PFAD = os.path.join(PROJEKT_ORDNER, UPDATE_ORDNER)
ZIP_PFAD = os.path.join(PROJEKT_ORDNER, UPDATE_ZIP)


# ============================================================
# DATEI LÖSCHEN
# ============================================================

def datei_loeschen_warten(pfad):

    while True:

        try:
            if os.path.exists(pfad):
                os.remove(pfad)

            break

        except PermissionError:
            print(f"Warte auf Datei: {os.path.basename(pfad)}")
            time.sleep(0.5)


# ============================================================
# ORDNER LÖSCHEN
# ============================================================

def ordner_loeschen(pfad):

    if not os.path.exists(pfad):
        return

    try:
        shutil.rmtree(pfad)

    except PermissionError:
        print(f"Warte auf Ordner: {os.path.basename(pfad)}")
        time.sleep(0.5)

        ordner_loeschen(pfad)


# ============================================================
# UPDATE HERUNTERLADEN
# ============================================================

def update_herunterladen():

    print("Suche nach Update...")
    print()

    github_antwort = urlopen(GITHUB_API, timeout=10)

    daten = json.loads(
        github_antwort.read().decode("utf-8")
    )

    download_url = None

    for asset in daten["assets"]:

        if asset["name"] == "update.zip":
            download_url = asset["browser_download_url"]
            break

    if download_url is None:
        print("Keine update.zip gefunden.")
        return False

    print("Update gefunden.")
    print("Lade Update herunter...")
    print()

    with urlopen(download_url, timeout=30) as antwort:

        with open(ZIP_PFAD, "wb") as datei:

            while True:

                daten_block = antwort.read(8192)

                if not daten_block:
                    break

                datei.write(daten_block)

    print("Download abgeschlossen.")
    print()

    return True


# ============================================================
# UPDATE ENTPACKEN
# ============================================================

def update_entpacken():

    print("Entpacke Update...")
    print()

    if os.path.exists(UPDATE_PFAD):
        ordner_loeschen(UPDATE_PFAD)

    os.makedirs(UPDATE_PFAD)

    with zipfile.ZipFile(ZIP_PFAD, "r") as zip_datei:

        zip_datei.extractall(UPDATE_PFAD)

    print("Update entpackt.")
    print()


# ============================================================
# UNNÖTIGE DATEIEN AUS UPDATE ENTFERNEN
# ============================================================

def update_vorbereiten():

    print("Bereite Update vor...")
    print()

    hauptordner = os.path.join(
        UPDATE_PFAD,
        "Class-clash-main"
    )

    nicht_uebernehmen = [
        "updater.py",
        ".gitignore",
        "saves",
        ".vscode",
        ".git"
    ]

    for name in nicht_uebernehmen:

        pfad = os.path.join(
            hauptordner,
            name
        )

        if os.path.isdir(pfad):
            ordner_loeschen(pfad)

        elif os.path.isfile(pfad):
            datei_loeschen_warten(pfad)

    print("Update vorbereitet.")
    print()


# ============================================================
# ALTE DATEIEN LÖSCHEN
# ============================================================

def alte_dateien_loeschen():

    print("Entferne alte Dateien...")
    print()

    geschuetzte_dateien = [
        "updater.py",
        "update.zip"
    ]

    geschuetzte_ordner = [
        "saves",
        ".git",
        ".vscode",
        ".venv",
        "update"
    ]

    for name in os.listdir(PROJEKT_ORDNER):

        pfad = os.path.join(PROJEKT_ORDNER, name)

        if name in geschuetzte_dateien:
            continue

        if name in geschuetzte_ordner:
            continue

        # Ordner
        if os.path.isdir(pfad):

            if name == "__pycache__":
                ordner_loeschen(pfad)

            continue

        # Dateien
        if os.path.isfile(pfad):

            # Diese Dateitypen werden vom Update ersetzt
            if name.endswith(".py"):
                datei_loeschen_warten(pfad)

            elif name.endswith(".txt"):
                datei_loeschen_warten(pfad)

            elif name.endswith(".json"):
                datei_loeschen_warten(pfad)

            elif name.endswith(".pyd"):
                datei_loeschen_warten(pfad)

    print("Alte Dateien entfernt.")
    print()


# ============================================================
# UPDATE DATEIEN KOPIEREN
# ============================================================

def update_installieren():

    print("Installiere Update...")
    print()

    # Der eigentliche Inhalt befindet sich in
    # "Class-clash-main"

    hauptordner = os.path.join(
        UPDATE_PFAD,
        "Class-clash-main"
    )

    for name in os.listdir(hauptordner):

        quelle = os.path.join(
            hauptordner,
            name
        )

        ziel = os.path.join(
            PROJEKT_ORDNER,
            name
        )

        if os.path.isdir(quelle):

            if os.path.exists(ziel):
                ordner_loeschen(ziel)

            shutil.copytree(
                quelle,
                ziel
            )

        else:

            shutil.copy2(
                quelle,
                ziel
            )

    print("Update installiert.")
    print()


# ============================================================
# UPDATE ORDNER AUFRÄUMEN
# ============================================================

def aufraeumen():

    print("Räume auf...")
    print()

    # update.zip löschen
    if os.path.exists(ZIP_PFAD):
        datei_loeschen_warten(ZIP_PFAD)

    # update-Ordner löschen
    if os.path.exists(UPDATE_PFAD):
        ordner_loeschen(UPDATE_PFAD)

    print("Aufräumen abgeschlossen.")
    print()


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║                 CLASS CLASH                      ║")
    print("║                  UPDATER                         ║")
    print("╚══════════════════════════════════════════════════╝")
    print()

    try:

        # ----------------------------------------------------
        # UPDATE HERUNTERLADEN
        # ----------------------------------------------------

        if not update_herunterladen():
            input("ENTER zum Beenden...")
            return

        # ----------------------------------------------------
        # ENTPACKEN
        # ----------------------------------------------------

        update_entpacken()

        # ----------------------------------------------------
        # UPDATE VORBEREITEN
        # ----------------------------------------------------

        update_vorbereiten()

        # ----------------------------------------------------
        # ALTE DATEIEN LÖSCHEN
        # ----------------------------------------------------

        alte_dateien_loeschen()

        # ----------------------------------------------------
        # NEUE DATEIEN INSTALLIEREN
        # ----------------------------------------------------

        update_installieren()

        # ----------------------------------------------------
        # AUFRÄUMEN
        # ----------------------------------------------------

        aufraeumen()

        print()
        print("════════════════════════════════════════════════════")
        print("Update erfolgreich installiert!")
        print("════════════════════════════════════════════════════")
        print()

        time.sleep(2)

        print("Class Clash wurde beendet.")
        print("Du kannst Class Clash jetzt manuell starten.")
        print()

        time.sleep(2)


    except Exception as fehler:

        print()
        print("════════════════════════════════════════════════════")
        print("FEHLER BEIM UPDATE")
        print("════════════════════════════════════════════════════")
        print()

        print(fehler)
        print()

        print("Das Update konnte nicht vollständig installiert werden.")
        print()

        input("ENTER zum Beenden...")


if __name__ == "__main__":
    main()