import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk

BILDER_ORDNER = Path(__file__).parent / "bilder"

BILD_BREITE = 250
BILD_HOEHE = 333

_root = None
_fenster = {}
_bilder = {}


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


def bild_schliessen(name):
    if name in _fenster:
        _fenster[name].destroy()
        del _fenster[name]
        del _bilder[name]


def alle_bilder_schliessen():
    for name in list(_fenster):
        bild_schliessen(name)