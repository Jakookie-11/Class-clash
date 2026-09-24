import os
import time
import confic
import neues_spiel
import ressourcen
import speichern
import charakter_bip
import charaktere


fortschritt = {}
   

# ══════════════════════════════════════════════════════════════
# Classes
# ══════════════════════════════════════════════════════════════



class kampangen_kampf:

    def __init__(
        self,
        name,
        spieler_1=None,
        spieler_2=None,
        spieler_3=None,
        spieler_4=None,
        gegner_1=None,
        gegner_2=None,
        gegner_3=None,
        gegner_4=None,
        belohnung=0,
        ki=1,
        npc_level=1,
        team_groesse=None,
        team_groesse_1=None,
        team_groesse_2=None,
        story_vorher=None,
        story_nachher=None,
        ist_kampf=True
    ):
        self.name = name
        self.spieler_1 = spieler_1
        self.spieler_2 = spieler_2
        self.spieler_3 = spieler_3
        self.spieler_4 = spieler_4
        self.gegner_1 = gegner_1
        self.gegner_2 = gegner_2
        self.gegner_3 = gegner_3
        self.gegner_4 = gegner_4
        self.belohnung = belohnung
        self.ki = ki
        self.npc_level = npc_level
        if team_groesse_1 is None:
            team_groesse_1 = team_groesse if team_groesse is not None else 2

        if team_groesse_2 is None:
            team_groesse_2 = team_groesse if team_groesse is not None else 2
        self.team_groesse_1 = team_groesse_1
        self.team_groesse_2 = team_groesse_2
        self.story_vorher = story_vorher
        self.story_nachher = story_nachher
        self.ist_kampf = ist_kampf

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



# ══════════════════════════════════════════════════════════════
# Allgemeine Funktionen
# ══════════════════════════════════════════════════════════════

def dialog_anzeigen(dialog):

    if not dialog:
        return

    os.system(confic.terminal_clear)

    laengster_sprecher = max(len(sprecher) for sprecher, text in dialog)
    breite = laengster_sprecher + 1

    for sprecher, text in dialog:

        if sprecher == "" and text == "":
            print()
            continue

        print(f"{sprecher :{breite}}: ", end="", flush=True)

        for buchstabe in text:
            print(buchstabe, end="", flush=True)
            time.sleep(0.05)

        print()

    input("Enter...")



def kampange_anzeigen():

    for kampange in alle_kampangen:
        print(f"-----Kampange{kampange.nummer}-----")
        print(f"         Name: {kampange.name}")
        print(f"Schwierigkeit: {kampange.schwierigkeit}")
        print(f"      Kaempfe: {kampange.anzahl_kaempfe}")
        print(f"  Fortschritt: {kampange.fortschritt}")
        print()



def npc_level_setzen(level, Leader_2, spieler_2_2, spieler_3_2=None, spieler_4_2=None):

    for spieler in [Leader_2,spieler_2_2, spieler_3_2, spieler_4_2]:

        if spieler is None:
            continue

        level_zuruecksetzen(spieler)

        for i in range(max(0, level - 1)):

            charakter_bip.level_up(spieler)



def level_zuruecksetzen(wen):

    if wen is None:
        return

    charakter = charaktere.Charaktere[wen]

    charakter.level = 1
    charakter.max_hp = charakter.max_max_hp
    charakter.hp = charakter.max_hp
    charakter.schaden = charakter.max_schaden
    


def kampangen(spieler_name):

    while True:

        os.system(confic.terminal_clear)

        kampange_anzeigen()

        kampangen_vorhanden = len(alle_kampangen)

        wahl = input("Welche moechtest du Spielen (1,2,2 etc./[0]abbrechen): ")

        if wahl == "0" or wahl == "abbrechen":
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

            for nummer, kampf in enumerate(
                kampange.kaempfe[:kampange.fortschritt + 1],
                start=1
            ):

                if kampf.ist_kampf:
                    print(f"[{nummer:02d}] {kampf.name}")
                else:
                    print(f"[{nummer:02d}] {kampf.name:<30} [Story]")

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

                # ══════════════════════════════════════════════════════════════
                # Eigentlicher Kampf
                # ══════════════════════════════════════════════════════════════

                ausgewaehlter_kampf = kampange.kaempfe[wahl - 1]

                if not ausgewaehlter_kampf.ist_kampf:

                    dialog_anzeigen(ausgewaehlter_kampf.story_vorher)

                    if wahl == kampange.fortschritt + 1:
                        kampange.fortschritt += 1

                    speichern.spiel_speichern(spieler_name)

                    continue

                npc_level_setzen(ausgewaehlter_kampf.npc_level, ausgewaehlter_kampf.gegner_1, ausgewaehlter_kampf.gegner_2, ausgewaehlter_kampf.gegner_3, ausgewaehlter_kampf.gegner_4)

                print()
                print(f"Du startest: {ausgewaehlter_kampf.name}")
                time.sleep(2)

                dialog_anzeigen(ausgewaehlter_kampf.story_vorher)

                os.system(confic.terminal_clear)

                spieler_team = [
                    name
                    for name in [
                        ausgewaehlter_kampf.spieler_1,
                        ausgewaehlter_kampf.spieler_2,
                        ausgewaehlter_kampf.spieler_3,
                        ausgewaehlter_kampf.spieler_4
                    ]
                    if name is not None
                ]

                gegner_team = [
                    name
                    for name in [
                        ausgewaehlter_kampf.gegner_1,
                        ausgewaehlter_kampf.gegner_2,
                        ausgewaehlter_kampf.gegner_3,
                        ausgewaehlter_kampf.gegner_4
                    ]
                    if name is not None
                ]

                is_win = neues_spiel.kampf(
                    team_1=spieler_team if spieler_team else None,
                    team_2=gegner_team,
                    Ki=ausgewaehlter_kampf.ki,
                    team_groesse_1=ausgewaehlter_kampf.team_groesse_1,
                    team_groesse_2=ausgewaehlter_kampf.team_groesse_2
                )

                if is_win == 1:

                    os.system(confic.terminal_clear)

                    dialog_anzeigen(ausgewaehlter_kampf.story_nachher)

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

                    level_zuruecksetzen(ausgewaehlter_kampf.gegner_1)
                    level_zuruecksetzen(ausgewaehlter_kampf.gegner_2)
                    level_zuruecksetzen(ausgewaehlter_kampf.gegner_3)
                    level_zuruecksetzen(ausgewaehlter_kampf.gegner_4)

                    ressourcen.ressourcen["Credits"] += ausgewaehlter_kampf.belohnung
                    if wahl == kampange.fortschritt + 1:
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

                    level_zuruecksetzen(ausgewaehlter_kampf.gegner_1)
                    level_zuruecksetzen(ausgewaehlter_kampf.gegner_2)
                    level_zuruecksetzen(ausgewaehlter_kampf.gegner_3)
                    level_zuruecksetzen(ausgewaehlter_kampf.gegner_4)

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

                    level_zuruecksetzen(ausgewaehlter_kampf.gegner_1)
                    level_zuruecksetzen(ausgewaehlter_kampf.gegner_2)
                    level_zuruecksetzen(ausgewaehlter_kampf.gegner_3)
                    level_zuruecksetzen(ausgewaehlter_kampf.gegner_4)

                    continue

        continue





# ══════════════════════════════════════════════════════════════


# Kampangen


# ══════════════════════════════════════════════════════════════




# ══════════════════════════════════════════════════════════════
# Kampange_01
# ══════════════════════════════════════════════════════════════

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


Kampange_1 = kampange(
    "_01",
    "Der 100er Gang",
    "leicht",
    3,
    [kampf_1_1, kampf_2_1, kampf_3_1],
    fortschritt=0
)



# ══════════════════════════════════════════════════════════════
# Kampange_2
# ══════════════════════════════════════════════════════════════


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



# ══════════════════════════════════════════════════════════════
# Kampange_3
# Die Sache mit den 6.-Klässlern
# ══════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════
# Kampf 1 – Wo ist mein Zeug?
# ══════════════════════════════════════════════════════════════

