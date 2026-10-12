import importlib.metadata
import re
import subprocess
import sys
import sysconfig
from pathlib import Path


PROJEKT_ORDNER = Path(__file__).resolve().parent
GEHEIMES_DATEI = PROJEKT_ORDNER / "geheimes.cp315-win_amd64.pyd"
REQUIREMENTS_DATEI = PROJEKT_ORDNER / "requirements.txt"
README_DATEI = PROJEKT_ORDNER / "README.md"
INSTALLATIONS_DATEI = PROJEKT_ORDNER / "Class Clash – Installation unter Windows.md"


def _hilfe_ausgeben(fehlermeldung: str):
    hilfe = (
        f"\n{fehlermeldung}\n"
        "\nHilfe:"
        "\n- Öffne die PDF-Versionen im Spielordner: 'README.pdf', 'More info.pdf' und 'Class Clash – Installation unter Windows.pdf'."
        "\n- Oder lese die Markdown-Dateien 'README.md' und 'Class Clash – Installation unter Windows.md'."
        "\n- Nutze zusätzlich den Menüpunkt 'Einstellungen > Wichtige Links' oder 'Einstellungen > Hilfe & Fehlerbehebung' im Spiel."
        "\n- Wichtig: Class Clash braucht CPython 3.15 (64-Bit), nicht eine andere Python-Version."
    )
    raise SystemExit(hilfe)


def pruefe_startvoraussetzungen():
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
