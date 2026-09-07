import charaktere
import status_effekte



def HP_verändern(wem, wie_viel):
    charaktere.Charaktere[wem].hp = charaktere.Charaktere[wem].hp +wie_viel



def effekte_berügsichtigen(wer):

    to_return = 1

    if status_effekte.status_effekt_vorhanden(wer, "schaden_plus"):
        if status_effekte.status_effekt_vorhanden(wer, "schaden_minus"):
            to_return = 1
        else:
            to_return = 1.3

    if status_effekte.status_effekt_vorhanden(wer, "schaden_minus"):
        if status_effekte.status_effekt_vorhanden(wer, "schaden_plus"):
            to_return = 1
        else:
            to_return = 0.7

    return to_return



def entgültigen_schaden_berechnen(wer):

    faktor_1 = charaktere.Charaktere[wer].schaden
    faktor_2 = effekte_berügsichtigen(wer)

    schaden = faktor_1 * faktor_2

    return schaden



#----------------------Fähigkeiten----------------------#


class faehigkeit:

    def __init__(
        self,
        name : str,
        funktion : object,
        max_abklingzeit : int,
        abklingzeit : int,
        zieltyp : str
        ):

        self.name = name
        self.funktion = funktion
        self.max_abklingzeit = max_abklingzeit
        self.abklingzeit = abklingzeit
        self.zieltyp = zieltyp





def einfacher_angriff_obj(wer, wen):

    schaden =  entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.8

    HP_verändern(wen, schaden)

def einfacher_angriff_erklaerung():
    print("Einfacher Angriff: Ein Angriff, der einfachen Schaden verursacht.")

einfacher_angriff = faehigkeit(
    "einfacher_angriff",
    einfacher_angriff_obj,
    0,
    0,
    "gegner"
)





def blutiger_schlag_obj(wer, wen):

    schaden =  entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.8

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.schaden_minus)

    HP_verändern(wen, schaden)

def blutiger_schlag_erklaerung():
    print("Blutiger Schlag: Ein Angriff, der einfachen Schaden verursacht und den Gegner schwächt, sodass er weniger Schaden verursacht.")

blutiger_schlag = faehigkeit(
    "blutiger_schlag",
    blutiger_schlag_obj,
    2,
    0,
    "gegner"
)





def einfache_heilung_obj(wer, wen):

    HP_verändern(wen, 50)

def einfache_heilung_erklaerung():
    print("Einfache Heilung: Eine Heilung, die 50 HP wiederherstellt.")

einfache_heilung = faehigkeit(
    "einfache_heilung",
    einfache_heilung_obj,
    3,
    0,
    "verbündete"
)





def staerkende_heilung_obj(wer, wen):

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.schaden_plus)

    HP_verändern(wen, 50)

def staerkende_heilung_erklaerung():
    print("Stärkende Heilung: Eine Heilung, die 50 HP wiederherstellt und den anvisierten Verbündeten stärkt, sodass er mehr Schaden verursacht.")

staerkende_heilung = faehigkeit(
    "staerkende_heilung",
    staerkende_heilung_obj,
    4,
    0,
    "verbündete"
)





def starker_schlag_obj(wer, wen):

    schaden =  entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.8

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.betaeubt)

    HP_verändern(wen, schaden)

def starker_schlag_erklaerung():
    print("Starker Schlag: Ein Angriff, der einfachen Schaden verursacht und den Gegner betäubt")

starker_schlag = faehigkeit(
    "starker_schlag",
    starker_schlag_obj,
    4,
    0,
    "gegner"
)





def bleibender_schlag_obj(wer, wen):

    schaden =  entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.8

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.damage_over_time_1)

    HP_verändern(wen, schaden)

def bleibender_schlag_erklaerung():
    print("Bleibender Schlag: Ein Angriff, der einfachen Schaden verursacht und den Gegner mit Schaden über Zeit belegt.")

bleibender_schlag = faehigkeit(
    "bleibender_schlag",
    bleibender_schlag_obj,
    2,
    0,
    "gegner"
)