kampf_1_3 = kampangen_kampf(
    "Wo ist mein Zeug?",
    gegner_1="normaler_6_klaessler",
    gegner_2="normaler_6_klaessler",
    belohnung=100,
    ki=1,
    npc_level=2,
    team_groesse=2,

    story_vorher=[
        ("Jakob", "Wo ist eigentlich mein Zeug?"),
        ("Jakob", "Ich hatte das doch gerade noch hier."),
        ("???", "Suchst du vielleicht DAS hier?"),
        ("Jakob", "Mein Zeug?!"),
        ("6.-Klässler", "Jo."),
        ("Jakob", "Gib es zurück."),
        ("6.-Klässler", "Nö."),
        ("Jakob", "Okay..."),
        ("Jakob", "Dann machen wir das eben anders.")
    ],

    story_nachher=[
        ("Jakob", "So. Und jetzt gib mir meine Sachen."),
        ("6.-Klässler", "Die anderen haben sie."),
        ("Jakob", "Welche anderen?"),
        ("6.-Klässler", "Die Bande."),
        ("Jakob", "Natürlich gibt es eine Bande...")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 2 – Die Bande
# ══════════════════════════════════════════════════════════════

kampf_2_3 = kampangen_kampf(
    "Die Bande",
    gegner_1="aggressiver_6_klaessler",
    gegner_2="normaler_6_klaessler",
    belohnung=150,
    ki=2,
    npc_level=2,
    team_groesse=2,

    story_vorher=[
        ("Jakob", "Also gut. Wo ist diese Bande?"),
        ("6.-Klässler", "Da vorne."),
        ("Jakob", "Das sind zwei Leute."),
        ("6.-Klässler", "Das reicht."),
        ("Jakob", "Ihr habt mein Zeug geklaut und seid zu zweit?"),
        ("Aggressiver 6.-Klässler", "Wir sind mehr als genug."),
        ("Jakob", "Das werden wir ja sehen.")
    ],

    story_nachher=[
        ("Jakob", "Wo sind meine Sachen?"),
        ("Aggressiver 6.-Klässler", "Wir haben sie nicht mehr."),
        ("Jakob", "Was soll das heißen?"),
        ("Aggressiver 6.-Klässler", "Wir mussten sie abgeben."),
        ("Jakob", "An wen?"),
        ("Aggressiver 6.-Klässler", "Keine Ahnung."),
        ("Jakob", "Das wird ja immer besser.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 3 – Das Lager
# ══════════════════════════════════════════════════════════════

kampf_3_3 = kampangen_kampf(
    "Das Lager",
    gegner_1="normaler_6_klaessler",
    gegner_2="schlauer_6_klaessler",
    gegner_3="nerviger_6_klaessler",
    belohnung=200,
    ki=2,
    npc_level=2,
    team_groesse=3,

    story_vorher=[
        ("Jakob", "Okay. Das soll also das Lager sein."),
        ("Jakob", "Warum stehen hier ungefähr hundert Sachen herum?"),
        ("Schlauer 6.-Klässler", "Wir sammeln sie."),
        ("Jakob", "Ihr klaut sie."),
        ("Schlauer 6.-Klässler", "Das ist eine Frage der Perspektive."),
        ("Jakob", "Da liegt sogar ein ganzer Rucksack."),
        ("Nerviger 6.-Klässler", "Den wollte jemand nicht mehr."),
        ("Jakob", "Der Besitzer sieht das wahrscheinlich anders.")
    ],

    story_nachher=[
        ("Jakob", "Hier muss irgendwo eine Liste sein."),
        ("Jakob", "Moment..."),
        ("Jakob", "Warum steht da mein Name?"),
        ("Jakob", "Und warum steht dahinter 'Priorität'?")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 4 – Gesucht
# ══════════════════════════════════════════════════════════════

kampf_4_3 = kampangen_kampf(
    "Gesucht",
    gegner_1="aggressiver_6_klaessler",
    gegner_2="nerviger_6_klaessler",
    gegner_3="normaler_6_klaessler",
    belohnung=250,
    ki=2,
    npc_level=3,
    team_groesse=3,

    story_vorher=[
        ("Jakob", "Warum bin ich auf dieser Liste?"),
        ("Jakob", "Was habe ich euch überhaupt getan?"),
        ("Nerviger 6.-Klässler", "Keine Ahnung."),
        ("Jakob", "Was?!"),
        ("Nerviger 6.-Klässler", "Wir haben nur den Auftrag bekommen."),
        ("Jakob", "Von wem?"),
        ("Aggressiver 6.-Klässler", "Das geht dich nichts an."),
        ("Jakob", "Dann finde ich es eben selbst heraus.")
    ],

    story_nachher=[
        ("Jakob", "Jetzt redet."),
        ("Aggressiver 6.-Klässler", "Wir bekommen unsere Befehle über Zettel."),
        ("Jakob", "Zettel?"),
        ("Aggressiver 6.-Klässler", "Ja."),
        ("Jakob", "Und woher kommen die?"),
        ("Nerviger 6.-Klässler", "Sie liegen morgens immer an einem bestimmten Ort."),
        ("Jakob", "Wo?")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 5 – Der Auftrag
# ══════════════════════════════════════════════════════════════

kampf_5_3 = kampangen_kampf(
    "Der Auftrag",
    gegner_1="starker_6_klaessler",
    gegner_2="aggressiver_6_klaessler",
    gegner_3="cooler_6_klaessler",
    belohnung=300,
    ki=2,
    npc_level=3,
    team_groesse=3,

    story_vorher=[
        ("Jakob", "Da ist also der Ort."),
        ("Jakob", "Und da liegt tatsächlich ein neuer Zettel."),
        ("Jakob", "Mal sehen..."),
        ("Jakob", "Ich soll etwas holen."),
        ("Jakob", "Und danach verschwinden."),
        ("Cooler 6.-Klässler", "Du solltest den Zettel nicht lesen."),
        ("Jakob", "Zu spät."),
        ("Starker 6.-Klässler", "Dann müssen wir dich wohl aufhalten.")
    ],

    story_nachher=[
        ("Jakob", "Was soll ich holen?"),
        ("Cooler 6.-Klässler", "Das wissen wir nicht."),
        ("Jakob", "Ihr arbeitet für jemanden und wisst nicht einmal, was ihr tut?"),
        ("Cooler 6.-Klässler", "Wir bekommen Credits."),
        ("Jakob", "Ah. Sehr überzeugend."),
        ("Jakob", "Wer gibt euch die Zettel?")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 6 – Der Informant
# ══════════════════════════════════════════════════════════════

kampf_6_3 = kampangen_kampf(
    "Der Informant",
    gegner_1="schlauer_6_klaessler",
    gegner_2="cooler_6_klaessler",
    belohnung=350,
    ki=3,
    npc_level=3,
    team_groesse=2,

    story_vorher=[
        ("Jakob", "Du weißt mehr als die anderen."),
        ("Schlauer 6.-Klässler", "Vielleicht."),
        ("Jakob", "Wer steckt dahinter?"),
        ("Schlauer 6.-Klässler", "Das willst du wirklich wissen?"),
        ("Jakob", "Ja."),
        ("Schlauer 6.-Klässler", "Dann musst du erst an uns vorbei.")
    ],

    story_nachher=[
        ("Schlauer 6.-Klässler", "Okay."),
        ("Jakob", "Endlich."),
        ("Schlauer 6.-Klässler", "Die Befehle kommen nicht von einem 6.-Klässler."),
        ("Jakob", "Das dachte ich mir."),
        ("Jakob", "Von wem dann?"),
        ("Schlauer 6.-Klässler", "Jemand, der hier schon ziemlich lange arbeitet."),
        ("Jakob", "Ein Lehrer?"),
        ("Schlauer 6.-Klässler", "Nein.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 7 – Der Boss
# ══════════════════════════════════════════════════════════════

kampf_7_3 = kampangen_kampf(
    "Der Boss",
    gegner_1="starker_6_klaessler",
    gegner_2="cooler_6_klaessler",
    gegner_3="aggressiver_6_klaessler",
    gegner_4="nerviger_6_klaessler",
    belohnung=450,
    ki=3,
    npc_level=4,
    team_groesse=4,

    story_vorher=[
        ("Jakob", "Du bist also der Anführer."),
        ("Cooler 6.-Klässler", "Man könnte es so nennen."),
        ("Jakob", "Dann weißt du auch, wer euch beauftragt."),
        ("Cooler 6.-Klässler", "Natürlich."),
        ("Jakob", "Wer?"),
        ("Cooler 6.-Klässler", "Das wirst du nicht erfahren."),
        ("Jakob", "Dann müssen wir wohl noch einmal kämpfen.")
    ],

    story_nachher=[
        ("Cooler 6.-Klässler", "Okay! Okay!"),
        ("Jakob", "Name."),
        ("Cooler 6.-Klässler", "Der Hausmeister."),
        ("Jakob", "..."),
        ("Jakob", "Der Hausmeister?!"),
        ("Cooler 6.-Klässler", "Ja."),
        ("Jakob", "Das ergibt überhaupt keinen Sinn.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 8 – Der Auftraggeber
# ══════════════════════════════════════════════════════════════

kampf_8_3 = kampangen_kampf(
    "Der Auftraggeber",
    gegner_1="hausmeister",
    gegner_2="aufsicht",
    belohnung=500,
    ki=3,
    npc_level=4,
    team_groesse=2,

    story_vorher=[
        ("Jakob", "Da bist du ja."),
        ("Hausmeister", "Ich hatte mich schon gefragt, wann du auftauchst."),
        ("Jakob", "Du hast die 6.-Klässler beauftragt."),
        ("Hausmeister", "Das stimmt."),
        ("Jakob", "Warum?"),
        ("Hausmeister", "Du hast etwas gefunden, das du nicht finden solltest."),
        ("Jakob", "Was denn?"),
        ("Hausmeister", "Das spielt jetzt keine Rolle mehr.")
    ],

    story_nachher=[
        ("Jakob", "Jetzt redest du."),
        ("Hausmeister", "Die 6.-Klässler sollten nur die Unterlagen finden."),
        ("Jakob", "Welche Unterlagen?"),
        ("Hausmeister", "Du hast sie bereits."),
        ("Jakob", "Was?"),
        ("Hausmeister", "Du hast die ganze Zeit danach gesucht.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 9 – Letzte Chance
# ══════════════════════════════════════════════════════════════

kampf_9_3 = kampangen_kampf(
    "Letzte Chance",
    gegner_1="hausmeister",
    gegner_2="direktor",
    gegner_3="aufsicht",
    belohnung=600,
    ki=3,
    npc_level=5,
    team_groesse=3,

    story_vorher=[
        ("Jakob", "Warum hilft dir der Direktor?"),
        ("Direktor", "Ich habe keine Ahnung, wovon du sprichst."),
        ("Jakob", "Dann erklär mir das hier."),
        ("Direktor", "Woher hast du diese Unterlagen?"),
        ("Jakob", "Aus eurem Lager."),
        ("Hausmeister", "Wir müssen das jetzt beenden."),
        ("Jakob", "Genau das dachte ich mir.")
    ],

    story_nachher=[
        ("Direktor", "Warte."),
        ("Jakob", "Was?"),
        ("Direktor", "Der Hausmeister hat uns ebenfalls belogen."),
        ("Jakob", "Dann hat er alleine gehandelt?"),
        ("Direktor", "Nein."),
        ("Jakob", "Wer dann?"),
        ("Direktor", "Jemand außerhalb der Schule.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 10 – Der letzte Kampf
# ══════════════════════════════════════════════════════════════

kampf_10_3 = kampangen_kampf(
    "Der letzte Kampf",
    gegner_1="direktor",
    gegner_2="hausmeister",
    gegner_3="cooler_6_klaessler",
    gegner_4="starker_6_klaessler",
    belohnung=1000,
    ki=4,
    npc_level=6,
    team_groesse=4,

    story_vorher=[
        ("Jakob", "Also gut."),
        ("Jakob", "Dann bringen wir das jetzt zu Ende."),
        ("Direktor", "Du verstehst immer noch nicht, worum es geht."),
        ("Jakob", "Dann erklär es mir."),
        ("Direktor", "Die Unterlagen sind viel wichtiger, als du denkst."),
        ("Jakob", "Dann werde ich sie wohl behalten."),
        ("Hausmeister", "Das werden wir verhindern."),
        ("Jakob", "Na dann. Kommt.")
    ],

    story_nachher=[
        ("Jakob", "Das war's."),
        ("Hausmeister", "Du hast gewonnen."),
        ("Jakob", "Was stand in den Unterlagen?"),
        ("Direktor", "Eine Liste."),
        ("Jakob", "Eine Liste mit was?"),
        ("Direktor", "Mit Namen."),
        ("Jakob", "Welche Namen?"),
        ("Direktor", "Von Schülern."),
        ("Jakob", "..."),
        ("Jakob", "Und meiner war ganz oben."),
        ("Direktor", "Ja."),
        ("Jakob", "Dann ist die Sache wohl doch noch nicht vorbei.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampagne erstellen
# ══════════════════════════════════════════════════════════════

Kampange_3 = kampange(
    "_03",
    "Die Sache mit den 6.-Klässlern",
    "schwer",
    10,
    [
        kampf_1_3,
        kampf_2_3,
        kampf_3_3,
        kampf_4_3,
        kampf_5_3,
        kampf_6_3,
        kampf_7_3,
        kampf_8_3,
        kampf_9_3,
        kampf_10_3
    ],
    fortschritt=0
)




# ══════════════════════════════════════════════════════════════
# Kampange_4
# Die Liste
# ══════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════
# Kampf 1 – Die Liste
# ══════════════════════════════════════════════════════════════

kampf_1_4 = kampangen_kampf(
    "Die Liste",
    gegner_1="normaler_6_klaessler",
    gegner_2="schlauer_6_klaessler",
    belohnung=100,
    ki=1,
    npc_level=4,
    team_groesse=2,

    story_vorher=[
        ("Jakob", "Also gut. Schauen wir uns diese Liste einmal genauer an."),
        ("Direktor", "Was steht dort?"),
        ("Jakob", "Mehrere Namen."),
        ("Direktor", "Schüler?"),
        ("Jakob", "Ja."),
        ("Jakob", "Und neben jedem Namen stehen irgendwelche Angaben."),
        ("Direktor", "Was steht neben deinem Namen?"),
        ("Jakob", "Priorität 1."),
        ("Direktor", "..."),
        ("Jakob", "Das gefällt mir irgendwie nicht.")
    ],

    story_nachher=[
        ("Jakob", "Ihr wisst also wirklich nicht, was das bedeutet?"),
        ("6.-Klässler", "Nein."),
        ("Jakob", "Dann finde ich es eben selbst heraus."),
        ("Jakob", "Aber zuerst will ich wissen, wer noch auf dieser Liste steht.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 2 – Weitere Namen
# ══════════════════════════════════════════════════════════════

kampf_2_4 = kampangen_kampf(
    "Weitere Namen",
    gegner_1="aggressiver_6_klaessler",
    gegner_2="nerviger_6_klaessler",
    belohnung=150,
    ki=2,
    npc_level=4,
    team_groesse=2,

    story_vorher=[
        ("Jakob", "Ich habe mir die anderen Namen angesehen."),
        ("Jakob", "Einige davon kenne ich."),
        ("Jakob", "Andere habe ich noch nie gehört."),
        ("Direktor", "Zeig mir die Liste."),
        ("Jakob", "Hier."),
        ("Direktor", "Moment."),
        ("Direktor", "Dieser Name..."),
        ("Jakob", "Was ist damit?"),
        ("Direktor", "Das war einmal ein Schüler dieser Schule.")
    ],

    story_nachher=[
        ("Jakob", "Und was ist aus ihm geworden?"),
        ("Direktor", "Ich weiß es nicht."),
        ("Jakob", "Er steht auf dieser Liste."),
        ("Jakob", "Dann sollten wir herausfinden, warum.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 3 – Der alte Raum
# ══════════════════════════════════════════════════════════════

kampf_3_4 = kampangen_kampf(
    "Der alte Raum",
    gegner_1="starker_6_klaessler",
    gegner_2="normaler_6_klaessler",
    gegner_3="nerviger_6_klaessler",
    belohnung=200,
    ki=2,
    npc_level=5,
    team_groesse=3,

    story_vorher=[
        ("Direktor", "Vielleicht gibt es noch alte Unterlagen im Keller."),
        ("Jakob", "Im Keller?"),
        ("Direktor", "Dort wurden früher die alten Schulakten gelagert."),
        ("Jakob", "Na dann los."),
        ("Jakob", "Hier ist ja alles voller Kartons."),
        ("Direktor", "Die meisten davon wurden seit Jahren nicht angerührt."),
        ("Jakob", "Und da hinten ist ein Schrank."),
        ("Jakob", "Der ist abgeschlossen."),
        ("Direktor", "Dann brauchen wir wohl einen Schlüssel.")
    ],

    story_nachher=[
        ("Jakob", "Das war's."),
        ("Jakob", "Und jetzt der Schrank."),
        ("Direktor", "Du hast den Schlüssel?"),
        ("Jakob", "Natürlich."),
        ("Jakob", "Mal sehen, was da drin ist.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 4 – Das Archiv
# ══════════════════════════════════════════════════════════════

kampf_4_4 = kampangen_kampf(
    "Das Archiv",
    gegner_1="cooler_6_klaessler",
    gegner_2="schlauer_6_klaessler",
    belohnung=250,
    ki=2,
    npc_level=5,
    team_groesse=2,

    story_vorher=[
        ("Jakob", "Hier sind jede Menge alte Akten."),
        ("Direktor", "Vielleicht finden wir etwas über die Liste."),
        ("Jakob", "Moment."),
        ("Jakob", "Da ist eine alte Version davon."),
        ("Direktor", "Eine alte Liste?"),
        ("Jakob", "Ja."),
        ("Jakob", "Und sie ist ziemlich alt."),
        ("Direktor", "Wie alt?"),
        ("Jakob", "Mehr als zehn Jahre.")
    ],

    story_nachher=[
        ("Jakob", "Das kann nicht sein."),
        ("Direktor", "Was hast du gefunden?"),
        ("Jakob", "Meinen Namen."),
        ("Direktor", "..."),
        ("Jakob", "Auf einer Liste, die älter ist als meine Zeit an dieser Schule.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 5 – Das kann nicht sein
# ══════════════════════════════════════════════════════════════

kampf_5_4 = kampangen_kampf(
    "Das kann nicht sein",
    gegner_1="aggressiver_6_klaessler",
    gegner_2="starker_6_klaessler",
    gegner_3="nerviger_6_klaessler",
    belohnung=300,
    ki=2,
    npc_level=6,
    team_groesse=3,

    story_vorher=[
        ("Jakob", "Vielleicht ist das einfach nur ein anderer Jakob."),
        ("Direktor", "Das könnte sein."),
        ("Jakob", "Aber hier steht mein vollständiger Name."),
        ("Direktor", "Zeig mal das Datum."),
        ("Jakob", "Da."),
        ("Direktor", "..."),
        ("Jakob", "Was ist?"),
        ("Direktor", "An diesem Datum warst du noch gar nicht hier."),
        ("Jakob", "Das wird immer seltsamer.")
    ],

    story_nachher=[
        ("Jakob", "Was weißt du über diese Liste?"),
        ("Direktor", "Nicht viel."),
        ("Jakob", "Du weißt doch irgendetwas."),
        ("Direktor", "Es gab damals ein Projekt."),
        ("Jakob", "Was für ein Projekt?")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 6 – Das Projekt
# ══════════════════════════════════════════════════════════════

kampf_6_4 = kampangen_kampf(
    "Das Projekt",
    gegner_1="aufsicht",
    gegner_2="hausmeister",
    belohnung=350,
    ki=3,
    npc_level=6,
    team_groesse=2,

    story_vorher=[
        ("Direktor", "Offiziell ging es um die Förderung bestimmter Schüler."),
        ("Jakob", "Und inoffiziell?"),
        ("Direktor", "Das weiß ich nicht."),
        ("Jakob", "Was wurde gemacht?"),
        ("Direktor", "Es wurden Daten gesammelt."),
        ("Jakob", "Welche Daten?"),
        ("Direktor", "Leistungen. Verhalten. Kontakte."),
        ("Jakob", "Also wurden Schüler beobachtet..."),
        ("Direktor", "Offenbar.")
    ],

    story_nachher=[
        ("Jakob", "Und wie hieß dieses Projekt?"),
        ("Direktor", "Ich erinnere mich nur an einen Namen."),
        ("Jakob", "Welchen?"),
        ("Direktor", "Projekt K."),
        ("Jakob", "Projekt K?")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 7 – Jemand weiß Bescheid
# ══════════════════════════════════════════════════════════════

kampf_7_4 = kampangen_kampf(
    "Jemand weiß Bescheid",
    gegner_1="hausmeister",
    gegner_2="direktor",
    gegner_3="klassenclown",
    belohnung=450,
    ki=3,
    npc_level=7,
    team_groesse=3,

    story_vorher=[
        ("Jakob", "Nach dem Stromausfall fehlt eine Akte."),
        ("Direktor", "Jemand muss hier gewesen sein."),
        ("Jakob", "Da liegt ein Zettel."),
        ("Jakob", "Was steht da?"),
        ("Jakob", "Ihr hättet die Liste nicht finden dürfen."),
        ("Direktor", "Das ist nicht gut."),
        ("Jakob", "Darunter steht eine Adresse."),
        ("Direktor", "Das ist keine Adresse hier an der Schule."),
        ("Jakob", "Dann weiß ich, wo wir als Nächstes hingehen.")
    ],

    story_nachher=[
        ("Jakob", "Die Person wusste, dass wir die Liste gefunden haben."),
        ("Direktor", "Dann weiß sie auch, dass wir ihr auf der Spur sind."),
        ("Jakob", "Umso besser.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 8 – Die Adresse
# ══════════════════════════════════════════════════════════════

kampf_8_4 = kampangen_kampf(
    "Die Adresse",
    gegner_1="starker_6_klaessler",
    gegner_2="cooler_6_klaessler",
    belohnung=500,
    ki=3,
    npc_level=8,
    team_groesse=2,

    story_vorher=[
        ("Jakob", "Das soll also die Adresse sein."),
        ("Direktor", "Sieht ziemlich verlassen aus."),
        ("Jakob", "Da vorne ist eine Tür."),
        ("Direktor", "Warte."),
        ("Jakob", "Was?"),
        ("Direktor", "Da sind Unterlagen."),
        ("Jakob", "Und auf denen steht wieder Projekt K."),
        ("Jakob", "Dann sind wir hier richtig.")
    ],

    story_nachher=[
        ("Jakob", "Hier steht etwas über die Liste."),
        ("Direktor", "Was?"),
        ("Jakob", "Status: aktiv."),
        ("Direktor", "Dann ist das Projekt noch nicht beendet.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 9 – Priorität 1
# ══════════════════════════════════════════════════════════════

kampf_9_4 = kampangen_kampf(
    "Priorität 1",
    gegner_1="hausmeister",
    gegner_2="klassenclown",
    gegner_3="cooler_6_klaessler",
    belohnung=600,
    ki=3,
    npc_level=9,
    team_groesse=3,

    story_vorher=[
        ("Jakob", "Hier ist eine aktuelle Akte."),
        ("Jakob", "Zielperson: Jakob."),
        ("Jakob", "Priorität: 1."),
        ("Direktor", "Was bedeutet das?"),
        ("Jakob", "Keine Ahnung."),
        ("Jakob", "Aber hier steht noch etwas."),
        ("Jakob", "Phase 2 beginnt nach Kontakt mit der Zielperson."),
        ("Direktor", "Phase 2?"),
        ("???", "Du solltest diese Akte nicht lesen.")
    ],

    story_nachher=[
        ("Jakob", "Wer bist du?"),
        ("Unbekannter", "Jemand, der für andere arbeitet."),
        ("Jakob", "Für wen?"),
        ("Unbekannter", "Das wirst du noch früh genug herausfinden."),
        ("Jakob", "Das glaube ich kaum.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 10 – Phase 2
# ══════════════════════════════════════════════════════════════

kampf_10_4 = kampangen_kampf(
    "Phase 2",
    gegner_1="aufsicht",
    gegner_2="hausmeister",
    gegner_3="cooler_6_klaessler",
    gegner_4="starker_6_klaessler",
    belohnung=1000,
    ki=4,
    npc_level=10,
    team_groesse=4,

    story_vorher=[
        ("Jakob", "Ihr wisst beide mehr, als ihr mir erzählt."),
        ("Direktor", "Jakob..."),
        ("Jakob", "Was ist Projekt K?"),
        ("Hausmeister", "Das solltest du nicht wissen."),
        ("Jakob", "Warum steht mein Name auf der Liste?"),
        ("Direktor", "Das wissen wir selbst nicht vollständig."),
        ("Jakob", "Dann werde ich es eben herausfinden."),
        ("Hausmeister", "Du verstehst nicht, womit du dich anlegst.")
    ],

    story_nachher=[
        ("Jakob", "Jetzt habe ich endlich Antworten."),
        ("Direktor", "Nein."),
        ("Jakob", "Was?"),
        ("Direktor", "Du hast nur angefangen, die richtigen Fragen zu stellen."),
        ("Jakob", "..."),
        ("Jakob", "Was soll das heißen?"),
        ("Direktor", "Das Projekt ist größer, als du denkst."),
        ("Jakob", "Dann war das hier also nur der Anfang."),
        ("Direktor", "Ja."),
        ("Jakob", "Dann finde ich den Rest auch noch heraus.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampagne erstellen
# ══════════════════════════════════════════════════════════════

Kampange_4 = kampange(
    "_04",
    "Die Liste (Nachfolge Kampange zu _03)",
    "schwer",
    10,
    [
        kampf_1_4,
        kampf_2_4,
        kampf_3_4,
        kampf_4_4,
        kampf_5_4,
        kampf_6_4,
        kampf_7_4,
        kampf_8_4,
        kampf_9_4,
        kampf_10_4
    ],
    fortschritt=0
)




# ══════════════════════════════════════════════════════════════
# Kampange_5
# Projekt K
# ══════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════
# Kampf 1 – Die Akte
# ══════════════════════════════════════════════════════════════

kampf_1_5 = kampangen_kampf(
    "Die Akte",
    gegner_1="normaler_6_klaessler",
    gegner_2="schlauer_6_klaessler",
    belohnung=100,
    ki=1,
    npc_level=5,
    team_groesse=2,

    story_vorher=[
        ("Jakob", "Also gut. Dann schauen wir uns diese Akte einmal genauer an."),
        ("Direktor", "Was steht darin?"),
        ("Jakob", "Eine Menge Informationen."),
        ("Jakob", "Und hier ist wieder dieses K."),
        ("Direktor", "Projekt K."),
        ("Jakob", "Genau."),
        ("Jakob", "Aber was bedeutet die Nummer daneben?"),
        ("Direktor", "Welche Nummer?"),
        ("Jakob", "K-001."),
        ("Jakob", "Und hier gibt es K-002, K-003 und noch viele weitere.")
    ],

    story_nachher=[
        ("Jakob", "Insgesamt gibt es siebzehn Akten."),
        ("Direktor", "Siebzehn?"),
        ("Jakob", "Ja."),
        ("Jakob", "Und ich bin K-001."),
        ("Jakob", "Ich will wissen, wer die anderen sind.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 2 – K-002
# ══════════════════════════════════════════════════════════════

kampf_2_5 = kampangen_kampf(
    "K-002",
    gegner_1="aggressiver_6_klaessler",
    gegner_2="normaler_6_klaessler",
    belohnung=150,
    ki=2,
    npc_level=5,
    team_groesse=2,

    story_vorher=[
        ("Jakob", "Eine der Akten ist noch nicht vollständig zerstört."),
        ("Jakob", "Hier steht ein Name."),
        ("Direktor", "Kennst du ihn?"),
        ("Jakob", "Ich glaube schon."),
        ("Jakob", "Das war ein ehemaliger Schüler."),
        ("Direktor", "Ja."),
        ("Jakob", "Was ist mit ihm passiert?"),
        ("Direktor", "Er hat die Schule vor Jahren verlassen."),
        ("Jakob", "Laut dieser Akte ist er verschwunden.")
    ],

    story_nachher=[
        ("Jakob", "Was bedeutet 'Status: unbekannt'?"),
        ("Direktor", "Ich weiß es nicht."),
        ("Jakob", "Dann müssen wir herausfinden, was mit den anderen passiert ist.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 3 – Die verschwundenen Schüler
# ══════════════════════════════════════════════════════════════

kampf_3_5 = kampangen_kampf(
    "Die verschwundenen Schüler",
    gegner_1="nerviger_6_klaessler",
    gegner_2="cooler_6_klaessler",
    gegner_3="normaler_6_klaessler",
    belohnung=200,
    ki=2,
    npc_level=6,
    team_groesse=3,

    story_vorher=[
        ("Jakob", "Wir sollten die Namen aus den Akten überprüfen."),
        ("Direktor", "Ich habe einige alte Schülerlisten gefunden."),
        ("Jakob", "Und?"),
        ("Direktor", "Mehrere Namen stimmen überein."),
        ("Jakob", "Was steht bei ihnen?"),
        ("Direktor", "Bei einigen steht 'unbekannt'."),
        ("Jakob", "Und bei den anderen?"),
        ("Direktor", "Bei einigen steht 'abgeschlossen'."),
        ("Jakob", "Abgeschlossen?")
    ],

    story_nachher=[
        ("Jakob", "Was soll das bedeuten?"),
        ("Direktor", "Das weiß ich nicht."),
        ("Jakob", "Dann finden wir es eben heraus.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 4 – Der erste Versuch
# ══════════════════════════════════════════════════════════════

kampf_4_5 = kampangen_kampf(
    "Der erste Versuch",
    gegner_1="starker_6_klaessler",
    gegner_2="schlauer_6_klaessler",
    belohnung=250,
    ki=2,
    npc_level=7,
    team_groesse=2,

    story_vorher=[
        ("Jakob", "Hier ist eine weitere Akte."),
        ("Jakob", "K-001."),
        ("Direktor", "Deine Akte?"),
        ("Jakob", "Ja."),
        ("Jakob", "Hier stehen Dinge, an die ich mich überhaupt nicht erinnere."),
        ("Direktor", "Was genau?"),
        ("Jakob", "Ereignisse aus meiner Kindheit."),
        ("Jakob", "Und hier steht: 'Subjekt zeigt erwartete Reaktion.'"),
        ("Direktor", "Das ist ungewöhnlich.")
    ],

    story_nachher=[
        ("Jakob", "Woher konnten die Leute hinter diesem Projekt das alles wissen?"),
        ("Direktor", "Ich weiß es nicht."),
        ("Jakob", "Du weißt mehr, als du sagst.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 5 – Der Name
# ══════════════════════════════════════════════════════════════

kampf_5_5 = kampangen_kampf(
    "Der Name",
    gegner_1="aufsicht",
    gegner_2="hausmeister",
    belohnung=300,
    ki=3,
    npc_level=8,
    team_groesse=2,

    story_vorher=[
        ("Jakob", "Wir müssen jemanden finden, der etwas über Projekt K weiß."),
        ("Direktor", "Es gibt eine ehemalige Mitarbeiterin."),
        ("Jakob", "Und sie weiß etwas?"),
        ("Direktor", "Vielleicht."),
        ("Jakob", "Dann sollten wir sie fragen."),
        ("Direktor", "Sie wird wahrscheinlich nicht freiwillig reden."),
        ("Jakob", "Dann überzeugen wir sie eben.")
    ],

    story_nachher=[
        ("Jakob", "Also? Wer hat Projekt K gestartet?"),
        ("Mitarbeiterin", "Nicht die Schule."),
        ("Jakob", "Was?"),
        ("Mitarbeiterin", "Die Schule wurde nur benutzt."),
        ("Jakob", "Von wem?"),
        ("Mitarbeiterin", "Kronos.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 6 – Kronos
# ══════════════════════════════════════════════════════════════

kampf_6_5 = kampangen_kampf(
    "Kronos",
    gegner_1="hausmeister",
    gegner_2="aufsicht",
    gegner_3="klassenclown",
    belohnung=350,
    ki=3,
    npc_level=9,
    team_groesse=3,

    story_vorher=[
        ("Jakob", "Kronos."),
        ("Direktor", "Ja."),
        ("Jakob", "Was ist das?"),
        ("Direktor", "Eine Organisation."),
        ("Jakob", "Existiert sie noch?"),
        ("Direktor", "Offiziell nicht."),
        ("Jakob", "Und Projekt K?"),
        ("Direktor", "Das ist die Frage."),
        ("Jakob", "Dann suchen wir weiter.")
    ],

    story_nachher=[
        ("Jakob", "Hier ist ein alter Computer."),
        ("Direktor", "Vielleicht finden wir darauf etwas."),
        ("Jakob", "Er ist passwortgeschützt."),
        ("Jakob", "Aber die Dateien sind noch da.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 7 – Eignung
# ══════════════════════════════════════════════════════════════

kampf_7_5 = kampangen_kampf(
    "Eignung",
    gegner_1="starker_6_klaessler",
    gegner_2="cooler_6_klaessler",
    gegner_3="aggressiver_6_klaessler",
    belohnung=450,
    ki=3,
    npc_level=10,
    team_groesse=3,

    story_vorher=[
        ("Jakob", "Ich habe die Dateien geöffnet."),
        ("Direktor", "Was steht darin?"),
        ("Jakob", "Informationen über die siebzehn Personen."),
        ("Direktor", "Und bei jeder gibt es eine Kategorie."),
        ("Jakob", "Eignung."),
        ("Direktor", "Eignung wofür?"),
        ("Jakob", "Keine Ahnung."),
        ("Jakob", "Ich öffne meine Akte.")
    ],

    story_nachher=[
        ("Jakob", "K-001."),
        ("Jakob", "Eignung: AUSGEZEICHNET."),
        ("Direktor", "Was bedeutet das?"),
        ("Jakob", "Hier steht noch mehr."),
        ("Jakob", "Phase 1: abgeschlossen."),
        ("Jakob", "Phase 2: abgeschlossen."),
        ("Jakob", "Phase 3: ausstehend.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 8 – Phase 3
# ══════════════════════════════════════════════════════════════

kampf_8_5 = kampangen_kampf(
    "Phase 3",
    gegner_1="hausmeister",
    gegner_2="direktor",
    belohnung=500,
    ki=3,
    npc_level=11,
    team_groesse=2,

    story_vorher=[
        ("Jakob", "Was ist Phase 3?"),
        ("Direktor", "Das weiß ich nicht."),
        ("Jakob", "Aber meine Akte sagt etwas anderes."),
        ("Direktor", "Jakob..."),
        ("Jakob", "Nur bestimmte Zielpersonen kommen in Phase 3."),
        ("Jakob", "Und ich bin eine davon."),
        ("Direktor", "Du solltest damit aufhören."),
        ("Jakob", "Warum?")
    ],

    story_nachher=[
        ("Jakob", "Ich habe eine Nachricht bekommen."),
        ("Direktor", "Von wem?"),
        ("Jakob", "Keine Ahnung."),
        ("Jakob", "Darin steht eine Adresse."),
        ("Direktor", "Dann wissen wir, wo wir als Nächstes suchen müssen.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 9 – Die Wahrheit
# ══════════════════════════════════════════════════════════════

kampf_9_5 = kampangen_kampf(
    "Die Wahrheit",
    gegner_1="klassenclown",
    gegner_2="cooler_6_klaessler",
    gegner_3="starker_6_klaessler",
    belohnung=600,
    ki=4,
    npc_level=12,
    team_groesse=3,

    story_vorher=[
        ("Jakob", "Das ist also der Ort."),
        ("Direktor", "Sieht verlassen aus."),
        ("Jakob", "Hier unten ist ein Raum."),
        ("Jakob", "Und dort sind die alten Unterlagen."),
        ("Direktor", "Was steht in der Akte?"),
        ("Jakob", "K-001."),
        ("Jakob", "Hier steht, dass ich bereits vor meiner Einschulung aufgenommen wurde."),
        ("Direktor", "..."),
        ("Jakob", "Du wusstest davon.")
    ],

    story_nachher=[
        ("Jakob", "Hier steht noch etwas."),
        ("Jakob", "Verantwortlich: [GESCHWÄRZT]."),
        ("Direktor", "Jakob..."),
        ("Jakob", "Und darunter steht etwas handgeschrieben."),
        ("Jakob", "Er darf niemals erfahren, wer ihn ausgewählt hat.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampf 10 – K-001
# ══════════════════════════════════════════════════════════════

kampf_10_5 = kampangen_kampf(
    "K-001",
    gegner_1="direktor",
    gegner_2="hausmeister",
    gegner_3="cooler_6_klaessler",
    gegner_4="starker_6_klaessler",
    belohnung=1000,
    ki=4,
    npc_level=13,
    team_groesse=4,

    story_vorher=[
        ("Jakob", "Also gut."),
        ("Jakob", "Dann öffne ich die letzte Seite."),
        ("Direktor", "Warte."),
        ("Jakob", "Nein."),
        ("Jakob", "Ich will endlich wissen, was hier passiert."),
        ("Jakob", "PROJEKT K."),
        ("Jakob", "SUBJEKT: K-001."),
        ("Jakob", "NAME: JAKOB."),
        ("Jakob", "STATUS: AKTIV."),
        ("Jakob", "AUFNAHME: VOR SCHULEINTRITT."),
        ("Jakob", "PHASE 3: FREIGEGEBEN.")
    ],

    story_nachher=[
        ("Jakob", "Du wusstest davon?"),
        ("Direktor", "Nicht alles."),
        ("Jakob", "Aber du wusstest, dass mein Name schon einmal gefallen ist."),
        ("Direktor", "Ja."),
        ("Jakob", "Wer hat mich ausgewählt?"),
        ("Direktor", "Das weiß ich nicht."),
        ("Jakob", "Dann finde ich es heraus."),
        ("Jakob", "Was ist das?"),
        ("Direktor", "Was?"),
        ("Jakob", "Der Bildschirm."),
        ("Jakob", "PROJEKT K."),
        ("Jakob", "PHASE 3: AKTIV."),
        ("Jakob", "K-001: BESTÄTIGT."),
        ("Jakob", "..."),
        ("Jakob", "Das reicht für heute."),
        ("Jakob", "Die Sache mit Projekt K ist hiermit beendet.")
    ]
)


# ══════════════════════════════════════════════════════════════
# Kampagne erstellen
# ══════════════════════════════════════════════════════════════

Kampange_5 = kampange(
    "_05",
    "Projekt K (Nachfolge Kampange zu _04)",
    "sehr schwer",
    10,
    [
        kampf_1_5,
        kampf_2_5,
        kampf_3_5,
        kampf_4_5,
        kampf_5_5,
        kampf_6_5,
        kampf_7_5,
        kampf_8_5,
        kampf_9_5,
        kampf_10_5
    ],
    fortschritt=0
)








# ══════════════════════════════════════════════════════════════


# Kampagne 6


# ══════════════════════════════════════════════════════════════


anfangsstory_6 = kampangen_kampf( #1
    "Anfangsstory",

    story_vorher=[
        ("Erzähler", "Frankfurt, Deutschland - Jahr 2025"),
        ("Erzähler", "Es war ein gewöhnlicher Tag bei der Flugsicherung."),
        ("Adam", "Noch ein ruhiger Tag..."),
        ("Erzähler", "Zumindest dachte Adam das."),
        ("Erzähler", "Plötzlich begannen mehrere Radarsysteme gleichzeitig zu flackern."),
        ("Adam", "Was ist das denn?"),
        ("Erzähler", "Ein unbekanntes Objekt war auf dem Radar erschienen."),
        ("Adam", "Das kann kein Flugzeug sein."),
        ("Erzähler", "Wenige Sekunden später wurde aus dem unbekannten Kontakt eine Katastrophe."),
        ("Erzähler", "Das Objekt raste auf den Flughafen zu."),
        ("Adam", "Alle weg von den Landebahnen!"),
        ("Erzähler", "Dann schlug es ein."),
        ("", ""),
        ("Erzähler", "Das Militär hatte das gesamte Gebiet abgesperrt."),
        ("Erzähler", "Niemand wusste genau, was auf einer der Start- und Landebahnen lag."),
        ("", ""),
        ("John", "Also gut. Was wissen wir bisher?"),
        ("Sara", "Nicht viel. Es sieht aus wie ein Asteroid."),
        ("Lara", "Ein Asteroid mit Triebwerken."),
        ("Rico", "Das macht die Sache doch interessant."),
        ("John", "Wir untersuchen es. Keine Alleingänge."),
        ("Rico", "Ja, ja. Schon verstanden.")
    ],

    ist_kampf=False
)


Die_Erkundung_6 = kampangen_kampf( #2
    "Die Erkundung",

    story_vorher=[
        ("Erzähler", "Das Gebiet um die Absturzstelle war vollständig vom Militär abgeriegelt worden."),
        ("Erzähler", "Nur ein kleines Team durfte sich dem unbekannten Objekt nähern."),
        ("Erzähler", "John, Sara, Rico und Lara machten sich gemeinsam auf den Weg."),
        ("", ""),
        ("John", "Bleibt zusammen. Wir wissen nicht, womit wir es hier zu tun haben."),
        ("Rico", "Sieht wirklich aus wie ein riesiger Stein."),
        ("Sara", "Ein riesiger Stein mit Triebwerken."),
        ("Lara", "Und wir wissen immer noch nicht, warum er überhaupt hier gelandet ist."),
        ("", ""),
        ("Erzähler", "Das Team umrundete das Objekt und untersuchte seine Oberfläche."),
        ("", ""),
        ("Rico", "Wartet mal."),
        ("Erzähler", "An der Seite des vermeintlichen Asteroiden befand sich eine kleine Einbuchtung."),
        ("Rico", "Da ist etwas."),
        ("John", "Nicht anfassen."),
        ("Erzähler", "Rico hatte bereits einen kleinen Knopf entdeckt."),
        ("John", "Warte kurz. Öffne erst, wenn wir in Position sind."),
        ("", ""),
        ("Erzähler", "Das Team nahm vorsichtig Abstand und machte sich bereit."),
        ("", ""),
        ("Rico", "Na dann..."),
        ("Erzähler", "Rico betätigte den Knopf."),
        ("Erzähler", "Ein Zischen ertönte."),
        ("Erzähler", "Dann öffnete sich wie aus dem Nichts eine Tür im Gestein.")
    ],

    ist_kampf=False
)


Im_Inneren_6 = kampangen_kampf( #3
    "Im Inneren",

    story_vorher=[
        ("Erzähler", "Hinter der Tür befand sich kein gewöhnlicher Raum."),
        ("Erzähler", "Ein schmaler Gang führte tief in das unbekannte Objekt hinein."),
        ("", ""),
        ("Sara", "Das ist definitiv kein Asteroid."),
        ("Lara", "Die Wände sehen aus, als wären sie aus Metall."),
        ("Rico", "Und trotzdem ist das Ding mitten auf der Landebahn eingeschlagen."),
        ("John", "Konzentriert bleiben. Wir wissen immer noch nicht, was das hier ist."),
        ("", ""),
        ("Erzähler", "Das Team bewegte sich langsam durch den Gang."),
        ("Erzähler", "Nach einigen Metern öffnete sich der Gang zu einem größeren Raum."),
        ("", ""),
        ("Sara", "Was zum...?"),
        ("Erzähler", "Überall an den Wänden befanden sich unbekannte technische Anlagen."),
        ("Lara", "Das sieht aus wie eine Art Kontrollraum."),
        ("Rico", "Dann sollten wir vielleicht herausfinden, was damit passiert ist."),
        ("John", "Vorsichtig."),
        ("", ""),
        ("Erzähler", "In der Mitte des Raumes befand sich eine große Konsole."),
        ("Erzähler", "Mehrere Anzeigen waren noch aktiv."),
        ("", ""),
        ("John", "Ich sehe mir die Konsole an."),
        ("Erzähler", "Während John die Anzeigen untersuchte, bemerkte Sara etwas an der gegenüberliegenden Wand."),
        ("", ""),
        ("Sara", "Leute... kommt mal her."),
        ("Erzähler", "Auf dem Boden lagen mehrere verweste menschliche Körper."),
        ("Lara", "Die sind schon länger hier."),
        ("Rico", "Was ist hier passiert?"),
        ("Erzähler", "Niemand antwortete."),
        ("Erzähler", "An einer der Wände waren tiefe Kratzspuren zu sehen.")
    ],

    ist_kampf=False
)


Die_Untersuchungen_6 = kampangen_kampf( #4
    "Die Untersuchungen",

    story_vorher=[
        ("Erzähler", "Das Team begann damit, den unbekannten Raum genauer zu untersuchen."),
        ("", ""),
        ("Erzähler", "John ging zur großen Konsole in der Mitte des Raumes."),
        ("John", "Ich sehe mal, ob ich hier irgendwelche Daten finde."),
        ("", ""),
        ("Erzähler", "Während John die Anzeigen untersuchte, teilten sich Sara, Lara und Rico auf."),
        ("", ""),
        ("Erzähler", "Sara und Lara untersuchten die Leichen."),
        ("Lara", "Die Verletzungen sehen merkwürdig aus."),
        ("Sara", "Das sind keine normalen Schussverletzungen."),
        ("Lara", "Und auch keine Verletzungen, wie man sie von einem einfachen Aufprall erwarten würde."),
        ("Sara", "Ich kann nicht sagen, was das verursacht hat."),
        ("", ""),
        ("Erzähler", "Rico untersuchte währenddessen die Kratzspuren an den Wänden."),
        ("Rico", "Die Spuren sind ziemlich tief."),
        ("Erzähler", "Neben den Kratzern waren dunkle Blutspuren an der Wand zu erkennen."),
        ("Rico", "Hier ist definitiv etwas passiert."),
        ("", ""),
        ("Erzähler", "John arbeitete weiter an der Konsole."),
        ("John", "Ich glaube, ich kann einige Dateien retten."),
        ("Erzähler", "Nach einigen Minuten gelang es ihm, mehrere Dateien auf einen Speicher zu kopieren."),
        ("John", "Ich hab ein paar Dateien."),
        ("Rico", "Und? Steht da irgendwas Brauchbares drin?"),
        ("John", "Keine Ahnung. Das sehen wir uns später an."),
        ("", ""),
        ("Erzähler", "Das Team untersuchte den Raum noch einige Minuten."),
        ("Erzähler", "Doch außer den Leichen, den Kratzspuren und den Dateien fanden sie zunächst nichts weiter."),
        ("", ""),
        ("Erzähler", "Plötzlich ertönte ein leises Geräusch."),
        ("Sara", "Habt ihr das gehört?"),
        ("John", "Alle stehen bleiben."),
        ("", ""),
        ("Erzähler", "Das Team hielt inne."),
        ("Erzähler", "Für einige Sekunden war nichts zu hören."),
        ("", ""),
        ("Rico", "Vielleicht war es nur irgendwas von der Konsole."),
        ("Lara", "Ich glaube nicht."),
        ("", ""),
        ("Erzähler", "Dann ertönte das Geräusch erneut."),
        ("Erzähler", "Diesmal deutlich näher."),
        ("", ""),
        ("John", "Zurück zur Tür."),
        ("Erzähler", "Das Team bewegte sich langsam zurück."),
        ("", ""),
        ("Erzähler", "Plötzlich flackerte eine der Anzeigen an der Wand auf."),
        ("Erzähler", "Ein mechanisches Geräusch ertönte."),
        ("", ""),
        ("Rico", "Was zum...?"),
        ("Erzähler", "Aus einer Wandöffnung bewegte sich eine kleine metallische Drohne."),
        ("", ""),
        ("Sara", "Kontakt!"),
        ("John", "Zurück!"),
        ("Erzähler", "Die Drohne richtete sich auf das Team aus.")
    ],

    ist_kampf=True,

    spieler_1="John",
    spieler_2="Sara",
    spieler_3="Rico",

    gegner_1="mars_sicherheitsdrohne",

    team_groesse_1=3,
    team_groesse_2=1,

    belohnung=100,
    ki=3,
    npc_level=6,

    story_nachher=[
        ("Erzähler", "Die Drohne lag reglos auf dem Boden."),
        ("", ""),
        ("Rico", "Was war das denn bitte?"),
        ("Sara", "Keine Ahnung. Aber sie wollte uns offensichtlich nicht gehen lassen."),
        ("Lara", "Vielleicht war das einfach eine Art Sicherheitssystem."),
        ("John", "Möglich. Ist jetzt auch egal."),
        ("", ""),
        ("Erzähler", "John nahm den Speicher mit den geretteten Dateien an sich."),
        ("John", "Wir haben, was wir brauchen. Raus hier."),
        ("", ""),
        ("Erzähler", "Das Team machte sich gemeinsam auf den Weg zurück zum Ausgang."),
        ("Erzähler", "Niemand sprach mehr über die Drohne.")
    ]
)


Rueckkehr_6 = kampangen_kampf( #5
    "Die Rückkehr",

    story_vorher=[
        ("Erzähler", "Das Team machte sich gemeinsam auf den Weg zurück zum Ausgang."),
        ("Erzähler", "Nach einigen Minuten erreichten sie wieder die Oberfläche."),
        ("Erzähler", "Vor dem Objekt warteten bereits Chasker und mehrere bewaffnete Soldaten."),
        ("", ""),
        ("Chasker", "Da seid ihr ja endlich."),
        ("John", "Wir haben ein paar Dateien gefunden."),
        ("Chasker", "Ein paar Dateien?"),
        ("John", "Ja. Wir erklären alles, sobald wir zurück sind."),
        ("", ""),
        ("Chasker", "Wie lange wart ihr da drin?"),
        ("John", "Keine Ahnung. Vielleicht eine Stunde?"),
        ("Chasker", "Eine Stunde?"),
        ("John", "Ungefähr."),
        ("Chasker", "Ihr wart fast vier Stunden dort drin."),
        ("", ""),
        ("Rico", "Was?"),
        ("Sara", "Das kann nicht sein."),
        ("Chasker", "Meine Uhr sagt etwas anderes."),
        ("", ""),
        ("Erzähler", "Die Gruppe sah Chasker verwirrt an."),
        ("Erzähler", "Niemand sagte etwas."),
        ("", ""),
        ("Chasker", "Dann sollten wir das später klären."),
        ("", ""),
        ("John", "Wir hatten dort drin noch ein anderes Problem."),
        ("Chasker", "Was für ein Problem?"),
        ("John", "Eine Drohne."),
        ("Chasker", "Eine Drohne?"),
        ("Rico", "Ja. Kam einfach aus einer Wand."),
        ("Lara", "Sie hat uns angegriffen."),
        ("John", "Wir haben sie ausgeschaltet."),
        ("Chasker", "Gut. Wir kümmern uns später darum."),
        ("", ""),
        ("Erzähler", "Chasker deutete auf den schnell errichteten Stützpunkt."),
        ("Chasker", "Kommt. Wir müssen uns ansehen, was ihr gefunden habt."),
        ("", ""),
        ("Erzähler", "Das Team folgte Chasker zurück zum provisorischen Stützpunkt.")
    ],

    ist_kampf=False
)


Die_Sitzung_6 = kampangen_kampf( #6
    "Die Sitzung",

    story_vorher=[
        ("Erzähler", "Anschließend gingen sie in Chaskers Büro, um mit ihm und ein paar hochrangigen Offizieren über das zu sprechen, was sie gesehen hatten."),
        ("", ""),
        ("Erzähler", "Als Erstes erzählten sie von den Leichen, den Kratzern und den Blutspuren an den Wänden."),
        ("Erzähler", "Sie erzählten auch, dass die Verletzungen keine einfachen Schuss- oder Stoßwunden waren, sondern anders aussahen."),
        ("", ""),
        ("John", "Wir konnten selbst nicht genau sagen, was diese Verletzungen verursacht hat."),
        ("", ""),
        ("Erzähler", "Anschließend zeigte John ihnen die Dateien, die er retten konnte."),
        ("Erzähler", "Eine Datei hieß „Tagebuch“ und beinhaltete nur Text."),
        ("Erzähler", "Der größte Teil des Textes war jedoch vollkommen unleserlich."),
        ("", ""),
        ("John", "Das hier ist die Datei."),
        ("John", "Ich weiß nicht, ob wir damit viel anfangen können."),
        ("", ""),
        ("Erzähler", "John zeigte ihnen den Inhalt der Datei."),
        ("", ""),
        ("Rico", "Das war ja sehr aufschlussreich."),
        ("Erzähler", "Rico murmelte die Worte genervt vor sich hin."),
        ("", ""),
        ("Erzähler", "Doch dann zeigte John ihnen eine zweite Datei."),
        ("Erzähler", "Auch sie beinhaltete hauptsächlich Text, doch diesmal trug die Datei einen eindeutigen Titel."),
        ("", ""),
        ("Erzähler", "Die Datei hieß: „Was ihr wissen müsst“."),
        ("", ""),
        ("Erzähler", "John öffnete die Datei und begann vorzulesen."),
        ("", ""),
        ("John", "Hallo John, Sara, Lara und Rico."),
        ("John", "Falls ihr das lest, ist unser Shuttle hoffentlich sicher mit Efa und den anderen angekommen, also werdet ihr das Meiste wahrscheinlich schon wissen."),
        ("John", "Die Dateien für den Antrieb für den Flug zu eurem Planeten Mars liegen im Ordner Dateien bei."),
        ("John", "Wir brauchen eure Hilfe!"),
        ("", ""),
        ("Erzähler", "Für einen kurzen Moment sagte niemand etwas."),
        ("Erzähler", "Dann brach im Raum völliges Durcheinander aus."),
        ("Erzähler", "Mehrere der Anwesenden begannen gleichzeitig zu reden."),
        ("Erzähler", "Nur einzelne Wörter wie „Namen“, „Andere“, „Warum“ und „Mars“ waren zu verstehen."),
        ("", ""),
        ("Chasker", "Ruhe!!"),
        ("", ""),
        ("Erzähler", "Nach kurzer Zeit beruhigte sich der Raum wieder."),
        ("", ""),
        ("Chasker", "So, wir machen das jetzt wie in der Schule."),
        ("Chasker", "Wer etwas sagen will, meldet sich und wartet, bis er drangenommen wird."),
        ("", ""),
        ("Chasker", "Wir haben jetzt mehrere Fragen."),
        ("Chasker", "Die erste ist: Warum kannten „Die“ die Namen von John und seinem Team?"),
        ("Chasker", "Die zweite ist: Was ist mit Efa und den anderen passiert?"),
        ("Chasker", "Und die letzte: Wo sind die Dateien für den Antrieb?"),
        ("", ""),
        ("Chasker", "Hat jemand eine Antwort auf eine dieser Fragen?"),
        ("", ""),
        ("Erzähler", "Nur John meldete sich."),
        ("", ""),
        ("Chasker", "Ja?"),
        ("", ""),
        ("John", "Ich habe die Dateien für den Antrieb noch auf dem Speicher."),
        ("John", "Sie waren dort in einer kleinen und unscheinbaren Armatur in der Nähe des Hauptterminals."),
        ("", ""),
        ("Chasker", "Perfekt. Dann haben wir ja jetzt nur noch zwei Fragen."),
        ("Chasker", "Hat irgendjemand noch eine Idee oder Antwort?"),
        ("", ""),
        ("Erzähler", "Alle schwiegen."),
        ("", ""),
        ("Chasker", "Okay. Dann treffen wir uns morgen wieder."),
        ("", ""),
        ("Erzähler", "Damit beendete Chasker die Sitzung."),
        ("Erzähler", "Die anderen verließen nach und nach den Raum."),
        ("Erzähler", "John blieb noch einen Moment länger am Fenster stehen."),
        ("", ""),
        ("Erzähler", "Von dort aus konnte er beobachten, wie die Leichensäcke verladen wurden."),
        ("Erzähler", "Einer davon bewegte sich."),
        ("Erzähler", "Zuerst war es nur ein kleines Zucken, kaum mehr als ein Flattern."),
        ("Erzähler", "Dann wölbte sich der Sack, als würde darunter jemand nach Luft schnappen."),
        ("", ""),
        ("Erzähler", "Johns Herz schlug schneller."),
        ("Erzähler", "Sein Atem stockte."),
        ("", ""),
        ("Erzähler", "Für einen Augenblick glaubte er, eine nicht menschliche Hand durch den Stoff zu sehen."),
        ("Erzähler", "Sie sah zu lang und seltsam verdreht aus."),
        ("", ""),
        ("Erzähler", "John rieb sich die Augen."),
        ("Erzähler", "Als er wieder hinsah, lag alles still."),
        ("", ""),
        ("Erzähler", "Die Türen des Transporters schlossen sich."),
        ("Erzähler", "John schwieg."),
        ("", ""),
        ("Erzähler", "Als John nach Hause kam, machte er sich erstmal Nudeln mit Tomatensoße und setzte sich auf das Sofa."),
        ("Erzähler", "Doch während er aß, musste er immer wieder an den Asteroiden und an den Leichensack denken."),
        ("", ""),
        ("Erzähler", "Um sich abzulenken, versuchte er fernzusehen."),
        ("Erzähler", "Doch auch das hatte nicht die Wirkung, die er sich erhofft hatte."),
        ("", ""),
        ("Erzähler", "Nach einer Weile überlegte John, Sara anzurufen, um ihr seine Erkenntnisse zu erzählen."),
        ("Erzähler", "Doch letztlich entschied er sich dagegen."),
        ("Erzähler", "Er befürchtete, von der Mission ausgeschlossen zu werden, wenn er erzählte, dass er einen sich bewegenden Leichensack gesehen hatte."),
        ("Erzähler", "Vielleicht war er einfach nur überarbeitet."),
        ("", ""),
        ("Erzähler", "Schließlich ging John schlafen.")
    ],

    ist_kampf=False
)


Der_Traum_6_begin = kampangen_kampf( #7
    "Der Traum",

    story_vorher=[
        ("Erzähler", "John stand plötzlich wieder im Inneren des unbekannten Objekts."),
        ("Erzähler", "Sara, Lara und Rico waren ebenfalls bei ihm."),
        ("", ""),
        ("John", "Ich habe noch drei Dateien gefunden."),
        ("John", "Ich lade sie noch schnell herunter und dann verschwinden wir hier."),
        ("", ""),
        ("Rico", "Gute Idee. Ich habe keine Lust, diesem Ding noch länger Gesellschaft zu leisten."),
        ("", ""),
        ("Erzähler", "John ging zurück zur Konsole."),
        ("Erzähler", "Auf dem Bildschirm waren noch mehrere Dateien zu sehen."),
        ("", ""),
        ("John", "Einen Moment..."),
        ("Erzähler", "John begann, die Dateien auf den Speicher zu übertragen."),
        ("", ""),
        ("Sara", "Wie lange dauert das noch?"),
        ("John", "Nicht mehr lange."),
        ("", ""),
        ("Erzähler", "Während die Dateien übertragen wurden, sah sich Lara noch einmal im Raum um."),
        ("Erzähler", "Rico stand einige Meter entfernt und beobachtete die Tür."),
        ("", ""),
        ("Erzähler", "Schließlich erschien auf dem Bildschirm eine Meldung."),
        ("John", "----Fertig----"),
        ("", ""),
        ("Erzähler", "John nahm den Speicher an sich."),
        ("John", "Wir verschwinden hier. Wir wollen doch diesem Monster nicht begegnen, oder?"),
        ("", ""),
        ("Erzähler", "John blieb stehen."),
        ("Erzähler", "Hinter der Armatur war ein Geräusch zu hören."),
        ("Erzähler", "Kein Tropfen. Kein Knacken."),
        ("Erzähler", "Es klang eher wie ein tiefes, kratzendes Atmen."),
        ("", ""),
        ("Rico", "Habt ihr das gehört?"),
        ("Sara", "Ja."),
        ("", ""),
        ("Erzähler", "Etwas bewegte sich im Schatten."),
        ("Erzähler", "Langsam und ruckartig."),
        ("", ""),
        ("Erzähler", "Dunkle Gliedmaßen lösten sich von der Wand, als wäre sie nur eine Hülle gewesen."),
        ("Erzähler", "Zu viele Gelenke."),
        ("Erzähler", "Zu lange Finger."),
        ("Erzähler", "Kein Gesicht."),
        ("Erzähler", "Nur ein flackerndes Glimmen dort, wo Augen hätten sein sollen."),
        ("", ""),
        ("Erzähler", "Das Atmen wurde lauter."),
        ("", ""),
        ("John", "Was zur Hölle ist das...?"),
        ("", ""),
        ("Erzähler", "Johns Beine fühlten sich schwer an, als wollten sie ihn nicht mehr tragen."),
        ("", ""),
        ("Sara", "John ... lauf.")
    ],

    ist_kampf=False
)


Der_Kampf_im_Traum_6 = kampangen_kampf( #8
    "Das Monster",

    spieler_1="John",
    spieler_2="Sara",
    spieler_3="Lara",
    spieler_4="Rico",

    gegner_1="schattenwesen",

    team_groesse_1=4,
    team_groesse_2=1,

    belohnung=400,
    ki=3,
    npc_level=6,

    story_vorher=[
        ("Erzähler", "Das Wesen bewegte sich plötzlich auf das Team zu."),
        ("", ""),
        ("John", "Alle zurück!"),
        ("Erzähler", "John zog seine Waffe und richtete sie auf die Gestalt."),
        ("", ""),
        ("Sara", "Was ist das für ein Ding?"),
        ("Rico", "Keine Ahnung. Aber es sieht nicht freundlich aus."),
        ("Lara", "Dann finden wir es wohl gleich heraus.")
    ],

    ist_kampf=True,

    story_nachher=[
        ("Erzähler", "Das Wesen wich einige Schritte zurück."),
        ("Erzähler", "Für einen Moment bewegte es sich nicht."),
        ("", ""),
        ("Rico", "Ist es ... tot?"),
        ("", ""),
        ("Erzähler", "Niemand antwortete."),
        ("Erzähler", "Das Wesen stand regungslos im Schatten."),
        ("", ""),
        ("Sara", "John..."),
        ("", ""),
        ("Erzähler", "John sah zu der Gestalt."),
        ("Erzähler", "Dann begann die Umgebung um ihn herum zu verschwimmen."),
        ("", ""),
        ("John", "Was passiert hier?"),
        ("", ""),
        ("Erzähler", "Die Wände schienen sich zu verformen."),
        ("Erzähler", "Das Licht flackerte immer schneller."),
        ("", ""),
        ("Sara", "John!"),
        ("", ""),
        ("Erzähler", "Dann wurde alles schwarz."),
        ("", ""),
        ("Erzähler", "John schreckte sofort aus seinem Schlaf auf."),
        ("Erzähler", "Er konnte kaum atmen und bekam nur schwer Luft."),
        ("", ""),
        ("Erzähler", "Irgendwie schaffte er es schließlich wieder einzuschlafen."),
        ("Erzähler", "Dieses Mal blieb der Albtraum aus.")
    ]
)


Der_Plan_6 = kampangen_kampf( #9
    "Der Plan",
    story_vorher=[
        ("Erzähler", "Chasker eröffnete ihnen den Plan des Präsidenten und des Militärs."),
        ("Chasker", "Der Plan ist, mit dem momentan noch im Bau befindlichen Schiff eine Basis auf dem Mars zu errichten und anschließend zu untersuchen, was wir dort finden."),
        ("Erzähler", "Das Schiff wurde extra für diesen Zweck entworfen. Es bot Platz für eine große Anzahl an Personen, verfügte über große Labore,"),
        ("Erzähler", "einen geräumigen Hangar zur Versorgung und eine große Brücke, die später auch als Kontrollzentrale der zu errichtenden Basis dienen sollte."),
        ("", ""),
        ("Rico", "Und wie lange soll das noch dauern? Ich dachte, wir reden hier von mehreren Monaten."),
        ("Chasker", "Eigentlich sollte es nur noch ein paar Wochen dauern."),
        ("Rico", "Ein paar Wochen?"),
        ("Erzähler", "Alle waren überrascht. Niemand hatte damit gerechnet, dass das Schiff schon so bald fertig sein würde."),
        ("Sara", "Warum geht das plötzlich so schnell?"),
        ("Chasker", "Ich weiß es selbst nicht. Man hat mir nur gesagt, dass es in einer Woche fertig sein wird."),
        ("", ""),
        ("Erzähler", "Nachdem das Thema beendet war, wechselte Chasker das Thema."),
        ("Chasker", "Außerdem wurden die Leichen untersucht, die ihr in dem Objekt gefunden habt."),
        ("John", "Und?"),
        ("Chasker", "Nach den bisherigen Untersuchungen handelt es sich offenbar um eine Art Roboter, der von einer KI gesteuert wurde."),
        ("Chasker", "Dort, wo sie keine mechanischen Teile besaßen, bestanden sie allerdings aus Fleisch und Blut."),
        ("", ""),
        ("Lara", "Aber warum sahen sie dann so alt aus?"),
        ("Erzähler", "Darauf hatte niemand eine Antwort."),
        ("", ""),
        ("Chasker", "Es gibt noch etwas. Ein paar Forscher konnten eine Datei retten."),
        ("Erzähler", "Chasker öffnete die Datei und begann vorzulesen."),
        ("", ""),
        ("Chasker", "Wir sind unserem Ziel nähergekommen, doch wir werden langsam schwächer."),
        ("Chasker", "Wir haben heute auch bemerkt, dass ein Schiff der —unbekannten Rasse— mit uns auf Kollisionskurs ist."),
        ("Chasker", "Unsere erste Idee war es, den Kurs zu ändern, doch das lässt der Computer nicht zu."),
        ("Chasker", "So müssen wir hoffen, dass sie ihren Kurs wechseln, denn sonst würden sie unser Schiff entern und uns töten und anschließend zum Planeten ‚Erde‘ reisen, um dort —"),
        ("", ""),
        ("Erzähler", "Die Nachricht endete abrupt."),
        ("Erzähler", "Für einige Sekunden sagte niemand etwas."),
        ("", ""),
        ("John", "Jetzt haben wir ja noch eine Frage mehr."),
        ("Lara", "Ja. Nämlich, wer waren die, mit denen sie auf Kollisionskurs standen?"),
        ("", ""),
        ("Sara", "Dafür haben wir vielleicht eine Antwort auf eine andere Frage."),
        ("John", "Welche?"),
        ("Sara", "Warum sie ermordet wurden."),
        ("Sara", "Wahrscheinlich waren ihre Feinde oder Gegner in dem Schiff, mit dem sie auf Kollisionskurs standen. Sie könnten dann ihr Schiff betreten und sie getötet haben."),
        ("", ""),
        ("Erzähler", "Allen war aufgefallen, wie abrupt die Nachricht endete."),
        ("Erzähler", "Doch auch dafür hatten sie keine Erklärung.")
    ],
    ist_kampf=False
)


Die_Woche_6 = kampangen_kampf( #10

    "Die Woche",

    story_vorher=[
        ("Erzähler", "Die folgenden sieben Tage verliefen größtenteils ruhig, doch die Ereignisse aus der Station ließen die Gruppe nicht los."),
        ("", ""),
        ("Erzähler", "Am ersten Tag untersuchte Sara die gefundenen Proben im Labor."),
        ("Erzähler", "Unter dem Mikroskop wirkten einige Bruchstücke wie Metall, doch manchmal schien sich ihre Oberfläche leicht zu bewegen."),
        ("Sara", "Vielleicht nur eine optische Täuschung."),
        ("Erzähler", "Trotzdem schloss sie die Proben zur Sicherheit in einen Safe."),
        ("", ""),
        ("Erzähler", "Am zweiten Tag beschäftigte sich die Gruppe mit den Soldaten und Forschern mit der Auswertung des Fundes."),
        ("Erzähler", "Rico langweilte sich und machte sich über die langsamen Untersuchungen lustig, während Lara ihn immer wieder zur Ordnung rief."),
        ("Erzähler", "Abgesehen davon verlief der Tag völlig normal."),
        ("", ""),
        ("Erzähler", "Am dritten Tag fiel für genau dreißig Sekunden der Strom aus."),
        ("Erzähler", "Auch die Kühlkammern mit den Leichen waren betroffen."),
        ("Chasker", "Alles unter Kontrolle."),
        ("Erzähler", "Ein Soldat behauptete später, im Dunkeln zwei leuchtende Augen gesehen zu haben."),
        ("Erzähler", "Niemand nahm ihn ernst."),
        ("Erzähler", "John allerdings behielt die Aussage im Hinterkopf."),
        ("", ""),
        ("Erzähler", "Am vierten Tag schien wieder alles normal zu sein."),
        ("Erzähler", "Die Gruppe trainierte, erledigte Papierkram und besprach die Vorbereitungen für den Abflug."),
        ("Erzähler", "Trotzdem blieb das ungute Gefühl bestehen, dass etwas nicht stimmte."),
        ("", ""),
        ("Erzähler", "Am fünften Tag bemerkte Lara beim Frühstück, dass ihre Uhr mehrere Minuten nachging."),
        ("Lara", "Vielleicht ist einfach die Batterie leer."),
        ("Erzähler", "Kurz darauf bemerkte auch Sara, dass ihre Uhr nicht mehr richtig lief."),
        ("Sara", "Meine läuft auch nicht mehr ganz richtig."),
        ("Erzähler", "Die Gruppe schob es zunächst auf defekte Uhren."),
        ("", ""),
        ("Erzähler", "In der folgenden Nacht konnte John nicht einschlafen."),
        ("Erzähler", "Immer wieder hörte er dieses leise, kratzende Atmen."),
        ("Erzähler", "Als er schließlich in die Küche ging und zurückkam, entdeckte er frische Kratzer an der Wand neben seinem Bett."),
        ("Erzähler", "Sie sahen aus, als hätte jemand mit langen Fingern darübergefahren."),
        ("Erzähler", "John wollte dort nicht mehr schlafen und buchte sich noch in derselben Nacht ein Hotel."),
        ("", ""),
        ("Erzähler", "Am siebten Tag traf sich die Gruppe erneut bei Chasker."),
        ("Erzähler", "Alle wirkten müde und überarbeitet, doch niemand sprach die seltsamen Ereignisse offen an."),
        ("Chasker", "Das Schiff ist fast fertig. Der Abflug kann bald stattfinden."),
        ("Erzähler", "John sah zu Sara, Lara und Rico."),
        ("Erzähler", "Keiner von ihnen glaubte noch daran, dass sie eine normale Mission erwartete.")
    ],

    ist_kampf=False
)


Der_Abflug_6 = kampangen_kampf( #11
    "Der Abflug",
    story_vorher=[
        ("Erzähler", "Der Hangar war still. Nur das leise Summen der Maschinen war zu hören."),
        ("Erzähler", "Das Schiff stand bereit unter den grellen Scheinwerfern."),
        ("Chasker", "Bereit?"),
        ("Erzähler", "John, Sara, Lara und Rico machten sich bereit."),
        ("Erzähler", "Als John im Cockpit Platz nahm, flackerte kurz ein rotes Warnlicht auf einem Monitor auf."),
        ("John", "Nur ein Fehler ... hoffentlich."),
        ("Erzähler", "Kurz darauf hob das Schiff ab."),
        ("Erzähler", "Die Erde wurde unter ihnen immer kleiner, während das Schiff die Atmosphäre verließ."),
        ("Erzähler", "Plötzlich huschte ein Schatten über das Fenster."),
        ("John", "Habt ihr das gesehen?"),
        ("Sara", "Nein. Alle Systeme sind stabil."),
        ("Rico", "Also, Leute ... denkt dran. Wir fliegen zum Mars, nicht ins Gruselkabinett."),
        ("Erzähler", "Niemand lachte."),
        ("Erzähler", "Als die Erde hinter ihnen verschwand, ruckelte das Schiff plötzlich."),
        ("Chasker", "Keine Panik. Nur ein Turbulenzstoß im Orbit."),
        ("Erzähler", "Doch niemand war wirklich entspannt."),
        ("Erzähler", "Für John fühlte es sich nicht wie der Beginn einer normalen Mission an.")
    ],
    ist_kampf=False
)


Der_Flug_6 = kampangen_kampf( #12
    "Der Flug",
    story_vorher=[
        ("Erzähler", "Die Reise zum Mars sollte knapp zwei Tage dauern. Die Crew wechselte sich deshalb bei der Steuerung ab."),
        ("", ""),
        ("Erzähler", "Während Rico seine Schicht hatte, sah sich Sara im Labor um."),
        ("Erzähler", "Das Labor war mit modernster Ausrüstung ausgestattet und wirkte deutlich fortschrittlicher als alles, was Sara bisher gesehen hatte."),
        ("Erzähler", "Nachdem sie sich umgesehen hatte, kehrte sie auf die Brücke zurück."),
        ("", ""),
        ("Erzähler", "Als Rico abgelöst wurde, sah er sich noch kurz im Lager um."),
        ("Erzähler", "Dort fand er Lebensmittel, Getränke, Waffen und verschiedene UAVs."),
        ("Erzähler", "Sogar mehrere Militärhubschrauber waren dort untergebracht."),
        ("Rico", "Ob die Dinger auf dem Mars überhaupt fliegen können?"),
        ("Erzähler", "Er nahm sich vor, später einen Forscher danach zu fragen."),
        ("", ""),
        ("Erzähler", "Am nächsten Tag übernahm John die Steuerung."),
        ("Erzähler", "Zunächst überprüfte er die Flugdaten. Der Kurs war stabil und alle Systeme funktionierten normal."),
        ("Erzähler", "Dann flackerte plötzlich ein Signal auf dem Navigationsschirm auf."),
        ("John", "Hm ..."),
        ("Erzähler", "Die Koordinaten stimmten nicht mehr mit seiner ursprünglichen Eingabe überein."),
        ("Erzähler", "John korrigierte den Kurs manuell."),
        ("Erzähler", "Für einen kurzen Moment erschien dabei ein fremdes Symbol auf dem Bildschirm."),
        ("Erzähler", "Dann war es wieder verschwunden."),
        ("John", "Muss ein Glitch gewesen sein."),
        ("", ""),
        ("Erzähler", "Währenddessen dokumentierte Lara die ungewöhnlichen Ereignisse auf ihrem Tablet."),
        ("Lara", "Tag 2: leichte Abweichung der Kurskoordinaten. John hat korrigiert. Sensorwerte stabil."),
        ("Erzähler", "Sie wusste nicht, was sie erwartete. Aber sie wollte sicherstellen, dass nichts vergessen wurde.")
    ],
    ist_kampf=False
)


Gefangen_von_der_Marsstation_6 = kampangen_kampf( #13
    "Gefangen von der Marsstation",
    story_vorher=[
        ("Erzähler", "Gegen 15:00 Uhr näherte sich die Red Horizon der geplanten Landestelle auf dem Mars."),
        ("Erzähler", "Unter der dünnen Atmosphäre waren nur rote Felsen und endlose Ebenen zu erkennen."),
        ("John", "Ich überprüfe noch einmal den Kurs."),
        ("Erzähler", "John überprüfte den Kurs, während Lara die Instrumente überwachte."),
        ("Erzähler", "Plötzlich registrierten die Sensoren eine Energiespitze unterhalb des Schiffes."),
        ("John", "Was ist das?"),
        ("Erzähler", "Ein schwaches, bläuliches Licht begann unter dem Schiff zu pulsieren."),
        ("Erzähler", "Ohne Vorwarnung erfasste ein Lichtstrahl die Red Horizon."),
        ("Erzähler", "Das Schiff wurde mit großer Kraft in Richtung Boden gezogen."),
        ("John", "Ich verliere die Kontrolle!"),
        ("Erzähler", "John kämpfte mit den Steuerhebeln, doch das Schiff reagierte kaum."),
        ("Erzähler", "Unter ihnen begann der Boden metallisch zu glühen."),
        ("Erzähler", "Eine gigantische Struktur schob sich aus dem Marsboden."),
        ("Erzähler", "Eine fremde Station, die teilweise tief in den roten Felsen eingebettet war."),
        ("Erzähler", "Dünne, pulsierende Adern zogen sich über ihre Oberfläche."),
        ("Rico", "Was zum ...?"),
        ("Erzähler", "Die Red Horizon wurde langsam auf die Station zugezogen."),
        ("Erzähler", "Die Instrumente spielten verrückt und mehrere Navigationssysteme fielen aus."),
        ("Erzähler", "Dann öffnete sich eine gigantische Schleuse."),
        ("Erzähler", "Die Red Horizon wurde in die Station hineingezogen."),
        ("Erzähler", "Im Inneren schimmerte alles metallisch und organisch zugleich."),
        ("Erzähler", "Adern zogen sich über Wände und Boden."),
        ("Erzähler", "Es war vollkommen still."),
        ("John", "Wir ... sind nicht gelandet."),
        ("John", "Wir wurden in diese Station gezogen.")
    ],
    ist_kampf=False
)


Ein_neues_Zuhause_6 = kampangen_kampf( #14

    "Ein neues Zuhause",

    story_vorher=[
        ("Erzähler", "Nachdem die Red Horizon zum Stillstand gekommen war, wurde das Gebiet sofort von Soldaten gesichert."),
        ("", ""),
        ("Chasker", "Durchsucht die Station. Wir müssen herausfinden, ob wir hier alleine sind."),
        ("", ""),
        ("Erzähler", "John und sein Team wurden damit beauftragt, die erste Erkundung zu leiten."),
        ("Erzähler", "Vorsichtig bewegten sie sich durch die unbekannten Gänge."),
        ("", ""),
        ("Erzähler", "Nach einigen Ecken huschte plötzlich ein dunkler Schatten über eine Wand."),
        ("Rico", "Habt ihr das gesehen?"),
        ("John", "Ja."),
        ("Erzähler", "John blieb stehen und sah in den Gang zurück."),
        ("Erzähler", "Für einen kurzen Moment glaubte er, eine Kreatur zu erkennen."),
        ("Erzähler", "Doch der Gang war leer."),
        ("", ""),
        ("Erzähler", "Sie gingen vorsichtig weiter."),
        ("Erzähler", "Wenig später entdeckten sie einen metallischen Körper auf dem Boden."),
        ("Erzähler", "Nur noch wenige Reste von Fleisch befanden sich an dem mechanischen Körper."),
        ("", ""),
        ("Sara", "Das sieht genauso aus wie die Kreaturen, die wir in dem Asteroiden gefunden haben."),
        ("Sara", "Nur hatten die dort noch viel mehr Fleisch am Körper."),
        ("", ""),
        ("Erzähler", "Es sah aus, als hätte etwas das Fleisch des Wesens gewaltsam von seinem Körper gerissen."),
        ("", ""),
        ("Lara", "Hier ist etwas."),
        ("", ""),
        ("Erzähler", "Lara entdeckte neben dem Körper einen kleinen Datenträger."),
        ("Lara", "Den nehme ich für weitere Untersuchungen mit."),
        ("", ""),
        ("Erzähler", "John betrachtete den Körper genauer."),
        ("", ""),
        ("John", "Das Ding sieht aus wie der Terminator."),
        ("", ""),
        ("Rico", "Vielleicht war der Schatten dafür verantwortlich."),
        ("Rico", "Wir sollten zu Chasker zurück und ihm Bericht erstatten."),
        ("", ""),
        ("Erzähler", "Bevor sie sich auf den Rückweg machen konnten, meldete sich Chasker über Funk."),
        ("", ""),
        ("Chasker", "John, hört ihr mich?"),
        ("John", "Laut und deutlich."),
        ("Chasker", "Ein Erkundungsteam wird vermisst. Sucht nach ihnen und bringt sie zurück."),
        ("John", "Verstanden.")
    ],

    ist_kampf=False
)


Der_erste_Kontakt_6 = kampangen_kampf( #15
    "Der erste Kontakt",
    spieler_1="John",
    spieler_2="Sara",
    spieler_3="Lara",
    spieler_4="Rico",
    gegner_1="mars_sicherheitsdrohne",
    belohnung=150,
    ki=2,
    npc_level=5,
    team_groesse_1=8,
    team_groesse_2=1,

    story_vorher=[
        ("Erzähler", "Das Team machte sich auf die Suche nach den vermissten Soldaten."),
        ("Erzähler", "Plötzlich ertönte hinter ihnen ein metallisches Geräusch."),
        ("Rico", "Ähm ... Leute?"),
        ("Erzähler", "Aus einem Seitengang bewegte sich eine mechanische Gestalt auf das Team zu."),
        ("John", "Kontakt!"),
        ("Erzähler", "Die Gestalt beschleunigte und stürmte direkt auf das Team zu."),
        ("John", "Alle zurück!")
    ],

    ist_kampf=True,

    story_nachher=[
        ("Erzähler", "Die mechanische Gestalt fiel zu Boden."),
        ("Sara", "Was zum Teufel war das?"),
        ("Lara", "Vermutlich eine Art Sicherheitsdrohne."),
        ("John", "Dann müssen wir davon ausgehen, dass es noch mehr davon gibt."),
        ("Rico", "Na super."),
        ("Erzähler", "John sah in den dunklen Gang."),
        ("John", "Wir suchen weiter. Aber diesmal bleiben wir besonders vorsichtig.")
    ]
)


Weitere_Sicherheitsdrohnen_6 = kampangen_kampf( #16
    "Weitere Sicherheitsdrohnen",
    spieler_1="John",
    spieler_2="Sara",
    spieler_3="Lara",
    spieler_4="Rico",

    gegner_1="mars_sicherheitsdrohne",
    gegner_2="mars_sicherheitsdrohne",

    belohnung=250,
    ki=2,
    npc_level=6,
    team_groesse_1=4,
    team_groesse_2=2,

    story_vorher=[
        ("Erzähler", "Das Team folgte den Spuren des vermissten Erkundungsteams."),
        ("Erzähler", "Je weiter sie in die Station vordrangen, desto dunkler wurden die Gänge."),
        ("Erzähler", "Plötzlich waren aus zwei verschiedenen Richtungen metallische Geräusche zu hören."),
        ("Rico", "Das werden wohl nicht unsere vermissten Soldaten sein."),
        ("John", "Waffen bereit."),
        ("Erzähler", "Zwei größere Sicherheitsdrohnen traten aus der Dunkelheit."),
        ("Sara", "Die sehen stärker aus als die letzte."),
        ("John", "Dann erledigen wir sie schnell.")
    ],

    ist_kampf=True,

    story_nachher=[
        ("Erzähler", "Beide Drohnen lagen regungslos auf dem Boden."),
        ("Lara", "Die werden stärker."),
        ("Sara", "Dann sollten wir uns langsam fragen, was hier unten noch auf uns wartet."),
        ("John", "Wir finden zuerst das vermisste Team."),
        ("Erzähler", "Sie setzten ihren Weg durch die Station fort.")
    ]
)


Der_dritte_Kampf_6 = kampangen_kampf( #17
    "Der dritte Kampf",
    spieler_1="John",
    spieler_2="Sara",
    spieler_3="Lara",
    spieler_4="Rico",

    gegner_1="mars_sicherheitsdrohne",
    gegner_2="mars_sicherheitsdrohne",
    gegner_3="mars_sicherheitsdrohne",

    belohnung=350,
    ki=3,
    npc_level=4,
    team_groesse_1=4,
    team_groesse_2=3,

    story_vorher=[
        ("Erzähler", "Das Team setzte seine Suche nach den vermissten Soldaten fort."),
        ("Erzähler", "Die Gänge wurden immer dunkler und die Abstände zwischen den einzelnen Lichtquellen immer größer."),
        ("Erzähler", "Immer wieder hörten sie ein leises Kratzen aus den Seitengängen."),
        ("Rico", "Ich hasse diesen Ort."),
        ("Lara", "Du hast das vor einer Stunde auch schon gesagt."),
        ("Rico", "Und ich hatte da schon recht."),
        ("Erzähler", "Plötzlich ertönte hinter ihnen ein lautes metallisches Geräusch."),
        ("John", "Alle stehen bleiben."),
        ("Erzähler", "John drehte sich langsam um."),
        ("Erzähler", "Eine Sicherheitsdrohne stand am anderen Ende des Ganges."),
        ("Sara", "Da ist eine."),
        ("Erzähler", "Dann leuchteten zwei weitere Lichter aus den Seitengängen auf."),
        ("Rico", "Drei."),
        ("John", "Waffen bereit."),
        ("Erzähler", "Die erste Drohne bewegte sich langsam auf sie zu."),
        ("Erzähler", "Plötzlich beschleunigte sie."),
        ("John", "Jetzt!")
    ],

    ist_kampf=True,

    story_nachher=[
        ("Erzähler", "Die letzte Drohne fiel zu Boden."),
        ("Erzähler", "Für einige Sekunden war nur das leise Summen der beschädigten Maschinen zu hören."),
        ("Rico", "Das werden jedes Mal mehr."),
        ("Sara", "Und stärker."),
        ("Lara", "Wir sollten vorsichtiger werden."),
        ("John", "Ja. Aber wir müssen die Vermissten finden."),
        ("Erzähler", "John sah den Gang entlang."),
        ("Erzähler", "Am Boden waren mehrere Kratzer zu sehen, die in dieselbe Richtung führten."),
        ("Lara", "Vielleicht haben sie etwas damit zu tun."),
        ("John", "Dann folgen wir ihnen.")
    ]
)


Die_ersten_Opfer_6 = kampangen_kampf( #18
    "Die ersten Opfer",
    story_vorher=[
        ("Erzähler", "Sie machten sich sofort wieder auf die Suche nach dem verschollenen Team."),
        ("Erzähler", "Die leeren Flure der Station wurden immer unheimlicher."),
        ("Erzähler", "Während sie durch die Gänge gingen, hörten sie immer wieder ein Kratzen oder andere seltsame Geräusche."),
        ("Erzähler", "Bei jedem Geräusch zuckten sie zusammen und sahen sich um."),
        ("Erzähler", "Doch jedes Mal war nichts zu sehen."),
        ("Rico", "Ich habe langsam das Gefühl, dass uns hier irgendetwas beobachtet."),
        ("Sara", "Sag sowas nicht."),
        ("Erzähler", "Plötzlich bemerkte Lara einen schwachen Lichtschein weiter vorne im Gang."),
        ("Lara", "Da vorne."),
        ("Erzähler", "Sie gingen vorsichtig näher."),
        ("Erzähler", "Der Lichtschein kam von einer Waffe, die offenbar fallen gelassen worden war."),
        ("John", "Die gehört einem unserer Leute."),
        ("Erzähler", "Sie folgten dem Gang weiter."),
        ("Erzähler", "Nach wenigen Metern entdeckten sie schließlich einen Soldaten, der schwer verletzt in einer Ecke saß."),
        ("John", "Da ist einer!"),
        ("Erzähler", "Sie eilten sofort zu ihm."),
        ("Sara", "Ganz ruhig. Wir bringen dich hier raus."),
        ("Erzähler", "Als sie ihm aufhelfen wollten, bemerkten sie die schwere Verletzung an seinem Hinterkopf."),
        ("Lara", "Er braucht sofort medizinische Hilfe."),
        ("John", "Wir bringen ihn zur Red Horizon."),
        ("Erzähler", "Gemeinsam brachten sie den verletzten Soldaten zurück zum Schiff."),
        ("Erzähler", "Dort wurde er sofort auf die Krankenstation gebracht."),
        ("Erzähler", "Die Gruppe wusste zu diesem Zeitpunkt noch nicht, was sie auf der Bodycam des Soldaten sehen würde.")
    ],
    ist_kampf=False
)


Die_Bodycam_6 = kampangen_kampf( #19
    "Die Bodycam",
    story_vorher=[
        ("Erzähler", "Zurück auf der Red Horizon wurde der verwundete Soldat in die Isolationszelle der Krankenstation gebracht."),
        ("Erzähler", "Sara begann sofort mit der Untersuchung, während John die Speicherkarte aus der Bodycam zog."),
        ("John", "Vielleicht erfahren wir, was passiert ist."),
        ("Erzähler", "Rico und Lara stellten sich hinter ihn, während John die Aufnahme auf den Hauptschirm lud."),
        ("", ""),
        ("Erzähler", "Das Video begann ruhig."),
        ("Erzähler", "Zwei Soldaten patrouillierten durch die kalten, metallenen Gänge der Station."),
        ("Erzähler", "Die Wände waren teilweise von den pulsierenden Adern durchzogen."),
        ("Erzähler", "Plötzlich war ein Kratzen zu hören."),
        ("Erzähler", "Der vordere Soldat hob sein Gewehr und näherte sich vorsichtig einer schmalen Öffnung in der Wand."),
        ("Erzähler", "Dann schoss etwas Großes und Dunkles aus dem Schacht."),
        ("Erzähler", "Eine unnatürlich große Hand packte den Soldaten und zog ihn in die Öffnung."),
        ("Erzähler", "Sein Schrei hallte durch den Gang und verstummte plötzlich."),
        ("Erzähler", "Der zweite Soldat wich zurück und rief nach seinem Kameraden."),
        ("Erzähler", "Doch er bekam keine Antwort."),
        ("Erzähler", "Dann rannte er."),
        ("Erzähler", "Die Kamera zeigte nur noch hastige Bewegungen und den keuchenden Atem des Soldaten."),
        ("Erzähler", "Schließlich stolperte er und stürzte."),
        ("Erzähler", "Als er wieder aufstand, schleppte er sich in eine Ecke."),
        ("Erzähler", "Die letzten Sekunden der Aufnahme zeigten nur noch verschwommene Schatten."),
        ("Erzähler", "Dann war ein tiefes Knurren zu hören."),
        ("Erzähler", "Das Bild wurde schwarz."),
        ("", ""),
        ("Erzähler", "Niemand sagte etwas."),
        ("John", "Was ... war das?"),
        ("Lara", "Das war definitiv kein Mensch."),
        ("Rico", "Und ich dachte, die Drohnen wären schon schlimm."),
        ("", ""),
        ("Erzähler", "Plötzlich knackte das Funkgerät."),
        ("Soldat", "Commander Chasker, bitte kommen Sie sofort in die Krankenstation! Es ist dringend!"),
        ("Erzähler", "Chasker stand sofort auf."),
        ("Chasker", "Ich bin unterwegs."),
        ("Erzähler", "John, Sara, Lara und Rico folgten ihm.")
    ],
    ist_kampf=False
)


Die_Seuche_6 = kampangen_kampf( #20
    "Die Seuche",
    story_vorher=[
        ("Erzähler", "Als sie in der Isolationszelle ankamen, erstarrten alle."),
        ("Erzähler", "Vor ihnen regte sich der verwundete Soldat, doch es war nicht mehr er."),
        ("Erzähler", "Aus seinem Körper zeichnete sich eine schattenhafte Gestalt ab."),
        ("Erzähler", "Schwarze Gliedmaßen, zu viele Gelenke und eine verzerrte Silhouette bewegten sich über den Boden."),
        ("Lara", "Oh Gott ..."),
        ("Erzähler", "Lara wich instinktiv zurück."),
        ("Erzähler", "Auch Rico war das Grinsen vergangen. Er starrte regungslos auf das Wesen."),
        ("Erzähler", "Das Wesen bewegte sich langsam, aber gezielt auf sie zu."),
        ("Erzähler", "Dort, wo sich Augen befinden könnten, flackerte ein dunkles Licht."),
        ("Erzähler", "Chasker trat einen Schritt nach vorne."),
        ("Chasker", "Bleibt ruhig ... wir tun dir nichts."),
        ("Erzähler", "Das Wesen reagierte plötzlich."),
        ("Erzähler", "Mit einer schnellen Bewegung schoss es ein Stück nach vorne."),
        ("Erzähler", "Es griff jedoch nicht an."),
        ("Erzähler", "Stattdessen blieb es stehen und betrachtete die Gruppe."),
        ("Erzähler", "John spürte, wie seine Hände schwitzten."),
        ("Erzähler", "Sara versuchte ruhig zu bleiben, während Rico seinen Blick nicht von dem Wesen lösen konnte."),
        ("Erzähler", "Plötzlich zuckte das Wesen, als hätte es ein Geräusch wahrgenommen, das nur es hören konnte."),
        ("Erzähler", "Dann bewegte es sich zurück und verkroch sich in eine Ecke."),
        ("Sara", "Es sieht so aus, als würde es kommunizieren."),
        ("John", "Ich habe eine Theorie."),
        ("Erzähler", "Die Gruppe verließ die Krankenstation und ging zurück auf die Brücke."),
        ("Erzähler", "Das Wesen blieb hinter der Glasscheibe der Isolationszelle zurück.")
    ],
    ist_kampf=False
)


Die_Theorie_6 = kampangen_kampf( #21
    "Die Theorie",
    story_vorher=[
        ("Erzähler", "Auf der Brücke erzählte John den anderen von seiner Beobachtung."),
        ("John", "Als wir damals den Leichensack gesehen haben, hat er sich bewegt."),
        ("John", "Damals dachte ich, ich hätte mir das nur eingebildet."),
        ("John", "Aber dann gab es die leuchtenden Augen in der Kühlkammer."),
        ("John", "Und wir haben diese Nachricht über das unbekannte Schiff gefunden."),
        ("John", "Ich glaube, dass das alles zusammenhängt."),
        ("Rico", "Und was genau glaubst du?"),
        ("John", "Ich glaube, dass diese Aliens eine Art Seuche sind."),
        ("John", "Wenn jemand mit ihnen in Kontakt kommt, könnte er selbst zu einem von ihnen werden."),
        ("Erzähler", "Für einen Moment sagte niemand etwas."),
        ("Chasker", "Aber wenn in dem Leichensack wirklich ein Alien war ..."),
        ("Chasker", "Dann könnte es entkommen sein und die Seuche verbreiten."),
        ("Chasker", "Wenn es die Erde erreicht, könnte das die gesamte Erde betreffen."),
        ("John", "Genau."),
        ("Erzähler", "Chasker traf sofort eine Entscheidung."),
        ("Chasker", "Wir fliegen zurück zur Erde."),
        ("Erzähler", "Er wollte gerade die Rückkehr vorbereiten, als Sara auf die Instrumente sah."),
        ("Sara", "Chasker ... wir können nicht zurück."),
        ("Chasker", "Was?"),
        ("Sara", "Die Station hält uns fest."),
        ("Erzähler", "Chasker sah sie ungläubig an."),
        ("Chasker", "Scheiße!"),
        ("Erzähler", "Er blickte auf die Anzeigen."),
        ("Chasker", "Wahrscheinlich Halteklammern!")
    ],
    ist_kampf=False
)


Plan_B_6 = kampangen_kampf( #22
    "Plan B",
    story_vorher=[
        ("Erzähler", "Die Nachricht, dass die Red Horizon von der Station festgehalten wurde, war äußerst beunruhigend."),
        ("Chasker", "Wenn wir jetzt nicht starten können, können wir es im Notfall ebenfalls nicht."),
        ("Erzähler", "Chasker überlegte kurz."),
        ("Chasker", "Wir müssen weiter in die Station vordringen."),
        ("Chasker", "Vielleicht finden wir eine Kommandozentrale oder etwas, mit dem wir die Halteklammern lösen können."),
        ("John", "Wie wäre es, wenn wir uns erstmal ausruhen, bevor wir uns in die Hölle begeben?"),
        ("Erzähler", "Für einen Moment sagte niemand etwas."),
        ("Rico", "Ehrlich gesagt klingt das gar nicht schlecht."),
        ("Sara", "Wir wissen nicht, was uns dort unten erwartet."),
        ("Lara", "Und wir sollten nicht völlig erschöpft losgehen."),
        ("Chasker", "In Ordnung."),
        ("Chasker", "Wir ruhen uns aus und gehen anschließend weiter."),
        ("Erzähler", "Die Gruppe beschloss, sich abwechselnd auszuruhen."),
        ("Erzähler", "Während einige schliefen, blieben andere zusammen mit einigen Marines auf der Brücke und hielten Wache."),
        ("Erzähler", "Die Station blieb währenddessen vollkommen still.")
    ],
    ist_kampf=False
)


Der_Traum_6 = kampangen_kampf( #23
    "Der Traum",

    # ─────────────────────────────────────
    # TEAM
    # ─────────────────────────────────────
    spieler_1="John",
    spieler_2=None,
    spieler_3=None,
    spieler_4=None,

    gegner_1="traum_sara",

    # ─────────────────────────────────────
    # KAMPF
    # ─────────────────────────────────────
    belohnung=400,
    ki=3,
    npc_level=1,
    team_groesse_1=1,
    team_groesse_2=1,

    # ─────────────────────────────────────
    # STORY VORHER
    # ─────────────────────────────────────
    story_vorher=[
        ("Erzähler", "John stand in der Luftschleuse."),
        ("Erzähler", "Alles war still. Zu still."),
        ("Erzähler", "Kein Piepen. Kein Summen. Nur sein eigener Atem."),
        ("", ""),
        ("Erzähler", "Vor ihm stand die Red Horizon im Dunst der Anlage."),
        ("Erzähler", "Doch etwas stimmte nicht."),
        ("Erzähler", "Das Metall wirkte spröde und war von leuchtenden Adern durchzogen."),
        ("", ""),
        ("Erzähler", "John versuchte, einen Schritt zu machen."),
        ("Erzähler", "Seine Stiefel klebten am Boden fest."),
        ("", ""),
        ("Erzähler", "Dann hörte er eine Stimme."),
        ("", ""),
        ("Traum-Sara", "John."),
        ("", ""),
        ("Erzähler", "John drehte sich ruckartig um."),
        ("Erzähler", "Sara stand dort."),
        ("Erzähler", "Zumindest dachte er das."),
        ("", ""),
        ("Erzähler", "Ihre Haut wirkte dunkel und unnatürlich."),
        ("Erzähler", "Ihre Augen waren vollkommen schwarz."),
        ("", ""),
        ("Traum-Sara", "Wir wollten es nicht ..."),
        ("", ""),
        ("John", "Was wolltet ihr nicht?"),
        ("", ""),
        ("Erzähler", "Hinter Sara bewegte sich etwas."),
        ("Erzähler", "Schatten krochen lautlos über die Wände."),
        ("Erzähler", "Ihre Bewegungen waren langsam und fließend, doch ihre Körper wirkten gleichzeitig fest."),
        ("", ""),
        ("Erzähler", "John erkannte die Gestalt aus der Krankenstation wieder."),
        ("Erzähler", "Zu viele Gelenke. Zu viele Hände."),
        ("", ""),
        ("Erzähler", "Sara hob langsam ihre Hand und zeigte auf John."),
        ("", ""),
        ("Traum-Sara", "Du bist schon einer von uns."),
        ("", ""),
        ("Erzähler", "John stolperte zurück."),
        ("Erzähler", "Er wollte schreien, doch kein Laut kam aus seinem Mund."),
        ("Erzähler", "Seine Finger begannen zu zittern."),
        ("", ""),
        ("Erzähler", "Dann sah er auf seine Hände."),
        ("Erzähler", "Dunkle Linien bewegten sich unter seiner Haut."),
        ("Erzähler", "Sie wanderten langsam seinen Arm hinauf und pulsierten im gleichen Rhythmus wie die Adern der Red Horizon."),
        ("", ""),
        ("Erzähler", "Dann hörte John es wieder."),
        ("Erzähler", "Dieses tiefe, kratzende Atmen."),
        ("Erzähler", "Es kam direkt von hinten."),
        ("", ""),
        ("Erzähler", "John wollte sich umdrehen, doch sein Körper bewegte sich nicht."),
        ("Erzähler", "Die Luft fühlte sich plötzlich schwer an."),
        ("", ""),
        ("Traum-Sara", "Es beginnt ..."),
    ],

    # ─────────────────────────────────────
    # KAMPF
    # ─────────────────────────────────────
    ist_kampf=True,

    # ─────────────────────────────────────
    # STORY NACHHER
    # ─────────────────────────────────────
    story_nachher=[
        ("Erzähler", "John schreckte hoch."),
        ("Erzähler", "Schweiß stand auf seiner Stirn und sein Atem ging stoßweise."),
        ("Erzähler", "Sein Herz raste."),
        ("", ""),
        ("Erzähler", "Für einen Moment wusste er nicht, wo er war."),
        ("Erzähler", "Dann sah er sich in seiner Kabine um."),
        ("Erzähler", "Alles war still."),
        ("", ""),
        ("Erzähler", "John versuchte, sich zu beruhigen."),
        ("Erzähler", "Doch dann bemerkte er etwas."),
        ("Erzähler", "Im Halbdunkel glaubte er für einen kurzen Moment, den Nebel seines eigenen Atems zu sehen."),
        ("Erzähler", "Doch es sah nicht so aus, als würde er selbst ausatmen."),
        ("Erzähler", "Es wirkte, als würde jemand direkt vor seinem Gesicht stehen und ihm ins Gesicht hauchen."),
        ("", ""),
        ("Erzähler", "John wich erschrocken zurück."),
        ("Erzähler", "Als er erneut hinsah, war dort nichts."),
        ("Erzähler", "Nur die Dunkelheit seiner Kabine."),
        ("", ""),
        ("Erzähler", "John blieb noch einige Sekunden wach."),
        ("Erzähler", "Dann legte er sich wieder hin.")
    ]
)


In_der_Hoehle_des_Loewen_6 = kampangen_kampf( #24
    "In der Höhle des Löwen",

    spieler_1="John",
    spieler_2="Sara",
    spieler_3=None,
    spieler_4=None,

    gegner_1="stationsdrohne",
    gegner_2="mars_wachroboter",
    gegner_3="stationsdrohne",

    belohnung=450,
    ki=3,
    npc_level=5,
    team_groesse_1=2,
    team_groesse_2=3,

    story_vorher=[
        ("Erzähler", "John stand auf und bereitete sich auf die bevorstehende Mission vor."),
        ("Erzähler", "Immer wieder fragte er sich, was sie in den Tiefen der Station finden würden."),
        ("Erzähler", "Vielleicht eine Horde dieser Kreaturen. Vielleicht weitere Roboter. Vielleicht nur Daten, die erklären konnten, was hier geschehen war."),
        ("Erzähler", "Doch ein Gedanke ließ ihn nicht los."),
        ("Erzähler", "Was wäre, wenn sie dem Tod direkt gegenüberstehen würden?"),
        ("Erzähler", "Diesen Gedanken verdrängte John."),
        ("Erzähler", "Er nahm seine Waffe und ging zu den anderen."),
        ("", ""),
        ("Erzähler", "Chasker hatte die Gruppe inzwischen in zwei Teams aufgeteilt."),
        ("Erzähler", "John und Sara sollten gemeinsam mit fünf Marines einen Bereich der Station durchsuchen."),
        ("Erzähler", "Rico und Lara würden mit weiteren fünf Marines einen anderen Bereich übernehmen."),
        ("", ""),
        ("Chasker", "Bleibt über Funk in Kontakt. Wenn ihr etwas findet, meldet euch sofort."),
        ("John", "Verstanden."),
        ("", ""),
        ("Erzähler", "Johns Atem hallte dumpf in seinem Helm wider, während sein Team durch einen schmalen Gang ging."),
        ("Erzähler", "Die Helmlampen glitten über kalte Metallwände, die an einigen Stellen deutliche Spuren eines früheren Kampfes zeigten."),
        ("", ""),
        ("Sara", "Kein Lebenszeichen."),
        ("John", "Bleibt wachsam."),
        ("", ""),
        ("Erzähler", "Plötzlich ertönte in der Ferne ein metallisches Klirren."),
        ("Erzähler", "Alle blieben stehen."),
        ("", ""),
        ("Marine", "Bewegung im Nordflügel."),
        ("", ""),
        ("Erzähler", "Dann meldete sich Rico über Funk."),
        ("Rico", "Wir haben hier auch etwas. Wartet ..."),
        ("Rico", "Da ist ..."),
        ("", ""),
        ("Erzähler", "Die Verbindung brach ab."),
        ("", ""),
        ("Sara", "Sollen wir zu ihnen?"),
        ("John", "Wir gehen."),
        ("", ""),
        ("Erzähler", "Das Klirren ertönte erneut."),
        ("Erzähler", "Diesmal war es deutlich näher."),
        ("Erzähler", "Dann hörten sie ein leises, unregelmäßiges Geräusch aus dem Gang vor ihnen."),
        ("", ""),
        ("Erzähler", "Das Team erreichte schließlich eine große Wartungshalle."),
        ("Erzähler", "Zerrissene Kabel hingen von der Decke und dunkle Flüssigkeit tropfte auf den Boden."),
        ("", ""),
        ("Erzähler", "Hinter mehreren Metallcontainern entdeckten sie Rico und Lara mit ihrem Team."),
        ("", ""),
        ("Rico", "Da seid ihr ja."),
        ("John", "Was ist passiert?"),
        ("Lara", "Wir wissen es selbst nicht genau."),
        ("", ""),
        ("Erzähler", "Plötzlich bewegte sich etwas am anderen Ende der Halle."),
        ("Sara", "Kontakt!")
    ],

    ist_kampf=True,

    story_nachher=[
        ("Erzähler", "Die letzte Maschine fiel zu Boden."),
        ("Rico", "Das waren definitiv keine normalen Wartungsdrohnen."),
        ("Lara", "Sie haben uns offenbar registriert, sobald wir die Halle betreten haben."),
        ("John", "Dann sollten wir hier nicht länger bleiben."),
        ("", ""),
        ("Erzähler", "John sah sich in der Halle um."),
        ("Erzähler", "In der gegenüberliegenden Wand befand sich eine große Öffnung."),
        ("Erzähler", "Aus dem Inneren kam kalte Luft."),
        ("", ""),
        ("Rico", "Da hinten geht es weiter."),
        ("John", "Dann los.")
    ]
)


Die_Jagd_6 = kampangen_kampf( #25
    "Die Jagd",

    spieler_1="John",
    spieler_2="Sara",
    spieler_3="Rico",
    spieler_4="Lara",

    gegner_1="mars_wachroboter",
    gegner_2="stationsdrohne",
    gegner_3="mars_wachroboter",

    belohnung=550,
    ki=3,
    npc_level=9,
    team_groesse_1=4,
    team_groesse_2=3,

    story_vorher=[
        ("Erzähler", "Sie liefen durch einen schmalen Wartungsgang weiter."),
        ("Erzähler", "Niemand sprach."),
        ("Erzähler", "Hinter ihnen war wieder ein Geräusch zu hören."),
        ("", ""),
        ("Rico", "Das Ding ist noch da."),
        ("Sara", "Woher willst du das wissen?"),
        ("Rico", "Weil es immer dann ruhig wird, wenn wir denken, dass wir sicher sind."),
        ("", ""),
        ("Erzähler", "John sah kurz zurück."),
        ("Erzähler", "Nichts."),
        ("", ""),
        ("John", "Weiter."),
        ("", ""),
        ("Erzähler", "Dann vibrierte der Boden leicht."),
        ("Erzähler", "Ein dumpfer Schlag hallte durch die Station."),
        ("Erzähler", "Noch einer."),
        ("", ""),
        ("Lara", "Das kommt näher."),
        ("", ""),
        ("Erzähler", "Plötzlich öffnete sich eine Tür neben ihnen."),
        ("", ""),
        ("John", "Waffen bereit!")
    ],

    ist_kampf=True,

    story_nachher=[
        ("Erzähler", "Die Maschinen waren zerstört."),
        ("Erzähler", "John sah in den Gang zurück."),
        ("", ""),
        ("John", "Alle da?"),
        ("Rico", "Ja."),
        ("Lara", "Noch."),
        ("", ""),
        ("Erzähler", "Ein weiteres Geräusch ertönte irgendwo hinter ihnen."),
        ("", ""),
        ("Sara", "Wir sollten weiter."),
        ("John", "Schnell.")
    ]
)


Die_Jagd_2_6 = kampangen_kampf( #26
    "Die Jagd II",

    spieler_1="John",
    spieler_2="Sara",
    spieler_3="Rico",
    spieler_4="Lara",

    gegner_1="stationsdrohne",
    gegner_2="stationsdrohne",
    gegner_3="mars_wachroboter",
    gegner_4="stationsdrohne",

    belohnung=650,
    ki=3,
    npc_level=8,
    team_groesse_1=4,
    team_groesse_2=4,

    story_vorher=[
        ("Erzähler", "Sie rannten weiter, bis ihre Atemzüge in den Helmen deutlich zu hören waren."),
        ("Erzähler", "Erst in einem engen Wartungsschacht hielten sie an."),
        ("Erzähler", "Niemand sprach."),
        ("", ""),
        ("Erzähler", "John zählte die Helmlampen."),
        ("John", "Alle da."),
        ("", ""),
        ("Sara", "Es ist ruhig."),
        ("", ""),
        ("Erzähler", "John nickte, doch sein Blick blieb auf der Dunkelheit vor ihnen gerichtet."),
        ("", ""),
        ("Erzähler", "Dann vibrierte der Boden erneut."),
        ("Erzähler", "Ein dumpfer Schlag."),
        ("Erzähler", "Noch einer."),
        ("Erzähler", "Die Geräusche kamen näher."),
        ("", ""),
        ("John", "Licht aus."),
        ("", ""),
        ("Erzähler", "Die Helmlampen erloschen."),
        ("Erzähler", "Nur das rote Notlicht der Station blieb eingeschaltet."),
        ("", ""),
        ("Erzähler", "Etwas bewegte sich im Gang."),
        ("", ""),
        ("Rico", "Ich sehe nichts."),
        ("", ""),
        ("Erzähler", "Plötzlich schalteten sich mehrere rote Sensoren gleichzeitig ein."),
        ("", ""),
        ("Lara", "Da!")
    ],

    ist_kampf=True,

    story_nachher=[
        ("Erzähler", "Das rote Licht flackerte noch einige Male, bevor wieder Ruhe einkehrte."),
        ("", ""),
        ("Rico", "Wie viele von diesen Dingern gibt es hier eigentlich?"),
        ("Lara", "Keine Ahnung."),
        ("Sara", "Aber offenbar genug."),
        ("", ""),
        ("Erzähler", "John ging zu einem Terminal an der Wand."),
        ("", ""),
        ("John", "Vielleicht können wir hier herausfinden, wo wir sind."),
        ("", ""),
        ("Erzähler", "Das Terminal war jedoch beschädigt."),
        ("", ""),
        ("John", "Verdammt."),
        ("", ""),
        ("Erzähler", "Plötzlich hörten sie wieder ein leises Geräusch aus dem Gang."),
        ("", ""),
        ("Sara", "Das ist nicht die Türsteuerung."),
        ("John", "Nein.")
    ]
)


Die_Jagd_3_6 = kampangen_kampf( #27
    "Die Jagd III",

    spieler_1="John",
    spieler_2="Sara",
    spieler_3="Rico",
    spieler_4="Lara",

    gegner_1="infizierter_roboter",
    gegner_2="mars_wachroboter",

    belohnung=800,
    ki=3,
    npc_level=9,
    team_groesse_1=4,
    team_groesse_2=2,

    story_vorher=[
        ("Erzähler", "Das Geräusch kam näher."),
        ("Erzähler", "John hob seine Waffe."),
        ("", ""),
        ("John", "Alle bereit."),
        ("", ""),
        ("Erzähler", "Aus einem Seitengang trat langsam eine mechanische Gestalt."),
        ("", ""),
        ("Rico", "Das ist einer von denen."),
        ("Lara", "Aber der sieht anders aus."),
        ("", ""),
        ("Erzähler", "Die Maschine bewegte sich ruckartig."),
        ("", ""),
        ("Sara", "Da kommt noch einer."),
        ("", ""),
        ("Erzähler", "Hinter der ersten Gestalt tauchte ein weiterer Wachroboter auf."),
        ("", ""),
        ("John", "Nicht auseinanderziehen lassen."),
        ("", ""),
        ("Erzähler", "Die beiden Maschinen richteten ihre Waffen auf das Team.")
    ],

    ist_kampf=True,

    story_nachher=[
        ("Erzähler", "Die beiden Maschinen lagen regungslos auf dem Boden."),
        ("Erzähler", "John überprüfte kurz seine Ausrüstung."),
        ("", ""),
        ("John", "Alle noch einsatzfähig?"),
        ("Sara", "Ja."),
        ("Rico", "Noch."),
        ("", ""),
        ("Lara", "Wir sollten einen Weg zurück zur Hauptstrecke finden."),
        ("", ""),
        ("Erzähler", "Lara deutete auf einen Seitengang."),

        ("Lara", "Dort vorne müsste ein größerer Bereich kommen."),
        ("John", "Dann gehen wir dort hin.")
    ]
)


Die_Jagd_4_6 = kampangen_kampf( #28
    "Die Jagd IV",

    spieler_1="John",
    spieler_2="Sara",
    spieler_3="Rico",
    spieler_4="Lara",

    gegner_1="stationsdrohne",
    gegner_2="mars_wachroboter",
    gegner_3="stationsdrohne",
    gegner_4="mars_wachroboter",

    belohnung=950,
    ki=3,
    npc_level=8,
    team_groesse_1=4,
    team_groesse_2=4,

    story_vorher=[
        ("Erzähler", "Der Seitengang führte tatsächlich in einen größeren Bereich."),
        ("", ""),
        ("Erzähler", "Doch kaum hatten sie ihn betreten, schlossen sich mehrere Türen hinter ihnen."),
        ("", ""),
        ("Rico", "Das gefällt mir überhaupt nicht."),
        ("Sara", "Mir auch nicht."),
        ("", ""),
        ("Erzähler", "Mehrere Maschinen aktivierten sich gleichzeitig."),
        ("", ""),
        ("Lara", "Wir sitzen fest."),
        ("John", "Dann schaffen wir uns einen Weg frei.")
    ],

    ist_kampf=True,

    story_nachher=[
        ("Erzähler", "Die letzte Maschine fiel zu Boden."),
        ("Erzähler", "Eine der Türen öffnete sich wieder."),
        ("", ""),
        ("Rico", "Endlich."),
        ("", ""),
        ("Erzähler", "John trat vorsichtig in den nächsten Gang."),
        ("Erzähler", "Für einige Sekunden war nichts zu hören."),
        ("", ""),
        ("Erzähler", "Dann erklang aus der Ferne ein metallisches Schaben."),
        ("", ""),
        ("Sara", "Da ist es wieder."),
        ("John", "Nicht stehen bleiben."),
        ("", ""),
        ("Erzähler", "Sie gingen weiter.")
    ]
)


Die_Jagd_5_6 = kampangen_kampf( #29
    "Die Jagd V",

    spieler_1="John",
    spieler_2="Sara",
    spieler_3="Rico",
    spieler_4="Lara",

    gegner_1="mars_wachroboter",
    gegner_2="infizierter_roboter",
    gegner_3="mars_wachroboter",

    belohnung=1100,
    ki=3,
    npc_level=9,
    team_groesse_1=4,
    team_groesse_2=3,

    story_vorher=[
        ("Erzähler", "Sie rannten weiter, bis sie einen engen Wartungsschacht erreichten."),
        ("Erzähler", "Dort blieben sie kurz stehen."),
        ("Erzähler", "Niemand wagte es, laut zu sprechen."),
        ("", ""),
        ("Erzähler", "Dann schlug irgendwo in der Station Metall auf Metall."),
        ("Erzähler", "Ein Geräusch folgte dem nächsten."),
        ("", ""),
        ("Rico", "Es kommt wieder."),
        ("John", "Alle bereit."),
        ("", ""),
        ("Erzähler", "Am Ende des Schachtes bewegte sich eine Gestalt."),
        ("", ""),
        ("Sara", "Kontakt."),
        ("", ""),
        ("Erzähler", "Zwei weitere Maschinen traten aus der Dunkelheit."),
        ("", ""),
        ("John", "Feuer!")
    ],

    ist_kampf=True,

    story_nachher=[
        ("Erzähler", "Die letzten Maschinen gingen zu Boden."),
        ("Erzähler", "Für einen Moment war es vollkommen still."),
        ("", ""),
        ("Erzähler", "Dann hörten sie ein leises Kratzen."),
        ("", ""),
        ("Sara", "Da."),
        ("John", "Ich höre es."),
        ("", ""),
        ("Erzähler", "Das Geräusch kam nicht aus einem der Gänge."),
        ("Erzähler", "Es kam aus den Wänden."),
        ("", ""),
        ("Rico", "Das ist nicht gut."),
        ("", ""),
        ("Erzähler", "Plötzlich schlug irgendwo eine Tür zu."),
        ("", ""),
        ("Lara", "Die Türsteuerung."),
        ("", ""),
        ("Erzähler", "John sah zum Ende des Ganges."),
        ("", ""),
        ("John", "Es schließt uns ein.")
    ]
)


Plan_C_6 = kampangen_kampf( #30
    "Plan C",

    spieler_1="John",
    spieler_2="Lara",
    spieler_3=None,
    spieler_4=None,

    gegner_1="schattenwesen",

    belohnung=0,
    ki=3,
    npc_level=1,
    team_groesse_1=2,
    team_groesse_2=1,

    story_vorher=[
        ("Erzähler", "Ihnen allen war klar, dass sie dort nicht bleiben konnten."),
        ("Erzähler", "Sie durchsuchten den Gang nach irgendeinem Ausgang."),
        ("", ""),
        ("Erzähler", "Erst nach einer gefühlten Stunde entdeckte einer der Marines eine Luke."),
        ("Erzähler", "In der Luke befand sich ein kleines Loch, vermutlich durch einen Schuss oder einen früheren Schaden entstanden."),
        ("Erzähler", "Dahinter war ein Schacht mit einer Leiter zu erkennen."),
        ("", ""),
        ("Marine", "Die Verriegelung ist teilweise geschmolzen."),
        ("John", "Kannst du sie öffnen?"),
        ("Marine", "Nein. Nicht von Hand."),
        ("", ""),
        ("Erzähler", "Die geschmolzenen Stellen mussten entfernt werden."),
        ("", ""),
        ("John", "Dann müssen wir darauf schießen."),
        ("Sara", "Das wird es hören."),
        ("John", "Ich weiß."),
        ("", ""),
        ("Erzähler", "Doch es war ihre einzige Möglichkeit."),
        ("", ""),
        ("John", "Sobald ich schieße, gehen Rico und vier Marines vor."),
        ("John", "Ihr sichert das Gebiet am anderen Ende der Leiter."),
        ("John", "Danach gehen Sara, Lara und die restlichen Marines."),
        ("John", "Ich gehe zuletzt."),
        ("John", "Wir werden es schaffen. Also los!"),
        ("", ""),
        ("Erzähler", "John hob seine Waffe."),
        ("Erzähler", "Ein Schuss krachte durch den Gang."),
        ("Erzähler", "Die geschmolzenen Teile der Verriegelung brachen auseinander."),
        ("Erzähler", "Ein lautes Klirren hallte durch die Station."),
        ("", ""),
        ("Erzähler", "Rico trat die Luke auf und stürmte mit den Marines in den kleinen Raum."),
        ("Erzähler", "Sofort begann er, die Leiter hinaufzusteigen."),
        ("Erzähler", "Sara und Lara wollten ihm folgen."),
        ("", ""),
        ("Erzähler", "Dann hörten sie es."),
        ("Erzähler", "Ein langgezogenes Quietschen."),
        ("Erzähler", "Das Geräusch konnte nur von einer sich öffnenden Metalltür stammen."),
        ("", ""),
        ("John", "Lauft!"),
        ("", ""),
        ("Erzähler", "John drehte sich um."),
        ("Erzähler", "Etwas stand im Schatten."),
        ("Erzähler", "Schwarz wie die Nacht."),
        ("Erzähler", "Die Augen glühten schwach in einem undefinierbaren Farbton zwischen Bernstein und Rauch."),
        ("Erzähler", "Das Wesen bewegte sich nicht."),
        ("", ""),
        ("Erzähler", "Dann öffnete es den Mund."),
        ("Erzähler", "Oder zumindest die Stelle, die wie ein Mund wirkte."),
        ("", ""),
        ("Schattenwesen", "Ihr hättet nicht wiederkommen sollen!"),
        ("", ""),
        ("Erzähler", "Die Stimme war kaum zu hören und schien gleichzeitig direkt in Johns Kopf zu entstehen."),
        ("Erzähler", "Dann stieß das Wesen einen schrecklichen Schrei aus und stürzte auf John zu."),
        ("", ""),
        ("John", "Lauft!")
    ],

    ist_kampf=True,

    story_nachher=[
        ("Erzähler", "Das Wesen wurde zurückgedrängt."),
        ("Erzähler", "John wollte gerade zur Leiter laufen, als die Gestalt plötzlich wieder vor ihm stand."),
        ("", ""),
        ("Erzähler", "Es packte ihn und drückte ihn gegen die Wand."),
        ("Erzähler", "Der Druck auf seiner Brust war so stark, dass John kaum noch atmen konnte."),
        ("", ""),
        ("Erzähler", "Er versuchte sich zu befreien, doch seine Kräfte ließen nach."),
        ("", ""),
        ("Erzähler", "Das Wesen beugte sich näher zu ihm."),
        ("Erzähler", "Seine Augen glühten stärker."),
        ("", ""),
        ("Erzähler", "John hatte das Gefühl, dass es direkt durch ihn hindurchblickte."),
        ("", ""),
        ("Erzähler", "In seinem Kopf rauschte es."),
        ("Erzähler", "Fetzen von Worten waren zu hören."),
        ("", ""),
        ("Schattenwesen", "Nicht ... du ..."),
        ("", ""),
        ("Erzähler", "Das Wesen hielt plötzlich inne."),
        ("Erzähler", "Für einige Sekunden bewegte sich nichts."),
        ("", ""),
        ("Erzähler", "Dann ließ es John brutal zu Boden fallen."),
        ("Erzähler", "John blieb benommen liegen."),
        ("", ""),
        ("Erzähler", "Als er wieder aufsah, war das Wesen verschwunden."),
        ("Erzähler", "Es war lautlos in den Schatten zurückgekehrt."),
        ("", ""),
        ("John", "Warum ...?"),
        ("", ""),
        ("Erzähler", "John verstand nicht, warum das Wesen ihn nicht getötet hatte."),
        ("", ""),
        ("Erzähler", "Seine Hände zitterten, als er sich langsam an der Leiter hochzog."),
        ("Erzähler", "Jeder Muskel brannte und sein Herz raste."),
        ("", ""),
        ("Erzähler", "Unter ihm lag nur noch Dunkelheit."),
        ("", ""),
        ("Erzähler", "John stieg weiter nach oben."),
        ("", ""),
        ("Erzähler", "Doch die Worte des Wesens gingen ihm nicht aus dem Kopf."),
        ("", ""),
        ("Schattenwesen", "Nicht ... du ...")
    ]
)


Eine_positive_Ueberraschung_6 = kampangen_kampf( #31
    "Eine positive Überraschung",

    spieler_1="John",
    spieler_2="Sara",
    spieler_3="Rico",
    spieler_4="Lara",

    gegner_1="stationsdrohne",
    gegner_2="infizierter_roboter",

    belohnung=1200,
    ki=3,
    npc_level=12,
    team_groesse_1=4,
    team_groesse_2=2,

    story_vorher=[
        ("Erzähler", "Nach einer gefühlten Ewigkeit erreichte John schließlich das Ende der Leiter."),
        ("Erzähler", "Zu seiner Überraschung befand er sich direkt in der Kommandozentrale der Station."),
        ("Erzähler", "Der Raum sah deutlich anders aus als die Bereiche, die sie zuvor durchquert hatten."),
        ("Erzähler", "Die Wände waren hier noch nicht vollständig von den pulsierenden Adern überwuchert."),
        ("Erzähler", "Überall waren Bildschirme, Terminals und verschiedene Armaturen zu erkennen."),

        ("", ""),

        ("Erzähler", "In der Mitte des Raumes befand sich eine große Hauptarmatur mit unzähligen Knöpfen und Anzeigen."),
        ("Erzähler", "Als John und die anderen sich dem Gerät näherten, öffnete sich ein Terminal."),

        ("", ""),

        ("Erzähler", "Drei Bereiche waren besonders auffällig."),
        ("Erzähler", "Stations Logbuch."),
        ("Erzähler", "AEON STRAIN."),
        ("Erzähler", "Das neue Wir."),

        ("", ""),

        ("Rico", "Das sieht interessant aus."),
        ("John", "Wir lesen das nicht hier."),
        ("Sara", "Warum nicht?"),
        ("John", "Wir nehmen den Speicherkern mit und sehen uns alles auf der Red Horizon in Ruhe an."),

        ("", ""),

        ("Erzähler", "John und Rico begannen, den Speicherkern auszubauen."),
        ("Erzähler", "Kaum hatte John die erste Verbindung gelöst, erloschen mehrere Anzeigen im Raum."),

        ("", ""),

        ("Erzähler", "Ein tiefes Summen ging durch die Kommandozentrale."),
        ("Lara", "Ähm ... ich glaube, wir haben gerade etwas ausgelöst."),

        ("Erzähler", "Aus den Wänden lösten sich zwei Maschinen."),
        ("Erzähler", "Eine Stationsdrohne schwebte langsam in den Raum."),
        ("Erzähler", "Hinter ihr bewegte sich ein beschädigter, von den dunklen Adern überwucherter Roboter."),

        ("Rico", "Na toll."),
        ("John", "Lasst den Speicherkern nicht fallen."),

        ("Erzähler", "Die beiden Maschinen richteten ihre Waffen auf die Gruppe."),

        ("", ""),

    ],

    ist_kampf=True,

    story_nachher=[
        ("Erzähler", "Die letzte Maschine fiel zu Boden."),
        ("Erzähler", "Für einige Sekunden war nur das leise Summen der beschädigten Systeme zu hören."),
        ("", ""),
        ("Rico", "Das war's hoffentlich."),
        ("Sara", "Hoffentlich."),
        ("", ""),
        ("Erzähler", "John überprüfte den Speicherkern."),
        ("John", "Er ist noch intakt."),
        ("", ""),
        ("Erzähler", "Er nahm ihn an sich und sah sich noch einmal in der Kommandozentrale um."),
        ("John", "Wir verschwinden hier."),
        ("", ""),
        ("Erzähler", "Sie machten sich auf den Rückweg zur Red Horizon."),
        ("Erzähler", "Der Weg durch die Station zog sich wie durch einen Nebel."),
        ("Erzähler", "Niemand sprach."),
        ("Erzähler", "Nur das leise Echo ihrer Schritte begleitete sie."),
        ("", ""),
        ("Erzähler", "Einmal blieb Sara stehen und horchte."),
        ("Erzähler", "Tief im Metall war ein leises Kratzen zu hören."),
        ("", ""),
        ("John", "Wir müssen weiter."),
        ("Erzähler", "Sara nickte und folgte ihm."),
        ("", ""),
        ("Erzähler", "Schließlich erreichten sie die Red Horizon."),
        ("Erzähler", "Als sich die Luftschleuse hinter ihnen schloss, ertönte ein tiefes Zischen."),
        ("Erzähler", "Dann war es still."),
        ("", ""),
        ("Sara", "Wir sind wieder zuhause."),
        ("", ""),
        ("Erzähler", "Sara ließ sich in den Pilotensitz fallen und überprüfte die Systeme."),
        ("Sara", "Alles grün."),
        ("", ""),
        ("Erzähler", "John schloss den Speicherkern an den Zentralcomputer an."),
        ("", ""),
        ("John", "Später. Jetzt ruhen wir uns aus.")
    ]
)


Die_Auswertung_6 = kampangen_kampf( #32
    "Die Auswertung",

    story_vorher=[
        ("Erzähler", "Am nächsten Tag begann die Gruppe damit, die Daten des Speicherkerns auszuwerten."),
        ("Erzähler", "Als Erstes öffneten sie das Stations Logbuch."),
        ("", ""),
        ("Stationslogbuch", "Tag 456 nach Start der Projekte."),
        ("Stationslogbuch", "Die Forschungen am Projekt AEON STRAIN werden fortgesetzt."),
        ("Stationslogbuch", "Seit Beginn des Projekts konnten noch keine zufriedenstellenden Ergebnisse erzielt werden."),
        ("Stationslogbuch", "Es sind jedoch erste Fortschritte zu verzeichnen."),
        ("Stationslogbuch", "Das Projekt Das neue Wir verläuft planmäßig."),
        ("Stationslogbuch", "Die Fertigstellung des ersten Produkts wird in etwa zehn Tagen erwartet."),
        ("Stationslogbuch", "Eintrag verfasst durch den marsianischen Anführer."),
        ("", ""),
        ("Stationslogbuch", "Tag 468 nach Start der Projekte."),
        ("Stationslogbuch", "AEON STRAIN: weiterhin nur geringe Fortschritte."),
        ("Stationslogbuch", "Das neue Wir: erster Prototyp fertiggestellt."),
        ("Stationslogbuch", "Der Prototyp erfüllt bisher alle Erwartungen."),
        ("Stationslogbuch", "Eintrag verfasst durch den marsianischen Anführer."),
        ("", ""),
        ("Stationslogbuch", "Tag 475 nach Start der Projekte."),
        ("Stationslogbuch", "Das Projekt Das neue Wir verläuft weiterhin planmäßig."),
        ("Stationslogbuch", "AEON STRAIN: kritischer Zwischenfall."),
        ("Stationslogbuch", "Ein Aeon wurde erfolgreich erschaffen."),
        ("Stationslogbuch", "Das Subjekt reagiert nicht auf Befehle."),
        ("Stationslogbuch", "Es zeigt ein stark ausgeprägtes Bedürfnis nach Nahrungsaufnahme."),
        ("Stationslogbuch", "Mehrere Personen wurden vom Subjekt konsumiert."),
        ("Stationslogbuch", "Einige Personen werden vom Subjekt nicht angegriffen."),
        ("Stationslogbuch", "Der Grund dafür konnte bisher nicht festgestellt werden."),
        ("Stationslogbuch", "Eintrag verfasst durch den marsianischen Anführer."),
        ("", ""),
        ("Stationslogbuch", "Tag 483 nach Start der Projekte."),
        ("Stationslogbuch", "Die Marsianer sind verschwunden."),
        ("Stationslogbuch", "Ausgenommen sind ausschließlich Personen, die vom Aeon nicht angegriffen wurden."),
        ("Stationslogbuch", "Das Subjekt zeigt weiterhin kein Interesse an den Mitgliedern von Das neue Wir."),
        ("Stationslogbuch", "Mögliche Erklärung: Die Mitglieder von Das neue Wir bestehen nicht vollständig aus biologischem Gewebe."),
        ("Stationslogbuch", "Bei Untersuchungen wurde ein Metallskelett festgestellt."),
        ("Stationslogbuch", "Eintrag verfasst durch  Das neue Wir Anführer."),
        ("", ""),
        ("Stationslogbuch", "Tag 488 nach Start der Projekte."),
        ("Stationslogbuch", "Der Aeon greift nun auch Mitglieder von Das neue Wir an."),
        ("Stationslogbuch", "Evakuierungsprotokoll eingeleitet."),
        ("Stationslogbuch", "Das Schiff Sanctuary wird von der Prometheus-Delta-Station nach Prometheus-Prime verlegt."),
        ("Stationslogbuch", "Eintrag verfasst durch  Das neue Wir Anführer."),
        ("", ""),
        ("Stationslogbuch", "Tag 396025 nach Start der Projekte."),
        ("Stationslogbuch", "Automatischer Eintrag."),
        ("Stationslogbuch", "Ein unbekanntes Schiff hat die Verbotene Zone betreten."),
        ("Stationslogbuch", "Protokoll zur Sicherung unbekannter Schiffe aktiviert."),
        ("Stationslogbuch", "Schiff wird in die Station gezogen."),
        ("", ""),
        ("Rico", "Das ist ... ziemlich viel."),
        ("John", "Und es erklärt zumindest einiges.")
    ],

    ist_kampf=False
)


Die_Auswertung_AEON_STRAIN_6 = kampangen_kampf( #33
    "AEON STRAIN",

    story_vorher=[
        ("Erzähler", "Als Nächstes öffneten sie die Datei über das Projekt AEON STRAIN."),
        ("", ""),
        ("Erzähler", "Klassifikation: Unbekannt / nicht-biologisch bestätigt."),
        ("Erzähler", "Ursprung: Herstellung aus —"),
        ("Erzähler", "Beschreibung: Aeon Strain zeigt keine feste Gestalt."),
        ("Erzähler", "Das Phänomen äußert sich als Störung in Raum und Wahrnehmung, begleitet von Flüstern auf allen Frequenzen."),
        ("Erzähler", "Theoretischer Status: Nicht als Lebewesen zu klassifizieren."),
        ("Erzähler", "Beobachtungshinweise: Kontakt mit exponierten Crewmitgliedern führt zu Identitätsfragmentierung,"),
        ("Erzähler", "spontanen Bewegungsabläufen und dem Verlust des eigenen Zeitgefühls."),
        ("Erzähler", "Aufgabe: Taktische Kriegsführung."),
        ("", ""),
        ("Erzähler", "Für einige Sekunden sagte niemand etwas."),
        ("", ""),
        ("Sara", "Das erklärt zumindest einige der Dinge, die wir erlebt haben."),
        ("John", "Und es bestätigt, dass diese Wesen nicht einfach normale Lebewesen sind.")
    ],

    ist_kampf=False
)


Die_Auswertung_Das_neue_Wir_6 = kampangen_kampf( #34
    "Das neue Wir",

    story_vorher=[
        ("Erzähler", "Zum Schluss öffneten sie die Datei über das Projekt Das neue Wir."),
        ("", ""),
        ("Erzähler", "Klassifikation: Robotermensch."),
        ("Erzähler", "Ursprung: Herstellung aus —"),
        ("Erzähler", "Beschreibung: Sieht aus wie ein Marsianer."),
        ("Erzähler", "Theoretischer Status: KI gesteuerter Roboter."),
        ("Erzähler", "Aufgabe: Übernehmen von Aufgaben."),
        ("", ""),
        ("Rico", "Diese Daten lösen zur Abwechslung mal ein paar Fragen."),
        ("John", "Das stimmt."),
        ("", ""),
        ("John", "Wir wissen jetzt, dass das oder die Aliens Aeons heißen."),
        ("John", "Wir wissen aber auch, dass sie hier hergestellt wurden."),
        ("John", "Und das ist nicht wirklich eine gute Nachricht."),
        ("", ""),
        ("Sara", "Es gibt aber auch einen Hinweis darauf, dass einige Marsianer und Roboter überlebt haben."),
        ("Sara", "Sie sind mit der Sanctuary nach Prometheus-Prime geflogen."),
        ("Sara", "Vielleicht finden wir heraus, wo dieser Ort liegt und können auch dorthin fliegen."),
        ("", ""),
        ("Chasker", "Ich werde sofort die besten Forscher darauf ansetzen, diese Dateien genauer zu untersuchen und den Ort zu finden."),
        ("", ""),
        ("Erzähler", "Damit beendete Chasker die Sitzung."),
        ("Erzähler", "Alle gingen wieder an die Arbeit.")
    ],

    ist_kampf=False
)


Die_Vorbereitungen_6 = kampangen_kampf( #35
    "Die Vorbereitungen",

    story_vorher=[
        ("Erzähler", "Während die führenden Forscher daran arbeiteten, nach den Koordinaten zu suchen,"),
        ("Erzähler", "waren John und Lara dabei, die Red Horizon auf den Start vorzubereiten."),
        ("Erzähler", "Sie überprüften alle Anzeigen und kalibrierten die Systeme neu, um sicherzugehen, dass auch wirklich alles glatt lief."),
        ("", ""),
        ("Erzähler", "Sara war unterdessen bei den Reaktoren des Schiffes und kontrollierte, ob sie noch richtig funktionierten und gleichmäßig Strom produzierten."),
        ("", ""),
        ("Erzähler", "Rico war mit einigen Marines dabei, eines der UAVs für den Start vorzubereiten."),
        ("Erzähler", "Nach dem Start sollte das UAV die Marsoberfläche nach weiteren Gebäuden oder möglichen Stationen absuchen."),
        ("Erzähler", "Sie überprüften alle Systeme. Sie begannen bei der Batterie und arbeiteten sich bis zur Kamera vor."),
        ("", ""),
        ("Erzähler", "Als alle ihre Aufgaben erledigt hatten, kehrten sie in den Kommandoraum zurück."),
        ("Erzähler", "Chasker wartete dort bereits auf sie."),
        ("", ""),
        ("Chasker", "Wir haben die Koordinaten."),
        ("", ""),
        ("Erzähler", "Für einen Moment herrschte Erleichterung."),
        ("", ""),
        ("Chasker", "Das einzige Problem ist, dass ich mir nicht sicher bin, ob wir wirklich dorthin fliegen sollten."),
        ("Chasker", "Wir könnten auch zur Erde fliegen und versuchen, den Aeon zu bekämpfen."),
        ("", ""),
        ("Sara", "Ich glaube nicht, dass wir es ohne Hilfe schaffen würden."),
        ("Sara", "Deshalb glaube ich, dass die Koordinaten die bessere Wahl sind."),
        ("John", "Das glaube ich auch."),
        ("", ""),
        ("Erzähler", "Damit war die Entscheidung getroffen."),
        ("Erzähler", "Sie würden zu den Koordinaten fliegen."),
        ("", ""),
        ("Lara", "Was machen wir eigentlich mit dem Aeon in der Isolationszelle?"),
        ("Chasker", "Wir werden ihn erstmal für einige Tests und Beobachtungen hier behalten."),
        ("Chasker", "Irgendwann werden wir ihn allerdings aus der Luftschleuse der Isolationszelle werfen."),
        ("", ""),
        ("Rico", "Ich werde da bestimmt nicht nochmal hineingehen, um ihn aus der Luftschleuse zu schieben!"),
        ("Sara", "Das wirst du auch nicht müssen."),
        ("Sara", "Der Sog wird ihn automatisch hinausziehen."),
        ("", ""),
        ("Erzähler", "Sara grinste leicht."),
        ("Erzähler", "Damit begannen die letzten Vorbereitungen für den Start.")
    ],

    ist_kampf=False
)


Der_Start_6 = kampangen_kampf( #36
    "Der Start",

    story_vorher=[
        ("Erzähler", "Als alle in ihren Sitzen saßen, begann John die Startsequenz."),
        ("", ""),
        ("Erzähler", "Die Triebwerke der Red Horizon begannen zu vibrieren, erst leise, dann wuchs das Grollen zu einem Sturm,"),
        ("Erzähler", "der durch die metallenen Rippen des Schiffes jagte."),
        ("", ""),
        ("Lara", "Klammer 3 reagiert nicht!"),
        ("John", "Verdammt, wenn die sich nicht löst, können wir nicht starten!"),
        ("", ""),
        ("Rico", "Ich geh raus."),
        ("Chasker", "Keine Diskussion. Das ist ein Befehl - ich übernehme."),
        ("", ""),
        ("Erzähler", "John wollte protestieren, doch Chasker hatte bereits die Schleuse betreten."),
        ("", ""),
        ("Chasker", "Wenn ich die Klammer freischneide, habt ihr exakt zehn Sekunden. Danach - Start. Keine Verzögerung."),
        ("Sara", "Aber ... du kommst dann nicht mehr rein."),
        ("Chasker", "Ich weiß."),
        ("", ""),
        ("Erzähler", "Draußen war nur das matte Licht der Notbeleuchtung zu sehen."),
        ("Erzähler", "Chaskers Silhouette bewegte sich träge zwischen den Startklammern."),
        ("Erzähler", "Die Klammer war komplett verdreht."),
        ("", ""),
        ("Erzähler", "Der Plasmabrenner zischte auf. Gleißendes Licht erfüllte das Dock."),
        ("Erzähler", "Funken sprühten über den metallenen Boden, der bereits von den Vibrationen bebte."),
        ("", ""),
        ("Erzähler", "Plötzlich flackerte die Beleuchtung."),
        ("Erzähler", "Ein Schatten huschte über die Wand, wo keiner hätte sein dürfen."),
        ("", ""),
        ("Chasker", "Sara, seht ihr das auch?"),
        ("Sara", "Negativ. Die Kameras zeigen nichts."),
        ("", ""),
        ("Erzähler", "Chasker senkte den Blick wieder auf die Klammer."),
        ("", ""),
        ("Erzähler", "Zwischen den Gitterplatten bewegte sich etwas."),
        ("Erzähler", "Zuerst hielt er es für austretenden schwarzen Schmierstoff."),
        ("Erzähler", "Dann bemerkte er, dass die Substanz gegen die Gravitation nach oben kroch und sich entlang des Metalls zog."),
        ("", ""),
        ("Chasker", "Hier draußen ... ist irgendwas."),
        ("John", "Wiederholen, Commander?"),
        ("Chasker", "Es ... beobachtet."),
        ("", ""),
        ("Erzähler", "Sein Atem beschlug das Visier."),
        ("Erzähler", "Er zwang sich, ruhig zu bleiben und setzte erneut den Brenner an."),
        ("", ""),
        ("Erzähler", "Der Schatten zuckte kurz zurück, als fürchtete er das Licht."),
        ("", ""),
        ("Chasker", "Noch fünf Sekunden."),
        ("", ""),
        ("Erzähler", "Hinter ihm zischte es leise."),
        ("Erzähler", "Die schwarze Substanz bewegte sich wieder vorwärts."),
        ("", ""),
        ("Chasker", "Vier ... drei ..."),
        ("", ""),
        ("Erzähler", "Ein metallisches Kreischen ertönte."),
        ("Erzähler", "Dann folgte ein kurzer Aufschrei."),
        ("", ""),
        ("Erzähler", "Der Funk explodierte in Rauschen."),
        ("", ""),
        ("John", "Commander! Antworten Sie!"),
        ("Erzähler", "Nichts."),
        ("", ""),
        ("Erzähler", "Nur das tiefe Brummen der Triebwerke und ein fremdes, pulsierendes Geräusch waren zu hören."),
        ("", ""),
        ("John", "Er hat es geschafft."),
        ("Lara", "Aber ..."),
        ("John", "Alle Systeme grün."),
        ("Lara", "Er wollte das so.")
    ],

    ist_kampf=False
)


Die_Flucht_6 = kampangen_kampf( #37
    "Die Flucht",

    story_vorher=[
        ("Erzähler", "Die Triebwerke heulten auf."),
        ("Erzähler", "Das gesamte Dock erzitterte."),
        ("Erzähler", "Die Startklammern gaben nach."),
        ("", ""),
        ("Erzähler", "Ein ohrenbetäubender Schlag hallte durch die Halle, als sich die Red Horizon löste."),
        ("Erzähler", "Feuer und Rauch peitschten durch die Gitterböden."),
        ("Erzähler", "Sirenen schrien auf."),
        ("", ""),
        ("Erzähler", "Dann brach das Schiff durch die Schleuse."),
        ("Erzähler", "Keiner sprach."),
        ("", ""),
        ("Erzähler", "Nur das metallische Atmen der Systeme füllte den Raum."),
        ("", ""),
        ("Rico", "Er hat uns rausgebracht."),
        ("", ""),
        ("Erzähler", "John setzte still den Kurs auf die Koordinaten."),
        ("Erzähler", "Die Station wurde hinter ihnen immer kleiner."),
        ("", ""),
        ("Sara", "Wir sollten überprüfen, ob das UAV bereit ist."),
        ("Rico", "Ich kümmere mich darum."),
        ("", ""),
        ("Erzähler", "Rico überprüfte die Verbindung zum UAV."),
        ("Rico", "Verbindung steht."),
        ("", ""),
        ("Erzähler", "Auf einem der Bildschirme erschien das Bild der Kamera."),
        ("", ""),
        ("Lara", "Dann können wir es später auf der Marsoberfläche einsetzen."),
        ("John", "Genau.")
    ],

    ist_kampf=False
)


Kampange_6 = kampange(
    "_06",
    "Down in Mars",
    "sehr schwer",
    37,
    [
        anfangsstory_6,
        Die_Erkundung_6,
        Im_Inneren_6,
        Die_Untersuchungen_6,
        Rueckkehr_6,
        Die_Sitzung_6,

        Der_Traum_6_begin,
        Der_Kampf_im_Traum_6,

        Der_Plan_6,
        Die_Woche_6,
        Der_Abflug_6,
        Der_Flug_6,
        Gefangen_von_der_Marsstation_6,
        Ein_neues_Zuhause_6,
        Der_erste_Kontakt_6,
        Weitere_Sicherheitsdrohnen_6,
        Der_dritte_Kampf_6,
        Die_ersten_Opfer_6,
        Die_Bodycam_6,
        Die_Seuche_6,
        Die_Theorie_6,

        Plan_B_6,

        Der_Traum_6,

        In_der_Hoehle_des_Loewen_6,
        Die_Jagd_6,
        Die_Jagd_2_6,
        Die_Jagd_3_6,
        Die_Jagd_4_6,
        Die_Jagd_5_6,

        Plan_C_6,

        Eine_positive_Ueberraschung_6,

        Die_Auswertung_6,
        Die_Auswertung_AEON_STRAIN_6,
        Die_Auswertung_Das_neue_Wir_6,

        Die_Vorbereitungen_6,
        Der_Start_6,
        Die_Flucht_6,
    ],
    fortschritt=0
)





alle_kampangen = [
    Kampange_1,
    Kampange_2,
    Kampange_3,
    Kampange_4,
    Kampange_5,
    Kampange_6
]