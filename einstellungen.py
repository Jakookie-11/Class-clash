import os
import sys
import time
import webbrowser
import bcrypt
import json

import confic
from pfade import ressourcen_pfad

import menues
import funktions
import credits
import speichern
import sound
import start_pruefung


SCHWARZ  = "\033[30m"
ROT      = "\033[31m"
GRUEN    = "\033[32m"
GELB     = "\033[33m"
BLAU     = "\033[34m"
MAGENTA  = "\033[35m"
CYAN     = "\033[36m"
WEISS    = "\033[37m"

RESET    = "\033[0m"


def einstellungen(spieler_name):

    while True:

        os.system(confic.terminal_clear)

        wahl = funktions.menue(menues.einstellungen_menue, spieler_name)

        if wahl == 1:
            os.system(confic.terminal_clear)

            is_breake_profil_einstellungen = profil_enstellungen(spieler_name)

            if is_breake_profil_einstellungen == 1:
                continue

        elif wahl == 2:
            os.system(confic.terminal_clear)

            is_breake_audio = audio(spieler_name)

            if is_breake_audio == 1:
                continue

        elif wahl == 3:
            os.system(confic.terminal_clear)

            is_break_credits = credits.credits()

            if is_break_credits == 1:
                continue

        elif wahl == 4:
            os.system(confic.terminal_clear)

            wichtige_links_zeigen()

        elif wahl == 5:
            os.system(confic.terminal_clear)

            start_pruefung.hilfe_und_fehlerbehebung(spieler_name)

        else:
            speichern.spiel_speichern(spieler_name)
            return 1




def passwort_art_aendern():

    while True:
        os.system(confic.terminal_clear)

        print("Moeglichkeiten:")
        print("[1] sternchen")
        print("[2] unsichtbar")
        print("[3] sichtbar")
        print("[0] zurueck")
        print()
        wahl = funktions.ganzzahl_einlesen("wahl? ", 0, 3)

        if wahl == 0:
            return 1

        if wahl == 1:
            confic.passwort_art = "sternchen"
            speichern.confic_setup_speichern()

            os.system(confic.terminal_clear)
            print()
            print(f"Passwort_art wurde geändert zu: {confic.passwort_art}")
            print()
            input("Enter...")

        elif wahl == 2:
            confic.passwort_art = "unsichtbar"
            speichern.confic_setup_speichern()

            os.system(confic.terminal_clear)
            print()
            print(f"Passwort_art wurde geändert zu: {confic.passwort_art}")
            print()
            input("Enter...")

        elif wahl == 3:
            confic.passwort_art = "sichtbar"
            speichern.confic_setup_speichern()

            os.system(confic.terminal_clear)
            print()
            print(f"Passwort_art wurde geändert zu: {confic.passwort_art}")
            print()
            input("Enter...")

        continue         



def profil_enstellungen(spieler_name):

    while True:

        os.system(confic.terminal_clear)

        wahl = funktions.menue(menues.profil_menue, spieler_name)

        if wahl == 1:
            is_breake_passwort_aendern = passwort_aendern(spieler_name)

            if is_breake_passwort_aendern == 1:
                continue

        elif wahl == 2:
            profil_daten_zeigen(spieler_name)

        elif wahl == 3:
            is_breake_profil_zuruecksetzen = profil_zuruecksetzen(spieler_name)

            if is_breake_profil_zuruecksetzen == 1:
                continue

        elif wahl == 4:
            is_breake_profil_loeschen = profil_loeschen(spieler_name)

            if is_breake_profil_loeschen == 1:
                continue

        elif wahl == 5:
            is_breake_passwort_art_aendern = passwort_art_aendern()
            
            if is_breake_passwort_art_aendern == 1:
                continue

        else:
            return 1




def passwort_aendern(spieler_name):

    while True:

        os.system(confic.terminal_clear)

        print("Passwort aendern")
        print("================")
        print()

        altes_passwort = input("Altes Passwort: ")

        if bcrypt.checkpw(
            altes_passwort.encode("utf-8"),
            confic.passwoerter[spieler_name].encode("utf-8")
            ):
            print()
            print("Passwort korrekt")
            time.sleep(2)
            funktions.zeilen_loeschen(3)

            while True:

                while True:

                    neues_passwort = input("Neues Passwort: ")

                    if neues_passwort == "":
                        print()
                        print("Passwort darf nicht leer sein")
                        time.sleep(2)
                        funktions.zeilen_loeschen(3)

                    elif len(neues_passwort) < 6:
                        print()
                        print("Passwort muss mindestens 6 Zeichen lang sein")
                        time.sleep(2)
                        funktions.zeilen_loeschen(3)

                    else:
                        break


                funktions.zeilen_loeschen(1)
                neues_passwort_wiederholen = input("Neues Passwort wiederholen: ")

                if neues_passwort == neues_passwort_wiederholen:

                    bestätigung = input("Bist du sicher, dass du dein Passwort aendern willst? (ja/nein) ")

                    if bestätigung == "ja":

                        bestätigung_2 = input("schreibe: ich bin mir sicher, dass ich mein Passwort aendern moechte :   ")

                        if bestätigung_2 == "ich bin mir sicher, dass ich mein Passwort aendern moechte":

                            neues_passwort_hash = bcrypt.hashpw(
                                neues_passwort.encode("utf-8"),
                                bcrypt.gensalt()
                            )

                            #---Passwort in saves/passwoerter.json speichern---#
                            confic.passwoerter[spieler_name] = neues_passwort_hash.decode("utf-8")

                            datei = open("saves/passwoerter.json", "w")

                            daten = {
                                "passwoerter": confic.passwoerter
                            }

                            json.dump(daten, datei)

                            datei.close()

                            print()
                            print("Passwort erfolgreich geaendert")
                            time.sleep(2)
                            return 1

                        else:
                            print()
                            print("Passwort aendern abgebrochen")
                            time.sleep(2)
                            return 1

                    else:
                        print()
                        print("Passwort aendern abgebrochen")
                        time.sleep(2)
                        return 1
                else:
                    print()
                    print("Passwoerter stimmen nicht ueberein")
                    time.sleep(2)
                    return 1




