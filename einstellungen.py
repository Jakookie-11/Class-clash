import os
import time
import bcrypt
import json

import confic

import menues
import funktions

def einstellungen(spieler_name):

    while True:

        os.system(confic.terminal_clear)

        wahl = funktions.menue(menues.einstellungen_menue, spieler_name)

        if wahl == 1:
            os.system(confic.terminal_clear)

            is_breake_profil_einstellungen = profil_enstellungen(spieler_name)

            if is_breake_profil_einstellungen == 1:
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
            print()

        elif wahl == 3:
            print()

        elif wahl == 4:
            print()

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

            neues_passwort = input("Neues Passwort: ")
            funktions.zeilen_loeschen(1)
            neues_passwort_wiederholen = input("Neues Passwort wiederholen: ")

            if neues_passwort == neues_passwort_wiederholen:

                bestätigung = input("Bist du sicher, dass du dein Passwort aendern willst? (ja/nein) ")
                if bestätigung == "ja":
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
                print("Passwoerter stimmen nicht ueberein")
                time.sleep(2)