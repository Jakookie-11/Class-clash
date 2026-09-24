import os
import time
import bcrypt
import json

import confic
import getpass

import funktions
import speichern
import menues
import speichern


def begin():

    speichern.confic_setup_laden()

    os.makedirs("saves", exist_ok=True)
    passwoerter_datei = "saves/passwoerter.json"

    if not os.path.exists(passwoerter_datei):
        with open(passwoerter_datei, "w", encoding="utf-8") as datei:
            json.dump({"passwoerter": {}}, datei)

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

    datei = f"saves/passwoerter.json"
    confic.passwoerter.clear()

    if os.path.exists(datei):
        with open(datei, "r", encoding="utf-8") as datei_lesen:
            daten = json.load(datei_lesen)

        passwoerter = daten.get("passwoerter", {})
        for spieler, passwort in passwoerter.items():
            confic.passwoerter[spieler] = passwort


    os.system(confic.terminal_clear)

    print("╔══════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                   CLASS CLASH                                    ║")
    print("║                                                                                  ║")
    print(f"║                                VERSION {funktions.lokale_version_abrufen()}                              ║")
    print("║                                                                                  ║")
    print("║  Willkommen zur ersten Beta-Version, die mit mehreren Spielern geteilt wird!     ║")
    print("║                                                                                  ║")
    print("║  RESPEKT UND FEEDBACK                                                            ║")
    print("║  In diesem Spiel steckt sehr viel Arbeit und Zeit. Bitte beurteile das Spiel     ║")
    print("║  mit Respekt und bedenke, dass es sich noch in der Entwicklung befindet.         ║")
    print("║                                                                                  ║")
    print("║  FEHLER MELDEN                                                                   ║")
    print("║  Wenn du einen Fehler findest, melde ihn gerne! Jeder gemeldete Fehler wird      ║")
    print("║  gewürdigt und du wirst dafür in den Credits erwähnt. Gib möglichst an, was      ║")
    print("║  passiert ist und die jeweilige crash.txt.                                       ║")
    print("║                                                                                  ║")
    print("║  KAMPAGNEN                                                                       ║")
    print("║  Die Kampagnen 3-5 wurden größtenteils von einer KI erstellt und sind eher als   ║")
    print("║  zusätzliche Inhalte zu betrachten, nicht als vollwertige Kampagnen.             ║")
    print("║  Kampagne 6 wurde getestet und so gut wie möglich ausbalanciert. Rückmeldungen   ║")
    print("║  zur Story und zum Schwierigkeitsgrad sind ausdrücklich willkommen!              ║")
    print("║                                                                                  ║")
    print("║  MITARBEIT UND IDEEN                                                             ║")
    print("║  Du möchtest bei der Entwicklung helfen? Melde dich! Auch ohne Programmier-      ║")
    print("║  kenntnisse finden wir bestimmt eine passende Aufgabe. Mitarbeit wird in den     ║")
    print("║  Credits mit einer besseren Position gewürdigt.                                  ║")
    print("║                                                                                  ║")
    print("║  FÄHIGKEITEN UND CHARAKTERE                                                      ║")
    print("║  Manche Fähigkeiten spiegeln meine persönliche Meinung wider und müssen nicht    ║")
    print("║  der Realität entsprechen. Einige Fähigkeiten sind noch Platzhalter. Geplant     ║")
    print("║  sind drei einzigartige Fähigkeiten pro Charakter. Kreative Ideen sind           ║")
    print("║  willkommen (Mitarbeit)!                                                         ║")
    print("║                                                                                  ║")
    print("║  WICHTIG                                                                         ║")
    print("║  Sichere deine Spielstände regelmäßig. Während der Beta können Fehler auftreten  ║")
    print("║  und Inhalte verändert werden.                                                   ║")
    print("║  !!!Das Spiel niemals über Fensterschliessung schliessen, sondern über Beenden   ║")
    print("║                                                                                  ║")
    print("║  CHANGELOGS UND WEITERE INFORMATIONEN                                            ║")
    print("║  Die Changelogs findest du auf GitHub unter Releases. Weitere Informationen      ║")
    print("║  zu Fehlerberichten, Mitarbeit und dem Beta-Test stehen in der More info.md.     ║")
    print("║                                                                                  ║")
    print("║                           Viel Erfolg und Spaß!                                  ║")
    print("╚══════════════════════════════════════════════════════════════════════════════════╝")

    input("Enter...")

    while True:

        os.system(confic.terminal_clear)

        if funktions.versionen_vergleichen() or pass_update == True:

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
                        spieler = input("Wie heisst du?/[0]abbrechen  ").strip()

                        if spieler == "0":
                            break

                        if confic.passwort_sichtbarkeitshinweis_anzeigen == True:
                            print("-------------")
                            print("! Das Passwort ist unsichtbar, das Kann in den Einstellungen unter Profil aber geaendert werden.")
                            print("-------------")
                            confic.passwort_sichtbarkeitshinweis_anzeigen = False
                            speichern.confic_setup_speichern()

                        if confic.passwort_sichtbarkeit == False:
                            passwort = getpass.getpass("Passwort? ").strip()

                        elif confic.passwort_sichtbarkeit == True:
                            passwort = input("Passwort? ")
                        
                        print()

                        if spieler == "" or spieler not in confic.passwoerter:
                            print("Benutzername unbekannt")
                            time.sleep(2)
                            os.system(confic.terminal_clear)
                            funktions.zeilen_loeschen(4)
                            continue

                        gespeichertes_passwort = str(confic.passwoerter[spieler])

                        if gespeichertes_passwort.startswith("$2"):
                            passwort_ok = bcrypt.checkpw(
                                passwort.encode("utf-8"),
                                gespeichertes_passwort.encode("utf-8")
                            )
                        else:
                            passwort_ok = gespeichertes_passwort == passwort

                        if passwort_ok:
                            print("Passwort korrekt")
                            break

                        else:
                            print("Passwort falsch")
                            time.sleep(2)
                            os.system(confic.terminal_clear)
                            funktions.zeilen_loeschen(4)

                    if spieler == "0":
                        break

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
                print(f"Aktuelle Version: {funktions.lokale_version_abrufen()}")
                print(f"Neueste Version : {funktions.online_version_abrufen()}")
                print()
                print("[1] Jetzt  Updaten")
                print("[2] Später Updaten")

                wahl = input("Wahl? ")

                if wahl == "1":
                    return "break"

                elif wahl == "2":
                    pass_update = True
                    break

                else:
                    os.system(confic.terminal_clear)
                    continue