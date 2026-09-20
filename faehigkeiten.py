import charaktere
import status_effekte



# ══════════════════════════════════════════════════════════════
# Fähigkeiten-Übersicht
# ══════════════════════════════════════════════════════════════

# Allgemeine Fähigkeiten:
# - einfacher_angriff
# - einfache_heilung
# - staerkende_heilung
# - blutiger_schlag
# - starker_schlag
# - bleibender_schlag
#
# Aus der Klasse:
#
# - Jakob
#   - Jakobs Basic
#
#
#
# Fünftklässler:
# - radiergummi_wefen
# - er_hat_nichts_gemacht
# - hordenangriff
#
# Cooler Fünftklässler:
# - ey_was_guckst_du
# - sonnenbrille_auf
# - ranzenwurf
#
# Streber:
# - das_ist_falsch
# - hausaufgaben_zeigen
# - musterloesung
#
# Aufsicht:
# - strafarbeit
# - ordnungsruf
#
# Hausmeister:
# - pausenbrot
# - glockenschlag
#
# Direktor:
# - autoritaet
# - glockenschlag
#
# Klassenclown:
# - streich
# - lachanfall
#
# 6.-Klässler:
# - schubser
# - rennen_gehen
# - wütender_schlag
# - voll_drauf
# - noch_wuetender
# - schlag
# - festhalten
# - nicht_weggehen
# - klugscheissen
# - hausaufgaben_helfen
# - ich_hab_einen_plan
# - nerven
# - ablenken
# - hoer_auf
# - cooler_schlag


# ══════════════════════════════════════════════════════════════
# Allgemeine Funktionen
# ══════════════════════════════════════════════════════════════


def HP_verändern(wem, wie_viel):

    charakter = charaktere.Charaktere[wem]

    charakter.hp = round(charakter.hp + wie_viel, 2)

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


# ══════════════════════════════════════════════════════════════
# Fähigkeiten-Klasse
# ══════════════════════════════════════════════════════════════


class faehigkeit:

    def __init__(
        self,
        name: str,
        funktion: object,
        erklaerung: str,
        max_abklingzeit: int,
        abklingzeit: int,
        zieltyp: str
    ):

        self.name = name
        self.funktion = funktion
        self.erklaerung = erklaerung
        self.max_abklingzeit = max_abklingzeit
        self.abklingzeit = abklingzeit
        self.zieltyp = zieltyp


# ══════════════════════════════════════════════════════════════
# Allgemeine Fähigkeiten
# ══════════════════════════════════════════════════════════════


# --- Einfacher Angriff ---

def einfacher_angriff_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.8

    HP_verändern(wen, schaden)


einfacher_angriff = faehigkeit(
    "einfacher_angriff",
    einfacher_angriff_obj,
    "Ein Angriff, der einfachen Schaden verursacht.",
    0,
    0,
    "gegner"
)


# --- Einfache Heilung ---

def einfache_heilung_obj(wer, wen, team=None):

    HP_verändern(wen, 50)


einfache_heilung = faehigkeit(
    "einfache_heilung",
    einfache_heilung_obj,
    "Eine Heilung, die 50 HP wiederherstellt.",
    3,
    0,
    "verbündete"
)


# --- Stärkende Heilung ---

def staerkende_heilung_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.schaden_plus
    )

    HP_verändern(wen, 50)


staerkende_heilung = faehigkeit(
    "staerkende_heilung",
    staerkende_heilung_obj,
    "Eine Heilung, die 50 HP wiederherstellt und den anvisierten Verbündeten stärkt, sodass er mehr Schaden verursacht.",
    4,
    0,
    "verbündete"
)


# --- Blutiger Schlag ---

def blutiger_schlag_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.8

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.schaden_minus
    )

    HP_verändern(wen, schaden)


blutiger_schlag = faehigkeit(
    "blutiger_schlag",
    blutiger_schlag_obj,
    "Ein Angriff, der einfachen Schaden verursacht und den Gegner schwächt, sodass er weniger Schaden verursacht.",
    3,
    0,
    "gegner"
)


