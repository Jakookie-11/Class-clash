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

PROJEKT_ORDNER = os.path.dirname(
    os.path.abspath(__file__)
)

UPDATE_PFAD = os.path.join(
    PROJEKT_ORDNER,
    UPDATE_ORDNER
)

ZIP_PFAD = os.path.join(
    PROJEKT_ORDNER,
    UPDATE_ZIP
)


# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def kurze_pause():
    time.sleep(0.7)


def laengere_pause():
    time.sleep(1.2)


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

            print(
                f"Warte auf Datei: {os.path.basename(pfad)}"
            )

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

        print(
            f"Warte auf Ordner: {os.path.basename(pfad)}"
        )

        time.sleep(0.5)

        ordner_loeschen(pfad)


# ============================================================
# UPDATE HERUNTERLADEN
# ============================================================

def update_herunterladen():

    print("[1/6] Update herunterladen")
    print()

    print("Suche nach Update...")
    print()

    github_antwort = urlopen(
        GITHUB_API,
        timeout=10
    )

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
        print()

        return False

    print("Update gefunden.")
    print()
    print("Lade Update herunter...")
    print()

    with urlopen(
        download_url,
        timeout=30
    ) as antwort:

        with open(
            ZIP_PFAD,
            "wb"
        ) as datei:

            while True:

                daten_block = antwort.read(8192)

                if not daten_block:
                    break

                datei.write(daten_block)

    print("Download abgeschlossen.")
    print()

    laengere_pause()

    return True


# ============================================================
# UPDATE ENTPACKEN
# ============================================================

def update_entpacken():

    print("[2/6] Update entpacken")
    print()

    if os.path.exists(UPDATE_PFAD):

        ordner_loeschen(
            UPDATE_PFAD
        )

    os.makedirs(
        UPDATE_PFAD
    )

    with zipfile.ZipFile(
        ZIP_PFAD,
        "r"
    ) as zip_datei:

        zip_datei.extractall(
            UPDATE_PFAD
        )

    print("Update entpackt.")
    print()

    laengere_pause()


# ============================================================
# SPIELSTÄNDE MIGRIEREN
# ============================================================

def daten_ergänzen(
    alte_daten,
    standard_daten
):

    if not isinstance(
        alte_daten,
        dict
    ):

        return alte_daten

    if not isinstance(
        standard_daten,
        dict
    ):

        return alte_daten

    for schlüssel, standard_wert in standard_daten.items():

        # ----------------------------------------------------
        # SCHLÜSSEL EXISTIERT BEREITS
        # ----------------------------------------------------

        if schlüssel in alte_daten:

            alter_wert = alte_daten[
                schlüssel
            ]

            # Beide Werte sind Dictionaries
            # → rekursiv überprüfen

            if (
                isinstance(
                    alter_wert,
                    dict
                )
                and
                isinstance(
                    standard_wert,
                    dict
                )
            ):

                daten_ergänzen(
                    alter_wert,
                    standard_wert
                )

        # ----------------------------------------------------
        # SCHLÜSSEL FEHLT
        # ----------------------------------------------------

        else:

            alte_daten[
                schlüssel
            ] = standard_wert

    return alte_daten


def spielstaende_migrieren():

    print("[3/6] Spielerdaten überprüfen")
    print()

    # --------------------------------------------------------
    # STANDARDDATEI DES UPDATES
    # --------------------------------------------------------

    standard_pfad = os.path.join(
        UPDATE_PFAD,
        "Class-clash-main",
        "standard.json"
    )

    if not os.path.exists(
        standard_pfad
    ):

        print(
            "Keine standard.json im Update gefunden."
        )

        print(
            "Spielstände werden nicht verändert."
        )

        print()

        return

    # --------------------------------------------------------
    # STANDARDDATEN LADEN
    # --------------------------------------------------------

    with open(
        standard_pfad,
        "r",
        encoding="utf-8"
    ) as datei:

        standard_daten = json.load(
            datei
        )

    # --------------------------------------------------------
    # SAVE-ORDNER
    # --------------------------------------------------------

    saves_pfad = os.path.join(
        PROJEKT_ORDNER,
        "saves"
    )

    if not os.path.exists(
        saves_pfad
    ):

        print(
            "Kein saves-Ordner gefunden."
        )

        print()

        return

    # --------------------------------------------------------
    # SPIELSTÄNDE DURCHGEHEN
    # --------------------------------------------------------

    anzahl = 0

    for dateiname in os.listdir(
        saves_pfad
    ):

        # Nur JSON-Dateien
        if not dateiname.endswith(
            ".json"
        ):

            continue

        # Diese Dateien sind KEINE Spielstände
        if dateiname in [
            "confic_setup.json",
            "passwoerter.json"
        ]:

            continue

        spielstand_pfad = os.path.join(
            saves_pfad,
            dateiname
        )

        # Nur Dateien
        if not os.path.isfile(
            spielstand_pfad
        ):

            continue

        print(
            f"  Überprüfe {dateiname}..."
        )

        # ----------------------------------------------------
        # SPIELSTAND LADEN
        # ----------------------------------------------------

        with open(
            spielstand_pfad,
            "r",
            encoding="utf-8"
        ) as datei:

            alte_daten = json.load(
                datei
            )

        # ----------------------------------------------------
        # DATEN ERGÄNZEN
        # ----------------------------------------------------

        daten_ergänzen(
            alte_daten,
            standard_daten
        )

        # ----------------------------------------------------
        # SPIELSTAND SPEICHERN
        # ----------------------------------------------------

        with open(
            spielstand_pfad,
            "w",
            encoding="utf-8"
        ) as datei:

            json.dump(
                alte_daten,
                datei,
                ensure_ascii=False,
                indent=4
            )

        print(
            f"  ✓ {dateiname}"
        )

        anzahl += 1

    print()

    if anzahl == 0:

        print(
            "Keine Spielstände gefunden."
        )

    else:

        print(
            f"{anzahl} Spielstand/Spielstände überprüft."
        )

    print()

    laengere_pause()


