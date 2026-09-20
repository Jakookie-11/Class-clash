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

        print(f"{sprecher :13}: {text}")
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
    npc_level=1,
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
    npc_level=1,
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
    npc_level=1,
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
    npc_level=2,
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
    npc_level=2,
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
    npc_level=2,
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
    npc_level=3,
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
    npc_level=3,
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
    npc_level=3,
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
    ki=3,
    npc_level=4,
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


alle_kampangen = [
    Kampange_1,
    Kampange_2,
    Kampange_3
]