# --- Starker Schlag ---

def starker_schlag_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.8

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.betaeubt
    )

    HP_verändern(wen, schaden)


starker_schlag = faehigkeit(
    "starker_schlag",
    starker_schlag_obj,
    "Ein Angriff, der einfachen Schaden verursacht und den Gegner betäubt.",
    4,
    0,
    "gegner"
)


# --- Bleibender Schlag ---

def bleibender_schlag_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.9

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.damage_over_time_1
    )

    HP_verändern(wen, schaden)


bleibender_schlag = faehigkeit(
    "bleibender_schlag",
    bleibender_schlag_obj,
    "Ein Angriff, der einfachen Schaden verursacht und den Gegner mit Schaden über Zeit belegt.",
    3,
    0,
    "gegner"
)

# ══════════════════════════════════════════════════════════════

# Aus der KLasse

# ══════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════
# Jakob
# ══════════════════════════════════════════════════════════════

def jakobs_basic_obj(wer, wen, team=None):

    import geheimes

    schaden = geheimes.geheime_attake_jakob(wer, wen, team)

    HP_verändern(wen, schaden)

jakobs_basic = faehigkeit(
    "jakobs_basic",
    jakobs_basic_obj,
    "GEheim...",
    0,
    0,
    "Gegner"
)
























# ══════════════════════════════════════════════════════════════
# Fünftklässler
# ══════════════════════════════════════════════════════════════


# --- Radiergummi werfen ---

def radiergummi_wefen_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    HP_verändern(wen, schaden)


radiergummi_wefen = faehigkeit(
    "radiergummi_werfen",
    radiergummi_wefen_obj,
    "Der am meisten genutzte Angriff in der Schule. Verursacht einfachen Schaden.",
    0,
    0,
    "gegner"
)


# --- Er hat nichts gemacht ---

def er_hat_nichts_gemacht_obj(wer, wen, team=None):

    charakter = charaktere.Charaktere[wen]

    for status in charakter.status_effekte.copy():

        if status.name != "schaden_plus" and status.name != "healing_over_time_1":
            charakter.status_effekte.remove(status)

    HP_verändern(wer, 20)


er_hat_nichts_gemacht = faehigkeit(
    "er_hat_nichts_gemacht",
    er_hat_nichts_gemacht_obj,
    "Er hat nichts gemacht! Entfernt negative Statuseffekte des Ziels und heilt den Angreifer um 20 HP.",
    4,
    0,
    "verbündete"
)


# --- Hordenangriff ---

def hordenangriff_obj(wer, wen, team):

    gesamtschaden = 0

    for charakter_name in team:

        charakter = charaktere.Charaktere[charakter_name]
        gesamtschaden += charakter.schaden

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.betaeubt
    )

    HP_verändern(wen, gesamtschaden)


hordenangriff = faehigkeit(
    "hordenangriff",
    hordenangriff_obj,
    "Die Gruppe versammelt sich und greifen zusammen an, sodass jeder einmal angreift. Außerdem wird das Ziel betäubt.",
    5,
    3,
    "gegner"
)


# ══════════════════════════════════════════════════════════════
# Cooler Fünftklässler
# ══════════════════════════════════════════════════════════════


# --- Ey, was guckst du? ---

def ey_was_guckst_du_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    HP_verändern(wen, schaden)

    status_effekte.status_effekte_hinzufügen(
        wer,
        status_effekte.schaden_plus
    )


ey_was_guckst_du = faehigkeit(
    "ey_was_guckst_du",
    ey_was_guckst_du_obj,
    "Ey, was guckst du?! Verursacht Schaden und erhöht den eigenen Schaden.",
    0,
    0,
    "gegner"
)


# --- Sonnenbrille auf ---

def sonnenbrille_auf_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(
        wer,
        status_effekte.schaden_plus
    )

    status_effekte.status_effekte_hinzufügen(
        wer,
        status_effekte.healing_over_time_1
    )


