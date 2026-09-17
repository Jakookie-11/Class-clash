import os
import time
import confic
import neues_spiel
import ressourcen
import speichern


fortschritt = {
    "kampagne": {
        "_01": 0
    }
}
   


#-----Classes-----#

class kampangen_kampf:

    def __init__(
        self,
        name,
        gegner_1,
        gegner_2,
        gegner_3=None,
        gegner_4=None,
        belohnung=0,
        ki=1,
        team_groesse=2
    ):

        self.name = name
        self.gegner_1 = gegner_1
        self.gegner_2 = gegner_2
        self.gegner_3 = gegner_3
        self.gegner_4 = gegner_4
        self.belohnung = belohnung
        self.ki = ki
        self.team_groesse = team_groesse

class kampange:

    def __init__(
        self,
        nummer,
        name,
        schwierigkeit,
        anzahl_kaempfe,
        kaempfe,
        fortschritt=0,

    ):

        self.name = name
        self.nummer = nummer
        self.schwierigkeit = schwierigkeit
        self.anzahl_kaempfe = anzahl_kaempfe
        self.kaempfe = kaempfe
        self.fortschritt = fortschritt




#---------------Kampangen---------------#

#---Kampange_1---#

kampf_1_1 = kampangen_kampf(
    "Die dumme Begruesung",
    gegner_1="cooler_fuenftklaessler",
    gegner_2="fuenftklaessler",
    belohnung=100,
    ki=1,
    team_groesse=2
)
kampf_2_1 = kampangen_kampf(
    "Sie sind schlauer geworden!",
    gegner_1="cooler_fuenftklaessler",
    gegner_2="fuenftklaessler",
    belohnung=100,
    ki=3,
    team_groesse=2
)
kampf_3_1 = kampangen_kampf(
    "die Horde",
    gegner_1="cooler_fuenftklaessler",
    gegner_2="fuenftklaessler",
    gegner_3="streber",
    belohnung=200,
    ki=3,
    team_groesse=3
)

kaempfe_kampange_1 = [kampf_1_1, kampf_2_1, kampf_3_1]

Kampange_1 = kampange(
    "_01",
    "Der 100er Gang",
    "leicht",
    3,
    kaempfe_kampange_1,
    fortschritt=0
)




kampf_1_2 = kampangen_kampf(
    "Aufsicht im Flur",
    gegner_1="aufsicht",
    gegner_2="klassenclown",
    belohnung=150,
    ki=1,
    team_groesse=2
)
kampf_2_2 = kampangen_kampf(
    "Der lange Schultag",
    gegner_1="hausmeister",
    gegner_2="aufsicht",
    belohnung=200,
    ki=3,
    team_groesse=2
)
kampf_3_2 = kampangen_kampf(
    "Schulhof-Aufruhr",
    gegner_1="hausmeister",
    gegner_2="klassenclown",
    gegner_3="aufsicht",
    belohnung=250,
    ki=3,
    team_groesse=3
)
kampf_4_2 = kampangen_kampf(
    "Der Direktor greift ein",
    gegner_1="direktor",
    gegner_2="hausmeister",
    gegner_3="aufsicht",
    belohnung=400,
    ki=3,
    team_groesse=3
)

Kampange_2 = kampange(
    "_02",
    "Chaos im Schulhaus",
    "mittel",
    4,
    [kampf_1_2, kampf_2_2, kampf_3_2, kampf_4_2],
    fortschritt=0
)

alle_kampangen = [Kampange_1, Kampange_2]


def kampange_anzeigen():

    for kampange in alle_kampangen:
        print(f"-----Kampange{kampange.nummer}-----")
        print(f"         Name: {kampange.name}")
        print(f"Schwierigkeit: {kampange.schwierigkeit}")
        print(f"      Kaempfe: {kampange.anzahl_kaempfe}")
        print(f"  Fortschritt: {kampange.fortschritt}")
        print()











