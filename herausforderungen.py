
import confic
import ressourcen
import charaktere
import spiel_starten
import time
import kampange
import os

Herausforderungs_fortschritt = []
Herausforderungs_kaempfe_fortschritt = []

# --------------------------------------------------
# Farben
# --------------------------------------------------

SCHWARZ  = "\033[30m"
ROT      = "\033[31m"
GRUEN    = "\033[32m"
GELB     = "\033[33m"
BLAU     = "\033[34m"
MAGENTA  = "\033[35m"
CYAN     = "\033[36m"
WEISS    = "\033[37m"

RESET    = "\033[0m"

# --------------------------------------------------
# Classes
# --------------------------------------------------

class herausforderung:

    def __init__(
        self,
        name=str,
        typ=str,
        art_des_ziels=str,
        nummer_des_ziels=int,
        belohnung_typ=str,
        belohnung_nummer=int,
        abgeholt=False,
        fortschritt=0,
        stufe=1,
        stufen=None,
        abgeschlossen=False,
    ):
        self.name = name
        self.typ = typ
        self.art_des_ziels = art_des_ziels
        self.nummer_des_ziels = nummer_des_ziels
        self.belohnung_typ = belohnung_typ
        self.belohnung_nummer = belohnung_nummer
        self.abgeholt = abgeholt
        self.fortschritt = fortschritt
        self.stufe = stufe
        self.stufen = stufen
        self.abgeschlossen = abgeschlossen


class herausforderungskampf:

    def __init__(
        self,
        gegner_1,
        gegner_2,
        gegner_3,
        gegner_4,
        team_groesse_1=2,
        team_groesse_2=2,
        level=1,
        name=str,
        nummer=int,
        beschreibung=str,
        musik=None,
        typ=str,
        ki= 4,
        belohnung_typ=str,
        belohnung_nummer=int,
        ist_belohnung_2=False,
        belohnung_2_typ=None,
        belohnung_2_nummer=None,
        abgeschlossen=False,
    ):
        self.gegner_1 = gegner_1
        self.gegner_2 = gegner_2
        self.gegner_3 = gegner_3
        self.gegner_4 = gegner_4
        self.team_groesse_1 = team_groesse_1
        self.team_groesse_2 = team_groesse_2
        self.level = level
        self.name = name
        self.nummer = nummer
        self.beschreibung = beschreibung
        self.musik = musik
        self.typ = typ
        self.ki = ki
        self.belohnung_typ = belohnung_typ
        self.belohnung_nummer = belohnung_nummer
        self.ist_belohnung_2 = ist_belohnung_2
        self.belohnung_2_typ = belohnung_2_typ
        self.belohnung_2_nummer = belohnung_2_nummer
        self.abgeschlossen = abgeschlossen


# --------------------------------------------------
# Muss gestzt werden
# --------------------------------------------------
Kampf_Stufen = [
    {"ziel": 5, "belohnung": 300},
    {"ziel": 10, "belohnung": 600},
    {"ziel": 25, "belohnung": 1500},
    {"ziel": 50, "belohnung": 3000},
]
Charakter_Level_Stufen = [
    {"ziel": 5, "belohnung": 300},
    {"ziel": 10, "belohnung": 600},
    {"ziel": 13, "belohnung": 1500},
]


# --------------------------------------------------
# Eigentliches Herausforderungen
# --------------------------------------------------

Ja_Ha = herausforderungskampf(
    gegner_1="Jakob_h",
    gegner_2="Ha",
    gegner_3=None,
    gegner_4=None,
    team_groesse_1=2,
    team_groesse_2=2,
    level=13,
    name="Ja_Ha",
    nummer=1,
    beschreibung="Besiege Jakob und Ha (beide Level 13) in einem Kampf, um die Herausforderung abzuschließen.",
    musik="home.mp3",
    typ="herausforderungskampf",
    ki=4,
    belohnung_typ="Credits",
    belohnung_nummer=7500,
    ist_belohnung_2=True,
    belohnung_2_typ="Material 1",
    belohnung_2_nummer=100
)

der_ultimative_kampf_gegen_die_Fuenftklaessler = herausforderungskampf(
    gegner_1="cooler_fuenftklaessler",
    gegner_2="streber",
    gegner_3="fuenftklaessler",
    gegner_4="fuenftklaessler",
    team_groesse_1=4,
    team_groesse_2=4,
    level=10,
    name="Der ultimative Kampf gegen die Fünftklässler",
    nummer=2,
    beschreibung="Besiege einen Trupp aus Fuenftklaesslern (alle Level 10) in einem Kampf, um die Herausforderung abzuschließen.",
    musik=None,
    typ="herausforderungskampf",
    ki=4,
    belohnung_typ="Credits",
    belohnung_nummer=10000
)