def profil_daten_zeigen(spieler_name):

    speichern.spiel_speichern(spieler_name)  # Speichern, um sicherzustellen, dass die Daten aktuell sind

    sekunden = confic.time_played_in_seconds

    stunden, rest = divmod(sekunden, 3600)
    minuten, sekunden = divmod(rest, 60)


    datei = f"saves/{spieler_name}.json"

    #---Erstellungsdatum holen---#
    if os.path.exists(datei):
        alte_datei = open(datei, "r")
        alte_daten = json.load(alte_datei)
        alte_datei.close()

        erstellungsdatum = alte_daten["Erstellungsdatum"]

    os.system(confic.terminal_clear)

    print("Profil Daten")
    print("============")
    print()

    print(f"Spielername       : {spieler_name}")
    print(f"Passwort          : {confic.passwoerter[spieler_name]}")
    print(f"Erstellungsdatum  : {erstellungsdatum}")
    print(f"Time played       : {stunden:02}:{minuten:02}:{sekunden:02}")
    print(f"Gewonnene Kaempfe : {confic.gewonnene_kaempfe}")
    print()
    input("fertig? ")
    os.system(confic.terminal_clear)




def profil_zuruecksetzen(spieler_name):

    os.system(confic.terminal_clear)

    print("Profil Zuruecksetzen")
    print("===================")
    print()
    print(f"{ROT}Achtung: Dein Profil wird auf den Standard zurueckgesetzt!")
    print("Alle deine Fortschritte gehen verloren!(Gespielte Zeit bleibt erhalten)")
    print("Dein Spielername, Erstellungsdatum bleiben erhalten!")
    print("Du kannst dies nicht rueckgaengig machen!")
    print(f"Du kannst dich danach wieder mit deinem alten Spielername und Passwort anmelden!{RESET}")
    print()

    bestätigung = input("Bist du sicher, dass du dein Profil zuruecksetzen willst? (ja/nein) ")
    print()

    if bestätigung == "ja":

        sound.sound_abspielen("invalid-login-or-password.mp3", lautstaerke=2)
        bestätigung_2 = input("schreibe: ich bin mir sicher, dass ich mein Profil zuruecksetzen moechte :   ")

        if bestätigung_2 == "ich bin mir sicher, dass ich mein Profil zuruecksetzen moechte":

            #---Wichtige Daten holen---#
            datei = f"saves/{spieler_name}.json"
            datei = open(datei, "r")
            alte_daten_spieler = json.load(datei)

            alte_daten_spielername = alte_daten_spieler["spieler_name"]
            altes_daten_erstellungsdatum = alte_daten_spieler["Erstellungsdatum"]
            altes_daten_letztes_speichern = alte_daten_spieler["Letztes_Speichern"]
            altes_daten_time_played_in_seconds = alte_daten_spieler["time_played_in_seconds"]

            datei.close()

            #---Generelle Daten holen---#
            datei = open(ressourcen_pfad("standard.json"), "r")
            generelle_daten = json.load(datei)

            generelle_daten_ressourcen = generelle_daten["ressourcen"]
            generelle_daten_charaktere = generelle_daten["charaktere"]

            datei.close()

            #---Profil zuruecksetzen---#
            datei = f"saves/{spieler_name}.json"
            datei = open(datei, "w")

            json_daten = {
                "spieler_name"           : alte_daten_spielername,
                "Erstellungsdatum"       : altes_daten_erstellungsdatum,
                "Letztes_Speichern"      : altes_daten_letztes_speichern,
                "ressourcen"             : generelle_daten_ressourcen,
                "charaktere"             : generelle_daten_charaktere,
                "time_played_in_seconds" : altes_daten_time_played_in_seconds
            }

            json.dump(json_daten, datei)

            datei.close()

            print()
            print("Profil erfolgreich zurueckgesetzt")
            time.sleep(2)

            os.execv(sys.executable, [sys.executable] + sys.argv)

        else:
            print()
            print("Profil Zuruecksetzen abgebrochen")
            time.sleep(2)
            return 1

    else:
        print()
        print("Profil Zuruecksetzen abgebrochen")
        time.sleep(2)
        return 1




