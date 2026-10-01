import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk

BILDER_ORDNER = Path(__file__).parent / "bilder"

BILD_BREITE = 250
BILD_HOEHE = 333
SEITENBILD_BREITE = BILD_BREITE*2
SEITENBILD_HOEHE = BILD_HOEHE*2

_root = None
_fenster = {}
_bilder = {}
_seitenfenster = None
_seitenlabel = None
_seitenbild = None


def fenster_system_starten():
    global _root

    if _root is None:
        _root = tk.Tk()
        _root.withdraw()


def bild_anzeigen(name, x, y):
    fenster_system_starten()

    # Wenn der Bilderordner nicht existiert, nichts machen
    if not BILDER_ORDNER.exists():
        return

    if name in _fenster:
        _fenster[name].lift()
        return

    bild_pfad = BILDER_ORDNER / f"CC-{name}.png"

    if not bild_pfad.exists():
        print(f"Bild nicht gefunden: {bild_pfad}")
        return

    fenster = tk.Toplevel(_root)
    fenster.overrideredirect(True)
    fenster.attributes("-topmost", True)
    fenster.title(name)
    fenster.geometry(f"{BILD_BREITE}x{BILD_HOEHE}+{x}+{y}")

    # Bild laden und hochwertig skalieren
    bild = Image.open(bild_pfad)
    bild = bild.resize(
        (BILD_BREITE, BILD_HOEHE),
        Image.Resampling.LANCZOS
    )

    bild_tk = ImageTk.PhotoImage(bild)

    label = tk.Label(fenster, image=bild_tk)
    label.pack()

    _bilder[name] = bild_tk
    _fenster[name] = fenster

    fenster.protocol(
        "WM_DELETE_WINDOW",
        lambda: bild_schliessen(name)
    )

    _root.update()


def bild_rechts_anzeigen(name):
    global _seitenfenster, _seitenlabel, _seitenbild

    fenster_system_starten()

    bild_pfad = BILDER_ORDNER / f"CC-{name}.png"
    if not bild_pfad.exists():
        bild_rechts_schliessen()
        print(f"Bild nicht gefunden: {bild_pfad}")
        return

    with Image.open(bild_pfad) as quellbild:
        bild = quellbild.resize(
            (SEITENBILD_BREITE, SEITENBILD_HOEHE),
            Image.Resampling.LANCZOS
        )
    bild_tk = ImageTk.PhotoImage(bild)

    if _seitenfenster is None or not _seitenfenster.winfo_exists():
        _seitenfenster = tk.Toplevel(_root)
        _seitenfenster.overrideredirect(True)
        _seitenfenster.attributes("-topmost", True)
        _seitenlabel = tk.Label(_seitenfenster, image=bild_tk)
        _seitenlabel.pack()
        _seitenfenster.protocol(
            "WM_DELETE_WINDOW",
            bild_rechts_schliessen
        )
    else:
        _seitenlabel.configure(image=bild_tk)

    _seitenbild = bild_tk
    _seitenfenster.title(name)
    x = _seitenfenster.winfo_screenwidth() - BILD_BREITE - 12
    _seitenfenster.geometry(
        f"{BILD_BREITE}x{BILD_HOEHE}+{x}+20"
    )
    _seitenfenster.lift()
    _root.update()


def bild_rechts_schliessen():
    global _seitenfenster, _seitenlabel, _seitenbild

    if _seitenfenster is not None and _seitenfenster.winfo_exists():
        _seitenfenster.destroy()

    _seitenfenster = None
    _seitenlabel = None
    _seitenbild = None


def bild_schliessen(name):
    if name in _fenster:
        _fenster[name].destroy()
        del _fenster[name]
        del _bilder[name]


def alle_bilder_schliessen():
    for name in list(_fenster):
        bild_schliessen(name)