Gewonnene_Kaempfe = herausforderung(
    "Gewonnene_Kaempfe",
    "kampf",
    "gewonnene_kaempfe",
    5,
    "Credits",
    300,
    stufen=Kampf_Stufen
)

Jakob_Leveln = herausforderung(
    "Jakob_Leveln",
    "level",
    "Jakob",
    5,
    "Credits",
    300,
    stufen=Charakter_Level_Stufen
)


John_Leveln = herausforderung(
    "John_Leveln",
    "level",
    "John",
    5,
    "Credits",
    300,
    stufen=Charakter_Level_Stufen
)

Rico_Leveln = herausforderung(
    "Rico_Leveln",
    "level",
    "Rico",
    5,
    "Credits",
    300,
    stufen=Charakter_Level_Stufen
)

Sara_Leveln = herausforderung(
    "Sara_Leveln",
    "level",
    "Sara",
    5,
    "Credits",
    300,
    stufen=Charakter_Level_Stufen
)

Lara_Leveln = herausforderung(
    "Lara_Leveln",
    "level",
    "Lara",
    5,
    "Credits",
    300,
    stufen=Charakter_Level_Stufen
)

Alle_Herausforderungen = [
    Gewonnene_Kaempfe,
    Jakob_Leveln,
    John_Leveln,
    Rico_Leveln,
    Sara_Leveln,
    Lara_Leveln,
    Ja_Ha,
    der_ultimative_kampf_gegen_die_Fuenftklaessler,
]


# --------------------------------------------------

# Funktionen

# --------------------------------------------------

# --------------------------------------------------
# Aktuelle Stufe abrufen
# --------------------------------------------------

def aktuelle_stufe_abrufen(Herausforderung):

    if Herausforderung.stufen:

        if Herausforderung.stufe <= len(Herausforderung.stufen):
            return Herausforderung.stufen[
                Herausforderung.stufe - 1
            ]

        return None

    return {
        "ziel": Herausforderung.nummer_des_ziels,
        "belohnung": Herausforderung.belohnung_nummer
    }


# --------------------------------------------------
# Aktuellen Fortschritt abrufen
# --------------------------------------------------

def aktuellen_fortschritt_abrufen(Herausforderung):

    if Herausforderung.typ == "level":

        charakter = charaktere.Charaktere.get(
            Herausforderung.art_des_ziels
        )

        if charakter is None:
            return 0

        return charakter.level

    return getattr(
        confic,
        Herausforderung.art_des_ziels,
        0
    )


# --------------------------------------------------
# Herausforderung prüfen
# --------------------------------------------------

def herausforderung_erfuellt(Herausforderung):

    if Herausforderung.abgeschlossen:
        return False

    if Herausforderung.abgeholt:
        return False

    stufe = aktuelle_stufe_abrufen(Herausforderung)

    if stufe is None:
        return False

    aktueller_wert = aktuellen_fortschritt_abrufen(
        Herausforderung
    )

    return aktueller_wert >= stufe["ziel"]


# --------------------------------------------------
# Belohnung vergeben
# --------------------------------------------------

def belohnung_vergeben(Herausforderung, belohnung):

    welche_ressource = Herausforderung.belohnung_typ
    wie_viel = belohnung

    ressourcen.ressourcen_verändern(welche_ressource, wie_viel)


# --------------------------------------------------
# Belohnung abholen
# --------------------------------------------------

def belohnung_abholen(Herausforderung):

    if Herausforderung.abgeschlossen:
        print("Alle Stufen wurden bereits abgeschlossen!")
        return

    if Herausforderung.abgeholt:
        print("Belohnung wurde bereits abgeholt!")
        return

    if not herausforderung_erfuellt(Herausforderung):
        print("Herausforderung noch nicht erfüllt!")
        return

    stufe = aktuelle_stufe_abrufen(Herausforderung)

    belohnung = stufe["belohnung"]

    if not belohnung_vergeben(Herausforderung, belohnung):
        return

    print(
        f"{GRUEN}Belohnung abgeholt: "
        f"{belohnung} "
        f"{Herausforderung.belohnung_typ}"
        f"{RESET}"
    )

    # ----------------------------------------------
    # Nächste Stufe freischalten
    # ----------------------------------------------

    if Herausforderung.stufen:

        if Herausforderung.stufe < len(Herausforderung.stufen):

            Herausforderung.stufe += 1
            Herausforderung.abgeholt = False

            print(
                f"{CYAN}Nächste Stufe freigeschaltet: "
                f"{Herausforderung.stufe}{RESET}"
            )

        else:

            Herausforderung.abgeschlossen = True
            Herausforderung.abgeholt = True

            print(
                f"{GRUEN}Alle Stufen abgeschlossen!{RESET}"
            )

    else:

        Herausforderung.abgeschlossen = True
        Herausforderung.abgeholt = True


