import sys
from pathlib import Path


def spiel_ordnung() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


def ressourcen_pfad(dateiname: str) -> Path:
    basis = Path(
        getattr(sys, "_MEIPASS", Path(__file__).resolve().parent)
    )
    return basis / dateiname
