import os
import time
import bcrypt
import json

import confic
import subprocess
import sys

import funktions
import speichern
import menues


def begin():

    speichern.confic_setup_laden()

    pass_update = False

    if confic.first_start_configurator == True:

        print("════════════════════════════════")
        print("           CLASS CLASH")
        print("════════════════════════════════")
        print()
        print("Willkommen!")
        print()
        print("Auf welchem System spielst du?")
        print()
        print("[1] Windows")
        print("[2] Linux")
        print()

        while True:

            betriebssystem = input("Wahl? ")

            if betriebssystem == "1":
                confic.first_start_configurator = False
                confic.terminal_clear = "cls"
                os.system(confic.terminal_clear)
                break
            elif betriebssystem == "2":
                confic.first_start_configurator = False
                confic.terminal_clear = "clear"
                os.system(confic.terminal_clear)
                break
            else:
                funktions.zeilen_loeschen(1)
                continue


    speichern.confic_setup_speichern()


    if not funktions.online_version_abrufen() == confic.version:
        os.system(confic.terminal_clear)

        subprocess.Popen([sys.executable, "updater.py"])

        return "break"



    datei = f"saves/passwoerter.json"
    datei = open(datei, "r")

    daten = json.load(datei)

    datei.close()

    for spieler, passwort in daten["passwoerter"].items():
        confic.passwoerter[spieler] = passwort


    os.system(confic.terminal_clear)

    while True:

        os.system(confic.terminal_clear)

        if funktions.versionen_vergleichen() == True or pass_update == True:

            #---Vorbild---#
            print("══════════════════════════════")
            print("        Willkommen bei ")
            print("          Class clash")
            print("══════════════════════════════")
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

        else:
            while True:

                print("════════════════════════════")
                print("      UPDATE VERFÜGBAR")
                print("════════════════════════════")
                print()
                print(f"Aktuelle Version: {confic.version}")
                print(f"Neueste Version : {funktions.online_version_abrufen()}")
                print()
                print("[1] Jetzt  Updaten")
                print("[2] Später Updaten")

                wahl = input("Wahl? ")

                if wahl == "1":
                    time.sleep(100)
                    break

                elif wahl == "2":
                    pass_update = True
                    break

                else:
                    os.system(confic.terminal_clear)
                    continue