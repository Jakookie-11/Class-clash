import start_pruefung

try:
    start_pruefung.pruefe_startvoraussetzungen()
except SystemExit as err:
    print()
    print("══════════════════════════════════════════════════")
    print("            CLASS CLASH - STARTFEHLER")
    print("══════════════════════════════════════════════════")
    print()
    print(str(err))
    print()
    print("[1] Hilfe & Fehlerbehebung anzeigen")
    print("[2] Nur beenden")
    print()
    wahl = input("Wahl? ")
    if wahl == "1":
        try:
            start_pruefung.hilfe_und_fehlerbehebung("Crash")
        except Exception:
            pass

import os
import time
import sys
import subprocess
import webbrowser

from pfade import spiel_ordnung

os.chdir(spiel_ordnung())

import confic
import funktions
import menues
import charakter_bip
import shop
import spiel_starten
import speichern
import begin
import crash_handler
import herausforderungen
import sound
import einstellungen

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

        if getattr(sys, "frozen", False):
            print("EXE-Updates werden nicht automatisch installiert.")
            print("Bitte lade die aktuelle Windows-Version von GitHub herunter:")
            print("https://github.com/Jakookie-11/Class-clash/releases")
            webbrowser.open(
                "https://github.com/Jakookie-11/Class-clash/releases",
                new=2,
            )
            input("Enter zum Beenden...")
            sys.exit()

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

    confic.start_zeit = int(time.time())

    while hauptmenue == True:

        sound.musik_abspielen("test.mp3",lautstaerke=0.4)
        
        wahl = funktions.menue(menues.hauptmenue, spieler)
        os.system(confic.terminal_clear)

        if wahl == 1:
            sound.musik_stoppen()
            while True:  
                is_brake_spiel_starten = spiel_starten.spiel_starten(spieler)

                if is_brake_spiel_starten == 1:
                    os.system(confic.terminal_clear)
                    break

        elif wahl == 2:
            sound.musik_stoppen()
            while True:
                is_brake_charakter_bib = charakter_bip.charakter_bip(spieler)

                if is_brake_charakter_bib == 1:
                    os.system(confic.terminal_clear)
                    break
                    

        elif wahl == 3:
            sound.musik_stoppen()
            while True:
                is_brake_einstellungen = einstellungen.einstellungen(spieler)

                if is_brake_einstellungen == 1:
                    os.system(confic.terminal_clear)
                    break

        elif wahl == 4:
            sound.musik_stoppen()
            while True:
                is_brake_shop = shop.shop(spieler)

                if is_brake_shop == 1:
                    os.system(confic.terminal_clear)
                    break

        elif wahl == 5:
            sound.musik_stoppen()
            herausforderungen.herausforderungen(spieler)

        else:
            sound.musik_stoppen()
            sound.musik_einmal_abspielen("shutdown.mp3")
            speichern.spiel_speichern(spieler)
            print("Spiel wird gespeichert...")
            time.sleep(3)
            os.system(confic.terminal_clear)
            print()
            print("BYE")
            print()
            time.sleep(13)
            sound.musik_stoppen()
            os.system(confic.terminal_clear)
            hauptmenue = False 


except Exception:

    # Spielstand sichern
    spielstand_gespeichert = True
    try:
        speichern.spiel_speichern(spieler)
    except OSError as speicher_fehler:
        spielstand_gespeichert = False
        print(f"Spielstand konnte nicht gespeichert werden: {speicher_fehler}")

    # Crash-Report erstellen
    dateiname, fehler_id, crash_pfad = crash_handler.crash_speichern(
        spieler
    )

    sound.musik_einmal_abspielen("emergency-alarm.mp3", lautstaerke=1.5)
    # Fehlermeldung anzeigen
    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║                 CLASS CLASH                      ║")
    print("║              FEHLER AUFGETRETEN                  ║")
    print("╚══════════════════════════════════════════════════╝")
    print()

    print("Leider ist ein unerwarteter Fehler aufgetreten.")
    print()
    print("Das Spiel ist nicht absichtlich beendet worden, sondern hat einen internen Fehler erkannt.")
    print("Ein Fehlerbericht wurde erstellt, damit der Fehler nachvollziehbar bleibt.")
    print("Wenn du hilfe brauchst, kannst du die Hilfe & Fehlerbehebung direkt hier öffnen.")
    print()

    if spielstand_gespeichert:
        print("Dein Spielstand wurde automatisch gespeichert.")
    else:
        print("Der Spielstand konnte nicht automatisch gespeichert werden.")
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

    print("[1] Hilfe & Fehlerbehebung anzeigen")
    print("[2] Nur beenden")
    print()
    wahl = input("Wahl? ")
    if wahl == "1":
        try:
            start_pruefung.hilfe_und_fehlerbehebung("Crash")
        except Exception:
            pass

    print()
    print("Class Clash wird jetzt beendet.")
    print()

    input("Drücke ENTER zum Beenden...")

    print()
    print("Falls es dich interessiert, hier ist der Fehler-Text:")
    print()

    # Ursprünglichen Fehler weiterhin anzeigen
    raise    