# ============================================================
# CONFIC MIGRATION
# ============================================================

def confic_daten_migrieren(
    alte_daten,
    neue_daten
):

    if not isinstance(
        alte_daten,
        dict
    ):

        return neue_daten

    if not isinstance(
        neue_daten,
        dict
    ):

        return alte_daten

    neue_config = {}

    for schlüssel, neuer_wert in neue_daten.items():

        # ----------------------------------------------------
        # SCHLÜSSEL EXISTIERT BEREITS
        # ----------------------------------------------------

        if schlüssel in alte_daten:

            alter_wert = alte_daten[
                schlüssel
            ]

            # Beide sind Dictionaries
            # → rekursiv migrieren

            if (
                isinstance(
                    alter_wert,
                    dict
                )
                and
                isinstance(
                    neuer_wert,
                    dict
                )
            ):

                neue_config[
                    schlüssel
                ] = confic_daten_migrieren(
                    alter_wert,
                    neuer_wert
                )

            # Alten Wert behalten
            else:

                neue_config[
                    schlüssel
                ] = alter_wert

        # ----------------------------------------------------
        # NEUER SCHLÜSSEL
        # ----------------------------------------------------

        else:

            neue_config[
                schlüssel
            ] = neuer_wert

    return neue_config


def confic_migrieren():

    print("  Konfiguration überprüfen...")

    neue_confic_pfad = os.path.join(
        UPDATE_PFAD,
        "Class-clash-main",
        "saves",
        "confic_setup.json"
    )

    alte_confic_pfad = os.path.join(
        PROJEKT_ORDNER,
        "saves",
        "confic_setup.json"
    )

    # --------------------------------------------------------
    # NEUE CONFIG PRÜFEN
    # --------------------------------------------------------

    if not os.path.exists(
        neue_confic_pfad
    ):

        print(
            "  ⚠ Keine neue confic_setup.json gefunden."
        )

        return

    # --------------------------------------------------------
    # ALTE CONFIG PRÜFEN
    # --------------------------------------------------------

    if not os.path.exists(
        alte_confic_pfad
    ):

        print(
            "  ⚠ Keine alte confic_setup.json gefunden."
        )

        return

    # --------------------------------------------------------
    # DATEIEN LADEN
    # --------------------------------------------------------

    with open(
        neue_confic_pfad,
        "r",
        encoding="utf-8"
    ) as datei:

        neue_daten = json.load(
            datei
        )

    with open(
        alte_confic_pfad,
        "r",
        encoding="utf-8"
    ) as datei:

        alte_daten = json.load(
            datei
        )

    # --------------------------------------------------------
    # MIGRIEREN
    # --------------------------------------------------------

    alte_daten = confic_daten_migrieren(
        alte_daten,
        neue_daten
    )

    # --------------------------------------------------------
    # SPEICHERN
    # --------------------------------------------------------

    with open(
        alte_confic_pfad,
        "w",
        encoding="utf-8"
    ) as datei:

        json.dump(
            alte_daten,
            datei,
            ensure_ascii=False,
            indent=4
        )

    print(
        "  ✓ Konfiguration aktualisiert."
    )

    laengere_pause()


# ============================================================
# UPDATE VORBEREITEN
# ============================================================

def update_vorbereiten():

    print("[4/6] Alte Update-Dateien vorbereiten")
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

        if os.path.isdir(
            pfad
        ):

            ordner_loeschen(
                pfad
            )

        elif os.path.isfile(
            pfad
        ):

            datei_loeschen_warten(
                pfad
            )

    print(
        "  ✓ Update vorbereitet."
    )

    print()

    laengere_pause()


# ============================================================
# ALTE DATEIEN LÖSCHEN
# ============================================================

