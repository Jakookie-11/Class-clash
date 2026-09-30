
import confic
import ressourcen
import charaktere

Herausforderungs_fortschritt = []

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

Alle_Herausforderungen = [
    Gewonnene_Kaempfe,
    Jakob_Leveln,
]


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

    if Herausforderung.belohnung_typ == "Credits":

        ressourcen.ressourcen["Credits"] += belohnung

    elif Herausforderung.belohnung_typ == "M_Credits":

        ressourcen.ressourcen["M_Credits"] += belohnung

    else:
        print("Unbekannter Belohnungstyp!")
        return False

    return True


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
# Herausforderungsfortschritt speichern
# --------------------------------------------------

def Herausforderungs_fortschritt_speichern():

    Herausforderungs_fortschritt.clear()

    for Herausforderung in Alle_Herausforderungen:

        Herausforderungs_fortschritt.append({
            "name": Herausforderung.name,
            "stufe": Herausforderung.stufe,
            "abgeholt": Herausforderung.abgeholt,
            "abgeschlossen": Herausforderung.abgeschlossen,
        })

    return Herausforderungs_fortschritt


# --------------------------------------------------
# Herausforderungsfortschritt laden
# --------------------------------------------------

def Herausforderungs_fortschritt_laden(
    gespeicherte_daten
):

    for gespeicherte in gespeicherte_daten:

        for Herausforderung in Alle_Herausforderungen:

            if Herausforderung.name == gespeicherte["name"]:

                Herausforderung.stufe = gespeicherte.get(
                    "stufe", 1
                )

                Herausforderung.abgeholt = gespeicherte.get(
                    "abgeholt", False
                )

                Herausforderung.abgeschlossen = gespeicherte.get(
                    "abgeschlossen", False
                )

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

        print(
            f"{BLAU}{Herausforderung.name}{RESET}"
        )

        if Herausforderung.abgeschlossen:

            print(f"{GRUEN}Alle Stufen abgeschlossen!{RESET}")
            print()

            continue

        stufe = aktuelle_stufe_abrufen(Herausforderung)

        if stufe is None:
            continue

        ziel = stufe["ziel"]
        belohnung = stufe["belohnung"]

        aktueller_wert = aktuellen_fortschritt_abrufen(
            Herausforderung
        )

        print(
            f"Stufe: {Herausforderung.stufe}"
        )

        print(
            f"Fortschritt: "
            f"{min(aktueller_wert, ziel)}/{ziel}"
        )

        print(
            f"Belohnung: "
            f"{belohnung} "
            f"{Herausforderung.belohnung_typ}"
        )

        if Herausforderung.abgeholt:

            print(
                f"{GRUEN}Belohnung bereits abgeholt{RESET}"
            )

        elif herausforderung_erfuellt(Herausforderung):

            print(
                f"{GELB}Herausforderung erfüllt!{RESET}"
            )

            auswahl = input(
                "Belohnung abholen? (y/n): "
            ).lower()

            if auswahl == "y":
                belohnung_abholen(Herausforderung)

        else:

            print(
                f"{GELB}Noch nicht erfüllt{RESET}"
            )

        print()

    input("Drücke Enter zum Fortfahren...")