# --------------------------------------------------
# Herausforderungsfortschritte speichern
# --------------------------------------------------

def Herausforderungs_fortschritt_speichern():

    Herausforderungs_fortschritt.clear()

    for Herausforderung in Alle_Herausforderungen:

        if Herausforderung.typ == "herausforderungskampf":
            continue

        Herausforderungs_fortschritt.append({
            "name": Herausforderung.name,
            "stufe": getattr(Herausforderung, "stufe", 1),
            "abgeholt": getattr(Herausforderung, "abgeholt", False),
            "abgeschlossen": Herausforderung.abgeschlossen,
        })

    return Herausforderungs_fortschritt

def Herausforderungs_kampf_fortschritt_speichern():

    Herausforderungs_kaempfe_fortschritt.clear()

    for Herausforderung in Alle_Herausforderungen:

        if Herausforderung.typ != "herausforderungskampf":
            continue

        Herausforderungs_kaempfe_fortschritt.append({
            "name": Herausforderung.name,
            "abgeschlossen": Herausforderung.abgeschlossen,
        })

    return Herausforderungs_kaempfe_fortschritt


# --------------------------------------------------
# Herausforderungsfortschritt laden
# --------------------------------------------------

def Herausforderungs_fortschritt_laden(gespeicherte_daten,):

    # Normale Herausforderungen laden
    for gespeicherte in gespeicherte_daten:

        for Herausforderung in Alle_Herausforderungen:

            if Herausforderung.typ == "herausforderungskampf":
                continue

            if Herausforderung.name == gespeicherte["name"]:

                if hasattr(Herausforderung, "stufe"):
                    Herausforderung.stufe = gespeicherte.get("stufe", 1)

                if hasattr(Herausforderung, "abgeholt"):
                    Herausforderung.abgeholt = gespeicherte.get("abgeholt", False)

                Herausforderung.abgeschlossen = gespeicherte.get("abgeschlossen", False)

                break

    # Herausforderungskaempfe laden
    for gespeicherte in gespeicherte_daten:

        for Herausforderung in Alle_Herausforderungen:

            if Herausforderung.typ != "herausforderungskampf":
                continue

            if Herausforderung.name == gespeicherte["name"]:

                Herausforderung.abgeschlossen = gespeicherte.get("abgeschlossen", False)

                break


# --------------------------------------------------
# Herausforderungsmenü
# --------------------------------------------------

def herausforderungen(spieler_name):

    print(f"{CYAN}═══════════════════════════════")
    print("     Herausforderungen")
    print(f"═══════════════════════════════{RESET}")
    print()

    for Herausforderung in Alle_Herausforderungen:

        if Herausforderung.typ == "herausforderungskampf":
            continue

        print(f"{BLAU}{Herausforderung.name}{RESET}")

        if Herausforderung.abgeschlossen:

            print(f"{GRUEN}Alle Stufen abgeschlossen!{RESET}")
            print()

            continue

        stufe = aktuelle_stufe_abrufen(Herausforderung)

        if stufe is None:
            continue

        ziel = stufe["ziel"]
        belohnung = stufe["belohnung"]

        aktueller_wert = aktuellen_fortschritt_abrufen(Herausforderung)

        print(f"Stufe: {Herausforderung.stufe}")
        print(f"Fortschritt: "f"{min(aktueller_wert, ziel)}/{ziel}")
        print(f"Belohnung: "f"{belohnung} "f"{Herausforderung.belohnung_typ}")

        if Herausforderung.abgeholt:
            print(f"{GRUEN}Belohnung bereits abgeholt{RESET}")

        elif herausforderung_erfuellt(Herausforderung):
            print(f"{GELB}Herausforderung erfüllt!{RESET}")

            auswahl = input("Belohnung abholen? (y/n): ").lower()

            if auswahl == "y":
                belohnung_abholen(Herausforderung)

        else:
            print(f"{GELB}Noch nicht erfüllt{RESET}")
        print()

    input("Drücke Enter zum Fortfahren...")