sonnenbrille_auf = faehigkeit(
    "sonnenbrille_auf",
    sonnenbrille_auf_obj,
    "Der Fünftklässler setzt seine Sonnenbrille auf und fühlt sich sofort cooler. Er erhält mehr Schaden und Heilung über Zeit.",
    4,
    0,
    "verbündete"
)


# --- Ranzenwurf ---

def ranzenwurf_obj(wer, wen, team=None):

    charakter = charaktere.Charaktere[wer]

    schaden = charakter.schaden * 2

    HP_verändern(wen, schaden)


ranzenwurf = faehigkeit(
    "ranzenwurf",
    ranzenwurf_obj,
    "Der Fünftklässler wirft seinen Ranzen auf den Gegner. Verursacht doppelten Schaden.",
    5,
    0,
    "gegner"
)


# ══════════════════════════════════════════════════════════════
# Streber
# ══════════════════════════════════════════════════════════════


# --- Das ist falsch ---

def das_ist_falsch_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.schaden_minus
    )


das_ist_falsch = faehigkeit(
    "das_ist_falsch",
    das_ist_falsch_obj,
    "Das ist falsch! Der Streber kritisiert den Gegner und verringert dessen Schaden.",
    0,
    0,
    "gegner"
)


# --- Hausaufgaben zeigen ---

def hausaufgaben_zeigen_obj(wer, wen, team=None):

    HP_verändern(wen, 40)


hausaufgaben_zeigen = faehigkeit(
    "hausaufgaben_zeigen",
    hausaufgaben_zeigen_obj,
    "Der Streber zeigt seine Hausaufgaben und hilft dem Verbündeten. Heilt 40 HP.",
    3,
    0,
    "verbündete"
)


# --- Musterlösung ---

def musterloesung_obj(wer, wen, team=None):

    charakter = charaktere.Charaktere[wen]

    for status in charakter.status_effekte.copy():

        if status.name != "schaden_plus" and status.name != "healing_over_time_1":
            charakter.status_effekte.remove(status)


musterloesung = faehigkeit(
    "musterloesung",
    musterloesung_obj,
    "Der Streber zeigt die Musterlösung. Entfernt negative Statuseffekte des Ziels.",
    4,
    0,
    "verbündete"
)


# ══════════════════════════════════════════════════════════════
# Aufsicht
# ══════════════════════════════════════════════════════════════


# --- Strafarbeit ---

def strafarbeit_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.schaden_minus
    )

    HP_verändern(
        wen,
        entgültigen_schaden_berechnen(wer)
    )


strafarbeit = faehigkeit(
    "strafarbeit",
    strafarbeit_obj,
    "Verursacht Schaden und verringert den Schaden des Gegners.",
    3,
    0,
    "gegner"
)


# --- Ordnungsruf ---

def ordnungsruf_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.betaeubt
    )


ordnungsruf = faehigkeit(
    "ordnungsruf",
    ordnungsruf_obj,
    "Ein strenger Ordnungsruf betäubt den Gegner.",
    4,
    0,
    "gegner"
)


# ══════════════════════════════════════════════════════════════
# Hausmeister
# ══════════════════════════════════════════════════════════════


# --- Pausenbrot ---

def pausenbrot_obj(wer, wen, team=None):

    HP_verändern(wen, 55)

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.healing_over_time_1
    )


pausenbrot = faehigkeit(
    "pausenbrot",
    pausenbrot_obj,
    "Heilt einen Verbündeten und gibt ihm Heilung über Zeit.",
    4,
    0,
    "verbündete"
)


# --- Glockenschlag ---

def glockenschlag_obj(wer, wen, team=None):

    HP_verändern(
        wen,
        entgültigen_schaden_berechnen(wer) * 2
    )


glockenschlag = faehigkeit(
    "glockenschlag",
    glockenschlag_obj,
    "Ein harter Schlag mit der Schulglocke verursacht doppelten Schaden.",
    5,
    0,
    "gegner"
)


