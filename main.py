import os
import time
import confic
import sys

import funktions
import menues
import charakter_bip
import shop
import neues_spiel
import speichern
import begin
import einstellungen
import subprocess
import crash_handler


SCHWARZ  = "\033[30m"
ROT      = "\033[31m"
GRUEN    = "\033[32m"
GELB     = "\033[33m"
BLAU     = "\033[34m"
MAGENTA  = "\033[35m"
CYAN     = "\033[36m"
WEISS    = "\033[37m"

RESET    = "\033[0m"


spieler = begin.begin()

try:

    if spieler == "break":

        updater = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "updater.py"
        )

        subprocess.Popen(
            [sys.executable, updater],
            cwd=os.path.dirname(os.path.abspath(__file__))
        )

        sys.exit()

    #-----Hauptmenü-----#

    hauptmenue = True

    while hauptmenue == True:
        wahl = funktions.menue(menues.hauptmenue, spieler)
        os.system(confic.terminal_clear)

        if wahl == 1:
            while True:  
                is_brake_neues_spiel = neues_spiel.neues_spiel(spieler)

                if is_brake_neues_spiel == 1:
                    os.system(confic.terminal_clear)
                    break

        elif wahl == 2:
            while True:
                is_brake_charakter_bib = charakter_bip.charakter_bip(spieler)

                if is_brake_charakter_bib == 1:
                    os.system(confic.terminal_clear)
                    break
                    

        elif wahl == 3:
            while True:
                is_brake_einstellungen = einstellungen.einstellungen(spieler)

                if is_brake_einstellungen == 1:
                    os.system(confic.terminal_clear)
                    break

        elif wahl == 4:
            while True:
                is_brake_shop = shop.shop(spieler)

                if is_brake_shop == 1:
                    os.system(confic.terminal_clear)
                    break

        else:
            speichern.spiel_speichern(spieler)
            print("Spiel wird gespeichert...")
            time.sleep(1)
            os.system(confic.terminal_clear)
            print()
            print("BYE")
            print()
            time.sleep(4)
            os.system(confic.terminal_clear)
            hauptmenue = False 


except Exception:

    # Spielstand sichern
    speichern.spiel_speichern(spieler)

    # Crash-Report erstellen
    dateiname, fehler_id, crash_pfad = crash_handler.crash_speichern(
        spieler
    )

    # Fehlermeldung anzeigen
    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║                 CLASS CLASH                      ║")
    print("║              FEHLER AUFGETRETEN                  ║")
    print("╚══════════════════════════════════════════════════╝")
    print()

    print("Leider ist ein unerwarteter Fehler aufgetreten.")
    print()

    print("Dein Spielstand wurde automatisch gespeichert.")
    print("Ein Fehlerbericht wurde erstellt.")
    print()

    print("Bitte sende den Fehlerbericht an den Entwickler,")
    print("damit der Fehler untersucht und behoben werden kann.")
    print()

    print(f"Fehler-ID: {fehler_id}")
    print()

    print("Fehlerbericht:")
    print(crash_pfad)
    print()

    print("Bitte sende genau diese Datei an den Entwickler.")
    print()

    print("Class Clash wird jetzt beendet.")
    print()

    input("Drücke ENTER zum Beenden...")

    print()
    print("Falls es dich interessiert, dass ist der fehler: ")
    print()

    # Ursprünglichen Fehler weiterhin anzeigen
    raise    
