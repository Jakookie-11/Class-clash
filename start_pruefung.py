import importlib.metadata
import re
import subprocess
import sys
import sysconfig
from pathlib import Path
import os
import webbrowser
import confic
from pfade import ressourcen_pfad


PROJEKT_ORDNER = Path(__file__).resolve().parent
GEHEIMES_DATEI = PROJEKT_ORDNER / "geheimes.cp315-win_amd64.pyd"
REQUIREMENTS_DATEI = PROJEKT_ORDNER / "requirements.txt"
README_DATEI = PROJEKT_ORDNER / "README.md"
INSTALLATIONS_DATEI = PROJEKT_ORDNER / "Class Clash - Installation unter Windows.md"


def _hilfe_ausgeben(fehlermeldung: str):
    hilfe = (
        f"\n{fehlermeldung}\n"
        "\nHilfe:"
        "\n- Öffne die mitgelieferten PDF-Hilfen: 'README.pdf', 'More info.pdf' und 'Class Clash - Installation unter Windows.pdf'."
        "\n- Oder lies die Markdown-Dateien 'README.md' und 'Class Clash - Installation unter Windows.md'."
        "\n- Nutze zusätzlich den Menüpunkt 'Einstellungen > Wichtige Links' oder 'Einstellungen > Hilfe & Fehlerbehebung' im Spiel."
        "\n- Wichtig: Class Clash braucht CPython 3.15 (64-Bit), nicht eine andere Python-Version(CPython ist aber in der neuen Python version enthalten)."
    )
    raise SystemExit(hilfe)


def pruefe_startvoraussetzungen():
    if getattr(sys, "frozen", False):
        return

    extension_suffix = sysconfig.get_config_var("EXT_SUFFIX")
    if (
        sys.implementation.name != "cpython"
        or not extension_suffix
        or not GEHEIMES_DATEI.name.endswith(extension_suffix)
    ):
        _hilfe_ausgeben(
            "Class Clash benötigt CPython 3.15 (64-Bit) für "
            "geheimes.cp315-win_amd64.pyd. "
            f"Verwendet wird Python {sys.version.split()[0]}."
        )

    if not GEHEIMES_DATEI.is_file():
        _hilfe_ausgeben(f"Die benötigte Datei fehlt: {GEHEIMES_DATEI.name}")

    if not REQUIREMENTS_DATEI.is_file():
        _hilfe_ausgeben(f"Die benötigte Datei fehlt: {REQUIREMENTS_DATEI.name}")

    fehlende_pakete = []
    alle_anforderungen_einfach = True
    for zeile in REQUIREMENTS_DATEI.read_text(encoding="utf-8").splitlines():
        anforderung = zeile.partition("#")[0].strip()
        if not anforderung:
            continue

        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", anforderung):
            alle_anforderungen_einfach = False
            continue

        try:
            importlib.metadata.distribution(anforderung)
        except importlib.metadata.PackageNotFoundError:
            fehlende_pakete.append(anforderung)

    if fehlende_pakete or not alle_anforderungen_einfach:
        print("Installiere die benötigten Pakete aus requirements.txt ...")
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "-r",
                str(REQUIREMENTS_DATEI),
            ],
            cwd=PROJEKT_ORDNER,
            check=True,
        )


def hilfe_und_fehlerbehebung(spieler_name):

    while True:
        os.system(confic.terminal_clear)

        print("══════════════════════════════")
        print("   Hilfe & Fehlerbehebung")
        print("══════════════════════════════")
        print()
        print("[1] Python 3.15 installieren / pruefen")
        print("[2] Falsche Python-Version beheben")
        print("[3] PDF-Hilfen oeffnen")
        print("[4] Crash-Logs anzeigen")
        print("[5] GitHub Issue melden")
        print("[0] Zurueck")
        print()

        wahl = input("Wahl? ")

        if wahl == "0":
            return 1

        if wahl == "1":
            os.system(confic.terminal_clear)
            print("Python 3.15 (64-Bit) erforderlich")
            print("=================================")
            print()
            print("1. Python 3.15 64-Bit installieren:")
            print("   https://www.python.org/downloads/release/python-3150/")
            print()
            print("2. Beim Installer 'Add python.exe to PATH' aktivieren.")
            print("3. Danach in PowerShell prüfen:")
            print("   py -3.15 --version")
            print("4. Wenn die Version 3.15.x angezeigt wird, geht es weiter.")
            print()
            print("[Enter] Zurueck zum Hilfe-Menue / [0] Beenden")
            eingabe = input("Wahl? ")
            if eingabe == "0":
                return 1
            continue

        if wahl == "2":
            os.system(confic.terminal_clear)
            print("Falsche Python-Version beheben")
            print("=============================")
            print()
            print("Wenn Class Clash meldet, dass Python 3.15 (64-Bit) erforderlich ist, dann:")
            print("- Python 3.15 64-Bit neu oder erneut installieren")
            print("- Pfad prüfen und PowerShell neu starten")
            print("- Danach genau so starten:")
            print("  py -3.15 -m main.py")
            print()
            print("[Enter] Zurueck zum Hilfe-Menue / [0] Beenden")
            eingabe = input("Wahl? ")
            if eingabe == "0":
                return 1
            continue

        if wahl == "3":
            os.system(confic.terminal_clear)
            dateien = [
                "README.pdf",
                "More info.pdf",
                "Class Clash - Installation unter Windows.pdf",
                "README.md",
                "More info.md",
                "Class Clash - Installation unter Windows.md",
            ]

            print("PDF-Hilfen werden geöffnet...")
            for datei in dateien:
                dateipfad = ressourcen_pfad(datei)
                if dateipfad.exists():
                    try:
                        os.startfile(dateipfad)
                    except Exception:
                        pass
            print()
            print("[Enter] Zurueck zum Hilfe-Menue / [0] Beenden")
            eingabe = input("Wahl? ")
            if eingabe == "0":
                return 1
            continue

        if wahl == "4":
            os.system(confic.terminal_clear)
            ordner = os.path.join(os.getcwd(), "crash_logs")
            os.makedirs(ordner, exist_ok=True)
            print("Crash-Logs Ordner wird geöffnet:")
            print(ordner)
            try:
                os.startfile(ordner)
            except Exception:
                pass
            print()
            print("[Enter] Zurueck zum Hilfe-Menue / [0] Beenden")
            eingabe = input("Wahl? ")
            if eingabe == "0":
                return 1
            continue

        if wahl == "5":
            os.system(confic.terminal_clear)
            url = "https://github.com/Jakookie-11/Class-clash/issues"
            print("GitHub Issues werden geöffnet:")
            print(url)
            try:
                webbrowser.open(url, new=2)
            except Exception:
                pass
            print()
            print("[Enter] Zurueck zum Hilfe-Menue / [0] Beenden")
            eingabe = input("Wahl? ")
            if eingabe == "0":
                return 1
            continue