def kampangen(spieler_name):

    while True:

        os.system(confic.terminal_clear)

        kampange_anzeigen()

        kampangen_vorhanden = len(alle_kampangen)

        wahl = input("Welche moechtest du Spielen (1,2,2 etc./abbrechen): ")

        if wahl == "abbrechen" or wahl == "Abbrechen":
            return 1

        if wahl == "":
            continue

        if not wahl.isdigit():
            continue

        wahl = int(wahl)

        if wahl > kampangen_vorhanden:
            continue

        kampange = alle_kampangen[wahl - 1]

        while True:

            os.system(confic.terminal_clear)

            print(f"Verfuegbare Kaempfe in der Kampange {kampange.name}: ")
            print()
            for nummer, kampf in enumerate(kampange.kaempfe[:kampange.fortschritt + 1], start=1):
                print(f"[{nummer}] {kampf.name}")
            print()
            print(f"[{nummer+1}] Zurueck")

            wahl = input("Wahl? ")

            if wahl == "":
                continue

            if not wahl.isdigit():
                continue

            wahl = int(wahl)

            if wahl == nummer + 1:
                break

            if wahl < 1 or wahl > nummer:
                continue

            else:
                ausgewaehlter_kampf = kampange.kaempfe[wahl - 1]

                print()
                print(f"Du startest: {ausgewaehlter_kampf.name}")
                time.sleep(2)

                is_win = neues_spiel.kampf(
                    leader_2=ausgewaehlter_kampf.gegner_1,
                    spieler_2_2=ausgewaehlter_kampf.gegner_2,
                    spieler_3_2=ausgewaehlter_kampf.gegner_3,
                    spieler_4_2=ausgewaehlter_kampf.gegner_4,
                    Ki=ausgewaehlter_kampf.ki,
                    team_groesse=ausgewaehlter_kampf.team_groesse
                )

                if is_win == 1:

                    os.system(confic.terminal_clear)

                    print("══════════════════════════════════════════════════")
                    print("                  KAMPF GEWONNEN")
                    print("══════════════════════════════════════════════════")
                    print()
                    print("                    SIEG!")
                    print()
                    print("        Du hast den Kampf gewonnen!")
                    print()
                    print(f"        Kampagne: {kampange.name}")
                    print(f"        Kampf: {ausgewaehlter_kampf.name}")
                    print()
                    print(f"        Belohnung: +{ausgewaehlter_kampf.belohnung} Credits")
                    print()
                    print("══════════════════════════════════════════════════")
                    print()
                    input("                [Enter] Weiter")

                    ressourcen.ressourcen["Credits"] += ausgewaehlter_kampf.belohnung
                    kampange.fortschritt += 1
                    speichern.spiel_speichern(spieler_name)
                    continue


                elif is_win == 3:

                    os.system(confic.terminal_clear)

                    print("══════════════════════════════════════════════════")
                    print("                 KAMPF VERLOREN")
                    print("══════════════════════════════════════════════════")
                    print()
                    print("                   NIEDERLAGE")
                    print()
                    print("        Dein Team wurde besiegt.")
                    print()
                    print("        Der Kampf wurde nicht abgeschlossen.")
                    print()
                    print(f"        Fortschritt: {kampange.fortschritt} / {len(kampange.kaempfe)}")
                    print()
                    print("══════════════════════════════════════════════════")
                    print()
                    input("                [Enter] Weiter")

                    continue


                elif is_win == 2:

                    os.system(confic.terminal_clear)

                    print("══════════════════════════════════════════════════")
                    print("                  KAMPF ABGEBROCHEN")
                    print("══════════════════════════════════════════════════")
                    print()
                    print("          Der Kampf wurde abgebrochen.")
                    print()
                    print("          Es wurde kein Fortschritt erzielt.")
                    print()
                    print("══════════════════════════════════════════════════")
                    print()
                    input("                [Enter] Zurück")

                    continue

        continue