# ══════════════════════════════════════════════════════════════
# Direktor
# ══════════════════════════════════════════════════════════════


# --- Autorität ---

def autoritaet_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(
        wer,
        status_effekte.schaden_plus
    )

    status_effekte.status_effekte_hinzufügen(
        wer,
        status_effekte.healing_over_time_1
    )


autoritaet = faehigkeit(
    "autoritaet",
    autoritaet_obj,
    "Stärkt den Anwender mit mehr Schaden und Heilung über Zeit.",
    4,
    0,
    "verbündete"
)


# ══════════════════════════════════════════════════════════════
# Klassenclown
# ══════════════════════════════════════════════════════════════


# --- Klassenstreich ---

def streich_obj(wer, wen, team=None):

    HP_verändern(
        wen,
        entgültigen_schaden_berechnen(wer)
    )

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.schaden_minus
    )


streich = faehigkeit(
    "streich",
    streich_obj,
    "Ein fieser Klassenstreich verursacht Schaden und lenkt den Gegner ab.",
    3,
    0,
    "gegner"
)


# --- Lachanfall ---

def lachanfall_obj(wer, wen, team=None):

    HP_verändern(
        wen,
        entgültigen_schaden_berechnen(wer) * 2
    )

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.betaeubt
    )


lachanfall = faehigkeit(
    "lachanfall",
    lachanfall_obj,
    "Der Klassenclown bringt den Gegner zum Lachen und verursacht doppelten Schaden.",
    5,
    0,
    "gegner"
)




# --- 6.-Klässler ---

# --- Schubser ---

def schubser_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    HP_verändern(wen, schaden)

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.schaden_minus
    )


schubser = faehigkeit(
    "schubser",
    schubser_obj,
    "Schubst den Gegner und senkt dessen Schaden.",
    2,
    0,
    "gegner"
)


# --- Rennen gehen ---

def rennen_gehen_obj(wer, wen, team=None):

    HP_verändern(wer, 10)

    status_effekte.status_effekte_hinzufügen(
        wer,
        status_effekte.schaden_plus
    )


rennen_gehen = faehigkeit(
    "rennen_gehen",
    rennen_gehen_obj,
    "Rennt kurz weg, heilt sich und bekommt einen Schadensbonus.",
    3,
    0,
    "verbündete"
)


# --- Wütender Schlag ---

def wütender_schlag_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    HP_verändern(wen, schaden)


wütender_schlag = faehigkeit(
    "wütender_schlag",
    wütender_schlag_obj,
    "Ein einfacher, aber kräftiger Schlag.",
    0,
    0,
    "gegner"
)


# --- Voll drauf ---

def voll_drauf_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    HP_verändern(wen, schaden * 1.5)

    status_effekte.status_effekte_hinzufügen(
        wer,
        status_effekte.schaden_minus
    )


voll_drauf = faehigkeit(
    "voll_drauf",
    voll_drauf_obj,
    "Verursacht hohen Schaden, schwächt danach aber den Angreifer.",
    3,
    0,
    "gegner"
)


# --- Noch wütender ---

def noch_wuetender_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(
        wer,
        status_effekte.schaden_plus
    )


noch_wuetender = faehigkeit(
    "noch_wuetender",
    noch_wuetender_obj,
    "Wird noch wütender und verursacht mehr Schaden.",
    4,
    0,
    "verbündete"
)


# --- Schlag ---

def schlag_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    HP_verändern(wen, schaden)


schlag = faehigkeit(
    "schlag",
    schlag_obj,
    "Ein kräftiger Schlag.",
    0,
    0,
    "gegner"
)


# --- Festhalten ---

def festhalten_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    HP_verändern(wen, schaden)

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.betaeubt
    )


festhalten = faehigkeit(
    "festhalten",
    festhalten_obj,
    "Hält den Gegner fest und betäubt ihn.",
    3,
    0,
    "gegner"
)


# --- Nicht weggehen ---

