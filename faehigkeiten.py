import charaktere
import status_effekte


# ══════════════════════════════════════════════════════════════
# Allgemeine Funktionen
# ══════════════════════════════════════════════════════════════


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


# ══════════════════════════════════════════════════════════════
# Fähigkeiten-Klasse
# ══════════════════════════════════════════════════════════════

# Eine Fähigkeit besteht immer aus:
# - dem Objekt, also der Funktion, die etwas beeinflusst
# - einer Erklärung
# - der Fähigkeiten-Klasse, welche Sachen wie Abklingzeiten enthält


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
# Fähigkeiten des Fünftklässlers
# ══════════════════════════════════════════════════════════════


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
    "Die Fünftklässler sammeln sich und greifen zusammen an, sodass jeder einmal angreift. Außerdem wird das Ziel betäubt.",
    5,
    3,
    "gegner"
)


# ══════════════════════════════════════════════════════════════
# Fähigkeiten des coolen Fünftklässlers
# ══════════════════════════════════════════════════════════════


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
# Fähigkeiten des Strebers
# ══════════════════════════════════════════════════════════════


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


def kreidewurf_obj(wer, wen, team=None):
    HP_verändern(wen, entgültigen_schaden_berechnen(wer))


kreidewurf = faehigkeit(
    "kreidewurf",
    kreidewurf_obj,
    "Wirft Kreide und verursacht normalen Schaden.",
    0,
    0,
    "gegner"
)


def strafarbeit_obj(wer, wen, team=None):
    status_effekte.status_effekte_hinzufügen(wen, status_effekte.schaden_minus)
    HP_verändern(wen, entgültigen_schaden_berechnen(wer))


strafarbeit = faehigkeit(
    "strafarbeit",
    strafarbeit_obj,
    "Verursacht Schaden und verringert den Schaden des Gegners.",
    3,
    0,
    "gegner"
)


def ordnungsruf_obj(wer, wen, team=None):
    status_effekte.status_effekte_hinzufügen(wen, status_effekte.betaeubt)


ordnungsruf = faehigkeit(
    "ordnungsruf",
    ordnungsruf_obj,
    "Ein strenger Ordnungsruf betäubt den Gegner.",
    4,
    0,
    "gegner"
)


def pausenbrot_obj(wer, wen, team=None):
    HP_verändern(wen, 55)
    status_effekte.status_effekte_hinzufügen(wen, status_effekte.healing_over_time_1)


pausenbrot = faehigkeit(
    "pausenbrot",
    pausenbrot_obj,
    "Heilt einen Verbündeten und gibt ihm Heilung über Zeit.",
    4,
    0,
    "verbündete"
)


def glockenschlag_obj(wer, wen, team=None):
    HP_verändern(wen, entgültigen_schaden_berechnen(wer) * 2)


glockenschlag = faehigkeit(
    "glockenschlag",
    glockenschlag_obj,
    "Ein harter Schlag mit der Schulglocke verursacht doppelten Schaden.",
    5,
    0,
    "gegner"
)


def autoritaet_obj(wer, wen, team=None):
    status_effekte.status_effekte_hinzufügen(wer, status_effekte.schaden_plus)
    status_effekte.status_effekte_hinzufügen(wer, status_effekte.healing_over_time_1)


autoritaet = faehigkeit(
    "autoritaet",
    autoritaet_obj,
    "Stärkt den Anwender mit mehr Schaden und Heilung über Zeit.",
    4,
    0,
    "verbündete"
)


def besenstreich_obj(wer, wen, team=None):
    HP_verändern(wen, entgültigen_schaden_berechnen(wer))
    status_effekte.status_effekte_hinzufügen(wen, status_effekte.damage_over_time_1)


besenstreich = faehigkeit(
    "besenstreich",
    besenstreich_obj,
    "Verursacht Schaden und Schaden über Zeit.",
    3,
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
    kreidewurf,
    strafarbeit,
    ordnungsruf,
    pausenbrot,
    glockenschlag,
    autoritaet,
    besenstreich
]