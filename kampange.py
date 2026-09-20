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
        gegner_1,
        gegner_2,
        gegner_3=None,
        gegner_4=None,
        belohnung=0,
        ki=1,
        npc_level=1,
        team_groesse=2,
        story_vorher=None,
        story_nachher=None
    ):
        self.name = name
        self.gegner_1 = gegner_1
        self.gegner_2 = gegner_2
        self.gegner_3 = gegner_3
        self.gegner_4 = gegner_4
        self.belohnung = belohnung
        self.ki = ki
        self.npc_level = npc_level
        self.team_groesse = team_groesse
        self.story_vorher = story_vorher
        self.story_nachher = story_nachher

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

    for sprecher, text in dialog:

        print(f"{sprecher :20}: {text}")
        print()
        time.sleep(2)

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

        for i in range(level -1):

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

                # ══════════════════════════════════════════════════════════════
                # Eigentlicher Kampf
                # ══════════════════════════════════════════════════════════════

                ausgewaehlter_kampf = kampange.kaempfe[wahl - 1]

                npc_level_setzen(ausgewaehlter_kampf.npc_level, ausgewaehlter_kampf.gegner_1, ausgewaehlter_kampf.gegner_2, ausgewaehlter_kampf.gegner_3, ausgewaehlter_kampf.gegner_4)

                print()
                print(f"Du startest: {ausgewaehlter_kampf.name}")
                time.sleep(2)

                dialog_anzeigen(ausgewaehlter_kampf.story_vorher)

                os.system(confic.terminal_clear)

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
    "Die Liste",
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
    "Projekt K",
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


alle_kampangen = [
    Kampange_1,
    Kampange_2,
    Kampange_3,
    Kampange_4,
    Kampange_5
]