def alte_dateien_loeschen():

    print("[5/6] Alte Programmdateien entfernen")
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

    for name in os.listdir(
        PROJEKT_ORDNER
    ):

        pfad = os.path.join(
            PROJEKT_ORDNER,
            name
        )

        if name in geschuetzte_dateien:
            continue

        if name in geschuetzte_ordner:
            continue

        # ----------------------------------------------------
        # ORDNER
        # ----------------------------------------------------

        if os.path.isdir(
            pfad
        ):

            if name == "__pycache__":

                ordner_loeschen(
                    pfad
                )

            continue

        # ----------------------------------------------------
        # DATEIEN
        # ----------------------------------------------------

        if os.path.isfile(
            pfad
        ):

            if name.endswith(
                ".py"
            ):

                datei_loeschen_warten(
                    pfad
                )

            elif name.endswith(
                ".txt"
            ):

                datei_loeschen_warten(
                    pfad
                )

            elif name.endswith(
                ".json"
            ):

                datei_loeschen_warten(
                    pfad
                )

            elif name.endswith(
                ".pyd"
            ):

                datei_loeschen_warten(
                    pfad
                )

    print(
        "  ✓ Alte Dateien entfernt."
    )

    print()

    laengere_pause()


# ============================================================
# UPDATE INSTALLIEREN
# ============================================================

def update_installieren():

    print("Installiere neue Version...")
    print()

    hauptordner = os.path.join(
        UPDATE_PFAD,
        "Class-clash-main"
    )

    for name in os.listdir(
        hauptordner
    ):

        quelle = os.path.join(
            hauptordner,
            name
        )

        ziel = os.path.join(
            PROJEKT_ORDNER,
            name
        )

        # ----------------------------------------------------
        # ORDNER
        # ----------------------------------------------------

        if os.path.isdir(
            quelle
        ):

            if os.path.exists(
                ziel
            ):

                ordner_loeschen(
                    ziel
                )

            shutil.copytree(
                quelle,
                ziel
            )

        # ----------------------------------------------------
        # DATEIEN
        # ----------------------------------------------------

        else:

            shutil.copy2(
                quelle,
                ziel
            )

    print(
        "  ✓ Neue Version installiert."
    )

    print()

    laengere_pause()


# ============================================================
# AUFRÄUMEN
# ============================================================

def aufraeumen():

    print("[6/6] Aufräumen")
    print()

    if os.path.exists(
        ZIP_PFAD
    ):

        datei_loeschen_warten(
            ZIP_PFAD
        )

    if os.path.exists(
        UPDATE_PFAD
    ):

        ordner_loeschen(
            UPDATE_PFAD
        )

    print(
        "  ✓ Temporäre Dateien entfernt."
    )

    print()

    laengere_pause()


# ============================================================
# MAIN
# ============================================================

def main():

    print()

    print(
        "╔══════════════════════════════════════════════════╗"
    )

    print(
        "║                 CLASS CLASH                     ║"
    )

    print(
        "║                  UPDATER                        ║"
    )

    print(
        "╚══════════════════════════════════════════════════╝"
    )

    print()

    try:

        # ----------------------------------------------------
        # UPDATE HERUNTERLADEN
        # ----------------------------------------------------

        if not update_herunterladen():

            input(
                "ENTER zum Beenden..."
            )

            return

        # ----------------------------------------------------
        # UPDATE ENTPACKEN
        # ----------------------------------------------------

        update_entpacken()

        # ----------------------------------------------------
        # SPIELERDATEN
        # ----------------------------------------------------

        print("[3/6] Spielerdaten")
        print()

        confic_migrieren()

        spielstaende_migrieren()

        # ----------------------------------------------------
        # UPDATE VORBEREITEN
        # ----------------------------------------------------

        update_vorbereiten()

        # ----------------------------------------------------
        # ALTE DATEIEN
        # ----------------------------------------------------

        alte_dateien_loeschen()

        # ----------------------------------------------------
        # NEUE DATEIEN
        # ----------------------------------------------------

        update_installieren()

        # ----------------------------------------------------
        # AUFRÄUMEN
        # ----------------------------------------------------

        aufraeumen()

        # ----------------------------------------------------
        # FERTIG
        # ----------------------------------------------------

        print()

        print(
            "════════════════════════════════════════════════════"
        )

        print(
            "              UPDATE ERFOLGREICH"
        )

        print(
            "════════════════════════════════════════════════════"
        )

        print()

        print(
            "Class Clash wurde aktualisiert."
        )

        print(
            "Du kannst Class Clash jetzt erneut starten."
        )

        print()

        time.sleep(2)

    except Exception as fehler:

        print()

        print(
            "════════════════════════════════════════════════════"
        )

        print(
            "                 UPDATE FEHLER"
        )

        print(
            "════════════════════════════════════════════════════"
        )

        print()

        print(
            f"Fehler: {fehler}"
        )

        print()

        print(
            "Das Update konnte nicht vollständig installiert werden."
        )

        print()

        input(
            "ENTER zum Beenden..."
        )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    main()