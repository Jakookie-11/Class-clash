import charaktere
import status_effekte


def HP_verändern(wem, wie_viel):
    charakter = charaktere.Charaktere[wem]

    charakter.hp += wie_viel

    if charakter.hp > charakter.max_hp:
        charakter.hp = charakter.max_hp

    elif charakter.hp <= 0:
        charakter.hp = -1



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
#Eine Faehigkeit besteht immer aus dem oby, also dem modul, was beeinflusst, einer erklärung und einer faehigkeiten klasse, 
#welche sachen wie Abklingzeiten enthält.


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





def einfacher_angriff_obj(wer, wen, team=None):

    schaden =  entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.8

    HP_verändern(wen, schaden)

def einfacher_angriff_erklaerung():
    print("Ein Angriff, der einfachen Schaden verursacht.")

einfacher_angriff = faehigkeit(
    "einfacher_angriff",
    einfacher_angriff_obj,
    0,
    0,
    "gegner"
)





def blutiger_schlag_obj(wer, wen, team=None):

    schaden =  entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.8

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.schaden_minus)

    HP_verändern(wen, schaden)

def blutiger_schlag_erklaerung():
    print("Ein Angriff, der einfachen Schaden verursacht und den Gegner schwächt, sodass er weniger Schaden verursacht.")

blutiger_schlag = faehigkeit(
    "blutiger_schlag",
    blutiger_schlag_obj,
    3,
    0,
    "gegner"
)





def einfache_heilung_obj(wer, wen, team=None):

    HP_verändern(wen, 50)

def einfache_heilung_erklaerung():
    print("Eine Heilung, die 50 HP wiederherstellt.")

einfache_heilung = faehigkeit(
    "einfache_heilung",
    einfache_heilung_obj,
    3,
    0,
    "verbündete"
)





def staerkende_heilung_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.schaden_plus)

    HP_verändern(wen, 50)

def staerkende_heilung_erklaerung():
    print("Eine Heilung, die 50 HP wiederherstellt und den anvisierten Verbündeten stärkt, sodass er mehr Schaden verursacht.")

staerkende_heilung = faehigkeit(
    "staerkende_heilung",
    staerkende_heilung_obj,
    4,
    0,
    "verbündete"
)





def starker_schlag_obj(wer, wen, team=None):

    schaden =  entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.8

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.betaeubt)

    HP_verändern(wen, schaden)

def starker_schlag_erklaerung():
    print("Ein Angriff, der einfachen Schaden verursacht und den Gegner betäubt")

starker_schlag = faehigkeit(
    "starker_schlag",
    starker_schlag_obj,
    4,
    0,
    "gegner"
)





def bleibender_schlag_obj(wer, wen, team=None):

    schaden =  entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.9

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.damage_over_time_1)

    HP_verändern(wen, schaden)

def bleibender_schlag_erklaerung():
    print("Ein Angriff, der einfachen Schaden verursacht und den Gegner mit Schaden über Zeit belegt.")

bleibender_schlag = faehigkeit(
    "bleibender_schlag",
    bleibender_schlag_obj,
    3,
    0,
    "gegner"
)





def hordenangriff_obj(wer, wen, team):

    gesamtschaden = 0

    for charakter_name in team:
        charakter = charaktere.Charaktere[charakter_name]
        gesamtschaden += charakter.schaden

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.betaeubt)

    HP_verändern(wen, gesamtschaden)

def hordenangriff_erklaerung():
    print("Die Fuenftklaessler sammeln sich und kreifen zusammen an, sodas jeder einmal angreift. Außerdem wird das Ziel Beteubt")

hordenangriff = faehigkeit(
    "hordenangriff",
    hordenangriff_obj,
    5,
    3,
    "gegner"
)





def radiergummi_wefen_obj(wer, wen, team=None):

    schaden =  entgültigen_schaden_berechnen(wer)

    HP_verändern(wen, schaden)

def radiergummi_werfen_erklaerung():
    print("Der am meiseten genutzte angriff in der Schule. Verursacht einfachen schaden")