def herausforderungskaempfe(spieler_name):

    while True:
        os.system(confic.terminal_clear)

        print(f"{CYAN}═══════════════════════════════")
        print("     Herausforderungskaempfe")
        print(f"═══════════════════════════════{RESET}")
        print()

        for Herausforderung in Alle_Herausforderungen:

            if Herausforderung.typ != "herausforderungskampf":
                continue

            print(f"{BLAU}[{Herausforderung.nummer}] {Herausforderung.name}{RESET}")
            print(f"Belohnung: {Herausforderung.belohnung_nummer} {Herausforderung.belohnung_typ}")
            print(f"Beschreibung: {Herausforderung.beschreibung}")

            if Herausforderung.abgeschlossen:
                print(f"{GRUEN}Belohnung bereits abgeholt{RESET}")

            else:
                print(f"{GELB}Noch nicht erfüllt{RESET}")
            print()

        wahl = input("Wähle eine Herausforderung (Nummer)/[0]zurueck: ")

        #safe check for exit
        if wahl == "0":
            return

        if not wahl.isdigit():
            print(f"{ROT}Ungültige Eingabe!{RESET}")
            continue

        #richtigen kampf finden
        wahl = int(wahl)

        ausgewaehlte_herausforderung = None

        for Herausforderung in Alle_Herausforderungen:

            if Herausforderung.typ != "herausforderungskampf":
                continue

            if Herausforderung.nummer == wahl:
                ausgewaehlte_herausforderung = Herausforderung
                break

        if ausgewaehlte_herausforderung is None:
            print(f"{ROT}Herausforderung nicht gefunden!{RESET}")
            continue

        #eignen Kampf starten
        team_2 = [gegner
            for gegner in [
                ausgewaehlte_herausforderung.gegner_1,
                ausgewaehlte_herausforderung.gegner_2,
                ausgewaehlte_herausforderung.gegner_3,
                ausgewaehlte_herausforderung.gegner_4,
            ]
            if gegner is not None
        ]

        if len(team_2) < 2:
            print("Es müssen mindestens 2 Gegner vorhanden sein!")
            time.sleep(5)
            return
        
        team_groesse_1 = ausgewaehlte_herausforderung.team_groesse_1
        team_groesse_2 = ausgewaehlte_herausforderung.team_groesse_2
        ki = ausgewaehlte_herausforderung.ki
        musik = ausgewaehlte_herausforderung.musik

        kampange.npc_level_setzen(level=ausgewaehlte_herausforderung.level, Leader_2=ausgewaehlte_herausforderung.gegner_1, spieler_2_2=ausgewaehlte_herausforderung.gegner_2, spieler_3_2=ausgewaehlte_herausforderung.gegner_3, spieler_4_2=ausgewaehlte_herausforderung.gegner_4)

        is_win = spiel_starten.kampf(team_2=team_2, team_groesse_1=team_groesse_1,team_groesse_2=team_groesse_2, Ki=ki, gegner_ki=True, musik=musik)

        if is_win==1:

            print(f"{GRUEN}══════════════════════════════════")
            print("          KAMPF GEWONNEN!")
            print(f"══════════════════════════════════{RESET}")
            print()
            print(f"Du hast die Herausforderung")
            print(f"{GELB}{Herausforderung.name}{RESET}")
            print("erfolgreich abgeschlossen!")
            print()
            if not Herausforderung.abgeschlossen:
                print(f"Belohnung: {Herausforderung.belohnung_nummer} "f"{Herausforderung.belohnung_typ}")
                print()
            print("[1] Weiter")
            print("[0] Zurück")

            kampange.level_zuruecksetzen(ausgewaehlte_herausforderung.gegner_1)
            kampange.level_zuruecksetzen(ausgewaehlte_herausforderung.gegner_2)
            kampange.level_zuruecksetzen(ausgewaehlte_herausforderung.gegner_3)
            kampange.level_zuruecksetzen(ausgewaehlte_herausforderung.gegner_4)

            if not Herausforderung.abgeschlossen:
                if not Herausforderung.ist_belohnung_2:
                    belohnung_vergeben(Herausforderung, Herausforderung.belohnung_nummer)
                    
                elif Herausforderung.ist_belohnung_2:
                    belohnung_vergeben(Herausforderung, Herausforderung.belohnung_nummer)
                    belohnung_vergeben(Herausforderung, Herausforderung.belohnung_2_nummer)

            wahl = input("Auswahl: ")

            if wahl == "1":
                continue

            elif wahl == "0":
                return
