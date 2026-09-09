import os
import sys
import time
import bcrypt
import json

import confic

import menues
import funktions
import credits

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

            is_break_credits = credits.credits()

            if is_break_credits == 1:
                continue
            

        else:
            return 1




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

    print(f"Spielername     : {spieler_name}")
    print(f"Passwort        : {confic.passwoerter[spieler_name]}")
    print(f"Erstellungsdatum: {erstellungsdatum}")
    print()
    input("fertig? ")
    os.system(confic.terminal_clear)




def profil_zuruecksetzen(spieler_name):

    os.system(confic.terminal_clear)

    print("Profil Zuruecksetzen")
    print("===================")
    print()
    print("Achtung: Dein Profil wird auf den Standard zurueckgesetzt!")
    print("Alle deine Fortschritte gehen verloren!")
    print("Dein Spielername, Erstellungsdatum bleiben erhalten!")
    print("Du kannst dies nicht rueckgaengig machen!")
    print("Du kannst dich danach wieder mit deinem alten Spielername und Passwort anmelden!")
    print()

    bestätigung = input("Bist du sicher, dass du dein Profil zuruecksetzen willst? (ja/nein) ")
    print()

    if bestätigung == "ja":

        bestätigung_2 = input("schreibe: ich bin mir sicher, dass ich mein Profil zuruecksetzen moechte :   ")

        if bestätigung_2 == "ich bin mir sicher, dass ich mein Profil zuruecksetzen moechte":

            #---Wichtige Daten holen---#
            datei = f"saves/{spieler_name}.json"
            datei = open(datei, "r")
            alte_daten_spieler = json.load(datei)

            alte_daten_spielername = alte_daten_spieler["spieler_name"]
            altes_daten_erstellungsdatum = alte_daten_spieler["Erstellungsdatum"]
            altes_daten_letztes_speichern = alte_daten_spieler["Letztes_Speichern"]

            datei.close()

            #---Generelle Daten holen---#
            datei = "standard.json"
            datei = open(datei, "r")
            generelle_daten = json.load(datei)

            generelle_daten_ressourcen = generelle_daten["ressourcen"]
            generelle_daten_charaktere = generelle_daten["charaktere"]

            datei.close()

            #---Profil zuruecksetzen---#
            datei = f"saves/{spieler_name}.json"
            datei = open(datei, "w")

            json_daten = {
                "spieler_name"    : alte_daten_spielername,
                "Erstellungsdatum" : altes_daten_erstellungsdatum,
                "Letztes_Speichern" : altes_daten_letztes_speichern,
                "ressourcen"      : generelle_daten_ressourcen,
                "charaktere"      : generelle_daten_charaktere
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
    print("Achtung: Dein Profil wird komplett geloescht!")
    print("Alle deine Fortschritte gehen verloren!")
    print("Du kannst dies nicht rueckgaengig machen!")
    print("Du kannst dich danach nicht mehr mit deinem alten Spielername und Passwort anmelden!")
    print()

    bestätigung = input("Bist du sicher, dass du dein Profil loeschen willst? (ja/nein) ")
    print()

    if bestätigung == "ja":

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