radiergummi_wefen = faehigkeit(
    "radiergummi_werfen",
    radiergummi_wefen_obj,
    0,
    0,
    "gegner"
)





def er_hat_nichts_gemacht_obj(wer, wen, team=None):

    charakter = charaktere.Charaktere[wen]

    for status in charakter.status_effekte.copy():
        if status.name != "schaden_plus" and status.name != "healing_over_time_1":
            charakter.status_effekte.remove(status)

    HP_verändern(wer, 20)

def er_hat_nichts_gemacht_erklaerung():
    print("Er hat nichts gemacht! Entfernt negative Statuseffekte des ziels und heilt Angreifer um 20 HP.")

er_hat_nichts_gemacht = faehigkeit(
    "er_hat_nichts_gemacht",
    er_hat_nichts_gemacht_obj,
    4,
    0,
    "verbündete"
)





def ey_was_guckst_du_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    HP_verändern(wen, schaden)

    status_effekte.status_effekte_hinzufügen(
        wer,
        status_effekte.schaden_plus
    )

def ey_was_guckst_du_erklaerung():
    print("Ey, was guckst du?! Verursacht Schaden und erhöht den eigenen Schaden.")

ey_was_guckst_du = faehigkeit(
    "ey_was_guckst_du",
    ey_was_guckst_du_obj,
    0,
    0,
    "gegner"
)





def sonnenbrille_auf_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(wer,status_effekte.schaden_plus)
    status_effekte.status_effekte_hinzufügen(wer,status_effekte.healing_over_time_1)

def sonnenbrille_auf_erklaerung():
    print("Der Fünftklässler setzt seine Sonnenbrille auf und fühlt sich sofort cooler. Er erhält mehr Schadenund healing over time.")

sonnenbrille_auf = faehigkeit(
    "sonnenbrille_auf",
    sonnenbrille_auf_obj,
    4,
    0,
    "verbündete"
)





def ranzenwurf_obj(wer, wen, team=None):

    charakter = charaktere.Charaktere[wer]

    schaden = charakter.schaden * 2

    HP_verändern(wen, schaden)

def ranzenwurf_erklaerung():
    print("Der Fünftklässler wirft seinen Ranzen auf den Gegner. Verursacht doppelten Schaden.")

ranzenwurf = faehigkeit(
    "ranzenwurf",
    ranzenwurf_obj,
    5,
    0,
    "gegner"
)





def hausaufgaben_zeigen_obj(wer, wen, team=None):

    HP_verändern(wen, 40)

def hausaufgaben_zeigen_erklaerung():
    print("Der Streber zeigt seine Hausaufgaben und hilft dem Verbündeten. Heilt 40 HP.")

hausaufgaben_zeigen = faehigkeit(
    "hausaufgaben_zeigen",
    hausaufgaben_zeigen_obj,
    3,
    0,
    "verbündete"
)





def musterloesung_obj(wer, wen, team=None):

    charakter = charaktere.Charaktere[wen]

    for status in charakter.status_effekte.copy():
        if status.name != "schaden_plus" and status.name != "healing_over_time_1":
            charakter.status_effekte.remove(status)

def musterloesung_erklaerung():
    print("Der Streber zeigt die Musterlösung. Entfernt negative Statuseffekte des Ziels.")

musterloesung = faehigkeit(
    "musterloesung",
    musterloesung_obj,
    4,
    0,
    "verbündete"
)





def das_ist_falsch_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.schaden_minus
    )

def das_ist_falsch_erklaerung():
    print("Das ist falsch! Der Streber kritisiert den Gegner und verringert dessen Schaden.")

das_ist_falsch = faehigkeit(
    "das_ist_falsch",
    das_ist_falsch_obj,
    0,
    0,
    "gegner"
)


alle_fähigkeiten = [
    einfacher_angriff,
    einfache_heilung,
    blutiger_schlag,
    staerkende_heilung,
    starker_schlag,
    bleibender_schlag,
    hordenangriff,
    radiergummi_wefen,
    er_hat_nichts_gemacht, 
    ey_was_guckst_du,
    sonnenbrille_auf,
    ranzenwurf, 
]