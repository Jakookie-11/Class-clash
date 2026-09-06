import os
import time
import bcrypt
import json
import confic

import funktions
from saves import speichern
import menues


def begin():

    datei = f"saves/passwoerter.json"
    datei = open(datei, "r")

    daten = json.load(datei)

    datei.close()

    for spieler, passwort in daten["passwoerter"].items():
        confic.passwoerter[spieler] = passwort


    os.system(confic.terminal_clear)

    #---Vorbild---#
    print("======================")
    print("Willkommen bei ")
    print("Class clash")
    print("======================")
    time.sleep(2)

    while True:

        registieren = True

        os.system(confic.terminal_clear)

        wahl = funktions.menue(menues.anmelden_menue)
        

        if wahl == 1:

            #---Begrüsung_Spieler/Anmeldung---#
            os.system(confic.terminal_clear)
            while True:
                spieler = input("Wie heisst du? ")
                passwort = input("Passwort? ")
                print()

                if bcrypt.checkpw(
                    passwort.encode("utf-8"),
                    confic.passwoerter[spieler].encode("utf-8")
                    ):
                    print("Passwort korrekt")
                    break
                    
                else:
                    print("Passwort falsch")
                    time.sleep(2)
                    os.system(confic.terminal_clear)
                    funktions.zeilen_loeschen(4)

            time.sleep(1)
            os.system(confic.terminal_clear)
            print()
            print(f"Willkommen {spieler}")
            time.sleep(2)

            os.system(confic.terminal_clear)

            speichern.spiel_laden(spieler)

            return spieler



        elif wahl == 2:
            os.system(confic.terminal_clear)

            while registieren == True:

                while True:
                    #---Benutzername---#
                    spieler = input("Wie heisst du? ")
                    print()

                    if spieler == "":
                        print("Bitte gib einen Namen ein")
                        time.sleep(2)
                        os.system(confic.terminal_clear)
                        continue

                    if spieler.isdigit():
                        print("Der Name darf nicht nur aus Zahlen bestehen")
                        time.sleep(2)
                        os.system(confic.terminal_clear)
                        continue

                    elif spieler in confic.passwoerter:
                        print("Name bereits vergeben")
                        time.sleep(2)
                        os.system(confic.terminal_clear)
                        continue

                    break


                while True:
                    #---Passwort---#
                    passwort = input("Passwort? ")
                    print()

                    if passwort == "":
                        print("Bitte gib ein Passwort ein")
                        time.sleep(2)
                        funktions.zeilen_loeschen(3)
                        continue

                    elif len(passwort) < 6:
                        print("Das Passwort muss mindestens 6 Zeichen haben")
                        time.sleep(2)
                        funktions.zeilen_loeschen(3)
                        continue


                    funktions.zeilen_loeschen(2)

                    passwort_bestaetigung = input("Passwort bestaetigen? ")

                    if passwort == passwort_bestaetigung:

                        os.system(confic.terminal_clear)

                        bestätigung = input("Bist du sicher, dass du dich registrieren willst? (ja/nein) ")
                        funktions.zeilen_loeschen(1)

                        if bestätigung == "ja":
                            passwort_hash = bcrypt.hashpw(
                                passwort.encode("utf-8"),
                                bcrypt.gensalt()
                            ).decode("utf-8")

                            confic.passwoerter[spieler] = passwort_hash
                            speichern.spiel_speichern(spieler)
                            print("Registrierung erfolgreich")
                            time.sleep(2)

                        datei = f"saves/passwoerter.json"
                        datei = open(datei, "w")

                        passwoerter_fuer_json = {}

                        for spieler, passwort in confic.passwoerter.items():
                            passwoerter_fuer_json[spieler] = passwort

                        daten = {
                            "passwoerter": passwoerter_fuer_json
                        }

                        json.dump(daten, datei)
                        datei.close()

                        registieren = False
                        break

                    else:
                        print("Passworter stimmen nicht ueberein")
                        funktions.zeilen_loeschen(2)
                        time.sleep(2)



        elif wahl == 3:
            os.system(confic.terminal_clear)
            print("Adminbereich...")
            time.sleep(2)