def profil_loeschen(spieler_name):

    os.system(confic.terminal_clear)

    print("Profil Loeschen")
    print("==============")
    print()
    print(f"{ROT}Achtung: Dein Profil wird komplett geloescht!")
    print("Alle deine Fortschritte gehen verloren!")
    print("Du kannst dies nicht rueckgaengig machen!")
    print(f"Du kannst dich danach nicht mehr mit deinem alten Spielername und Passwort anmelden!{RESET}")
    print()

    bestätigung = input("Bist du sicher, dass du dein Profil loeschen willst? (ja/nein) ")
    print()

    if bestätigung == "ja":

        sound.sound_abspielen("invalid-login-or-password.mp3", lautstaerke=2)
        bestätigung_2 = input("schreibe: ich bin mir sicher, dass ich mein Profil loeschen moechte :   ")

        if bestätigung_2 == "ich bin mir sicher, dass ich mein Profil loeschen moechte":

            #---Profil loeschen---#
            datei = f"saves/{spieler_name}.json"
            os.remove(datei)

            #---Passwort loeschen---#
            del confic.passwoerter[spieler_name]

            datei = open("saves/passwoerter.json", "w")

            daten = {
                "passwoerter": confic.passwoerter
            }

            json.dump(daten, datei)

            datei.close()

            print()
            print("Profil erfolgreich geloescht")
            time.sleep(2)
            os.execv(sys.executable, [sys.executable] + sys.argv)

        else:
            print()
            print("Profil Loeschen abgebrochen")
            time.sleep(2)
            return 1

    else:
        print()
        print("Profil Loeschen abgebrochen")
        time.sleep(2)
        return 1




def neue_zahl():

    while True:
    
        os.system(confic.terminal_clear)

        print(f"Gebe eine Zahl zwischen 0 und 1 ein. {ROT}Benutze einen Punkt und kein Komma!!{RESET}")
        text = input("Zahl?  ")

        try:
            try:
                zahl = int(text)
            except ValueError:
                zahl = float(text)
        except ValueError:
            continue

        if 0 <= zahl <= 1:
            return zahl




def lautstaerke_aendern(spieler_name):

    while True:

        os.system(confic.terminal_clear)

        pos_balken = round(confic.lautstaerke * 20)
        neg_balken = 20 - pos_balken 

        print("Lautstaerke aendern")
        print("===================")
        print()
        print("Aktuell:")
        for i in range(pos_balken):
            print("█", end="")
        for i in range(neg_balken):
            print("░", end="")
        print()
        print()
        print("[1] Aendern")
        print("[0] Zurueck")

        time.sleep(1)
        sound.sound_abspielen("good morning.mp3", lautstaerke=2)

        wahl = input("Wahl? ")

        if wahl == "0":
            return 

        if wahl == "1":
            zahl = neue_zahl()
            confic.lautstaerke = zahl
            speichern.spiel_speichern(spieler_name)
            continue




def audio(spieler_name):

    while True:

        os.system(confic.terminal_clear)

        wahl = funktions.menue(menues.audio_menue, spieler_name)

        if wahl == 1:
            if confic.ton == True:
                confic.ton = False
                confic.main_musik = False
            else:
                confic.ton = True
                           
            speichern.spiel_speichern(spieler_name)
            continue

        elif wahl == 2:
            if confic.main_musik == True:
                confic.main_musik = False
            else:
                confic.main_musik = True

            speichern.spiel_speichern(spieler_name)
            continue

        elif wahl == 3:
            lautstaerke_aendern(spieler_name)

        elif wahl == 0:
            return 1

        else:
            continue


def wichtige_links_zeigen():

    wichtige_links = {
        "Python 3.15 Download    " : "https://www.python.org/downloads/release/python-3150/",
        "README.pdf              " : "Mitgelieferte PDF-Hilfe",
        "README.md               " : "Mitgelieferte Hilfe (Markdown)",
        "Installation PDF        " : "Mitgelieferte PDF-Hilfe",
        "Installation MD         " : "Mitgelieferte Hilfe (Markdown)",
        "More info PDF           " : "Mitgelieferte PDF-Hilfe",
        "Github des Spiels       " : "https://github.com/Jakookie-11/Class-clash",
        "Issues des Spiels melden" : "https://github.com/Jakookie-11/Class-clash/issues",
        "Fehlerhilfe             " : "Pruefe crash_logs/ und notiere die Fehler-ID"
    }

    print("══════════════════════════════")
    print("        Wichtige Links")
    print("══════════════════════════════")
    print()
    print("Wenn du beim Start einen Python-Fehler siehst, pruefe zuerst:")
    print("- Python 3.15 64-Bit")
    print("- README.pdf oder README.md")
    print("- Class Clash - Installation unter Windows.pdf")
    print()

    for schlüssel, wert in wichtige_links.items():
        print(f"{schlüssel} : {wert}")

    print()
    print("Hinweis: Class Clash benoetigt CPython 3.15 (64-Bit).")
    print("Falls ein Fehler auftritt, schau auch in den Ordner 'crash_logs/'.")
    print()
    input("Enter...")