def nicht_weggehen_obj(wer, wen, team=None):

    HP_verändern(wer, 20)

    status_effekte.status_effekte_hinzufügen(
        wer,
        status_effekte.schaden_plus
    )


nicht_weggehen = faehigkeit(
    "nicht_weggehen",
    nicht_weggehen_obj,
    "Heilt sich und wird stärker.",
    4,
    0,
    "verbündete"
)


# --- Klugscheißen ---

def klugscheissen_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    HP_verändern(wen, schaden)

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.schaden_minus
    )


klugscheissen = faehigkeit(
    "klugscheissen",
    klugscheissen_obj,
    "Nervt den Gegner mit unnötigem Wissen und senkt dessen Schaden.",
    0,
    0,
    "gegner"
)


# --- Hausaufgaben helfen ---

def hausaufgaben_helfen_obj(wer, wen, team=None):

    HP_verändern(wen, 40)


hausaufgaben_helfen = faehigkeit(
    "hausaufgaben_helfen",
    hausaufgaben_helfen_obj,
    "Hilft einem Verbündeten bei den Hausaufgaben und heilt ihn.",
    3,
    0,
    "verbündete"
)


# --- Ich hab einen Plan ---

def ich_hab_einen_plan_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.schaden_plus
    )


ich_hab_einen_plan = faehigkeit(
    "ich_hab_einen_plan",
    ich_hab_einen_plan_obj,
    "Ein Verbündeter bekommt einen Schadensbonus.",
    4,
    0,
    "verbündete"
)


# --- Nerven ---

def nerven_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    HP_verändern(wen, schaden)


nerven = faehigkeit(
    "nerven",
    nerven_obj,
    "Nervt den Gegner.",
    0,
    0,
    "gegner"
)


# --- Ablenken ---

def ablenken_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    HP_verändern(wen, schaden)

    status_effekte.status_effekstatus_effekte_hinzufügent_hinzufuegen(
        wen,
        status_effekte.schaden_minus
    )


ablenken = faehigkeit(
    "ablenken",
    ablenken_obj,
    "Lenkt den Gegner ab und senkt dessen Schaden.",
    2,
    0,
    "gegner"
)


# --- Hör auf ---

def hoer_auf_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.betaeubt
    )


hoer_auf = faehigkeit(
    "hoer_auf",
    hoer_auf_obj,
    "Schreit den Gegner an und betäubt ihn.",
    4,
    0,
    "gegner"
)


# --- Cooler Schlag ---

def cooler_schlag_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer)

    HP_verändern(wen, schaden)


cooler_schlag = faehigkeit(
    "cooler_schlag",
    cooler_schlag_obj,
    "Ein besonders cooler Schlag.",
    0,
    0,
    "gegner"
)


# ══════════════════════════════════════════════════════════════
# Alle Fähigkeiten
# ══════════════════════════════════════════════════════════════


alle_fähigkeiten = [

    # Allgemein
    einfacher_angriff,
    einfache_heilung,
    staerkende_heilung,
    blutiger_schlag,
    starker_schlag,
    bleibender_schlag,

    # Fünftklässler
    radiergummi_wefen,
    er_hat_nichts_gemacht,
    hordenangriff,

    # Cooler Fünftklässler
    ey_was_guckst_du,
    sonnenbrille_auf,
    ranzenwurf,

    # Streber
    das_ist_falsch,
    hausaufgaben_zeigen,
    musterloesung,

    # Aufsicht
    strafarbeit,
    ordnungsruf,

    # Hausmeister
    pausenbrot,
    glockenschlag,

    # Direktor
    autoritaet,

    # Klassenclown
    streich,
    lachanfall,

    # 6.-Klässler
    schubser,
    rennen_gehen,
    wütender_schlag,
    voll_drauf,
    noch_wuetender,
    schlag,
    festhalten,
    nicht_weggehen,
    klugscheissen,
    hausaufgaben_helfen,
    ich_hab_einen_plan,
    nerven,
    ablenken,
    hoer_auf,
    cooler_schlag
]