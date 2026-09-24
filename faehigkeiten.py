import charaktere
import status_effekte
import random



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

    if wie_viel < 0:

        if status_effekte.status_effekt_vorhanden(wem, "schaden_erhalten_minus"):
            wie_viel *= 0.7

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
# Generell
# ══════════════════════════════════════════════════════════════

def einfacher_angriff_b_obj(wer, wen, team=None):

    import geheimes

    schaden = geheimes.einfacher_angriff_b_obj(wer, wen, team)

    HP_verändern(wen, schaden)

einfacher_angriff_b = faehigkeit(
    "einfacher_angriff_b",
    einfacher_angriff_b_obj,
    "Geheim...",
    0,
    0,
    "gegner"
)


def einfacher_angriff_g_obj(wer, wen, team=None):

    import geheimes

    schaden = geheimes.einfacher_angriff_g_obj(wer, wen, team)

    HP_verändern(wen, schaden)

einfacher_angriff_g = faehigkeit(
    "einfacher_angriff_g",
    einfacher_angriff_g_obj,
    "Geheim...",
    0,
    0,
    "gegner"
)

# ══════════════════════════════════════════════════════════════
# Jakob
# ══════════════════════════════════════════════════════════════

def jakobs_basic_obj(wer, wen, team_1, team_2):

    import geheimes

    schaden = geheimes.geheime_attake_jakob(wer, wen, team_1, team_2)

    HP_verändern(wen, schaden)

jakobs_basic = faehigkeit(
    "jakobs_basic",
    jakobs_basic_obj,
    "Geheim...",
    0,
    0,
    "gegner"
)

# ══════════════════════════════════════════════════════════════
# Max
# ══════════════════════════════════════════════════════════════

def knielauf_obj(wer, wen, team, team_2):

    import geheimes

    schaden = geheimes.einfacher_angriff_b_obj(wer, wen, team)

    charakter = charaktere.Charaktere[wen]

    if charakter.gender == "5":
        schaden = schaden * 2
    if charakter.gender == "6":
        schaden = schaden * 1.5

    for gegner in team_2:
        ziel_charakter = charaktere.Charaktere[gegner]

        if ziel_charakter.gender != "5" and ziel_charakter.gender != "6":
            continue

        HP_verändern(gegner, schaden)

knielauf = faehigkeit(
    "knielauf",
    knielauf_obj,
    "Max lauuft durch die Menge an Kindern. Er kickt jedem 5/6 Klaessler aus dem Gegnerteam ins Gesicht.",
    5,
    1,
    "gegner"
)

# ══════════════════════════════════════════════════════════════
# Noah
# ══════════════════════════════════════════════════════════════

def gib_mir_die_roehre_obj(wer, wen, team_1):

    import geheimes

    schaden = geheimes.einfacher_angriff_b_obj(wer, wen, team_1)

    if wen == "max":
        schaden = schaden * 2
        status_effekte.status_effekte_hinzufügen(wen, status_effekte.betaeubt)

    else:
        schaden = schaden * 1.5

    return schaden

gib_mir_die_roehre = faehigkeit(
    "gib_mir_die_roehre",
    gib_mir_die_roehre_obj,
    "Noah klopft an die tür des gegners und laesst ihn nicht schlafen, sobald er rauskommt schnappt sich Noah die Roehre und schlaegt den Gegner.",
    3,
    0,
    "gegner"
)


# ══════════════════════════════════════════════════════════════
# Sascha
# ══════════════════════════════════════════════════════════════

def leberkaesbroetchen_essen_obj(wer, wen, team=None):

    HP_verändern(wer, 70)


leberkaesbroetchen_essen = faehigkeit(
    "Leberkaesbroetchen_essen",
    leberkaesbroetchen_essen_obj,
    "Sascha isst ein Leberkaesbroetchen nud heilt sich dadurch um 70-HP.",
    3,
    0,
    "selbst"
)


















# ══════════════════════════════════════════════════════════════



# ══════════════════════════════════════════════════════════════

# Down in Mars

# ══════════════════════════════════════════════════════════════



# ══════════════════════════════════════════════════════════════



# ============================================================
# John
# ============================================================

def john_geziehlter_schuss_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 1.5

    HP_verändern(wen, schaden)

john_geziehlter_schuss = faehigkeit(
    "john_geziehlter_schuss",
    john_geziehlter_schuss_obj,
    "John führt einen gezielten Schuss aus, der erhöhten Schaden verursacht.",
    2,
    0,
    "gegner"
)


def john_taktischer_angriff_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 1.2

    HP_verändern(wen, schaden)

    status_effekte.status_effekte_hinzufügen(wer, status_effekte.schaden_plus)

john_taktischer_angriff = faehigkeit(
    "john_taktischer_angriff",
    john_taktischer_angriff_obj,
    "John greift einen Gegner an und erhöht anschließend seinen eigenen Schaden.",
    3,
    0,
    "gegner"
)


# ============================================================
# Sara
# ============================================================

def sara_geziehlter_schuss_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 1.3

    HP_verändern(wen, schaden)

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.schaden_minus)

sara_geziehlter_schuss = faehigkeit(
    "sara_geziehlter_schuss",
    sara_geziehlter_schuss_obj,
    "Sara verursacht erhöhten Schaden und verringert den Schaden des getroffenen Gegners.",
    2,
    0,
    "gegner"
)


def sara_ausweichen_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 1.2

    HP_verändern(wen, schaden)

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.betaeubt)

sara_ausweichen = faehigkeit(
    "sara_ausweichen",
    sara_ausweichen_obj,
    "Sara führt einen schnellen Ausweichangriff aus, wodurch der gegner beteubt wird.",
    3,
    0,
    "gegner"
)


# ============================================================
# Lara
# ============================================================

def lara_erste_hilfe_obj(wer, wen, team=None):

    heilung = 60

    charakter = charaktere.Charaktere[wen]

    charakter.hp += heilung

    if charakter.hp > charakter.max_hp:
        charakter.hp = charakter.max_hp

lara_erste_hilfe = faehigkeit(
    "lara_erste_hilfe",
    lara_erste_hilfe_obj,
    "Lara heilt einen Verbündeten um 60-HP.",
    4,
    0,
    "verbündete"
)


def lara_unterstuetzung_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(
        wen,
        status_effekte.schaden_plus
    )

lara_unterstuetzung = faehigkeit(
    "lara_unterstuetzung",
    lara_unterstuetzung_obj,
    "Lara erhöht vorübergehend den Schaden eines Verbündeten.",
    3,
    0,
    "verbündete"
)


# ============================================================
# Rico
# ============================================================

def rico_starker_schuss_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 1.7

    HP_verändern(wen, schaden)

rico_starker_schuss = faehigkeit(
    "rico_starker_schuss",
    rico_starker_schuss_obj,
    "Rico führt einen starken Schuss aus, der hohen Schaden verursacht.",
    2,
    0,
    "gegner"
)


def rico_feuerstoss_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 2

    HP_verändern(wen, schaden)

rico_feuerstoss = faehigkeit(
    "rico_feuerstoss",
    rico_feuerstoss_obj,
    "Rico führt einen besonders starken Angriff aus.",
    4,
    0,
    "gegner"
)


# ============================================================
# Chasker
# ============================================================

def chasker_schutz_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(
        wer,
        status_effekte.schaden_erhalten_minus
    )

chasker_schutz = faehigkeit(
    "chasker_schutz",
    chasker_schutz_obj,
    "Chasker erhält für längere Zeit 30 % weniger Schaden.",
    3,
    0,
    "selbst"
)


def chasker_schwerer_angriff_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 2

    HP_verändern(wen, schaden)

chasker_schwerer_angriff = faehigkeit(
    "chasker_schwerer_angriff",
    chasker_schwerer_angriff_obj,
    "Chasker führt einen besonders starken Angriff aus.",
    4,
    0,
    "gegner"
)


# ══════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════

# Down in Mars Gegner

# ══════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════
# Mars-Sicherheitsdrohne
# ══════════════════════════════════════════════════════════════

def mars_sicherheitsdrohne_stoerimpuls_obj(wer, wen, team=None):

    if random.random() < 0.4:
        status_effekte.status_effekte_hinzufügen(wen, status_effekte.betaeubt)
    else:
        schaden = entgültigen_schaden_berechnen(wer)
        HP_verändern(wen, schaden)

mars_sicherheitsdrohne_stoerimpuls = faehigkeit(
    "mars_sicherheitsdrohne_stoerimpuls",
    mars_sicherheitsdrohne_stoerimpuls_obj,
    "Die Drohne setzt einen Störimpuls ein. Mit 40 % Wahrscheinlichkeit wird das Ziel betäubt, ansonsten erleidet es Schaden.",
    2,
    0,
    "gegner"
)


def mars_sicherheitsdrohne_scan_obj(wer, wen, team=None):

    if random.random() < 0.5:
        status_effekte.status_effekte_hinzufügen(wer, status_effekte.schaden_plus)

mars_sicherheitsdrohne_scan = faehigkeit(
    "mars_sicherheitsdrohne_scan",
    mars_sicherheitsdrohne_scan_obj,
    "Die Drohne scannt ihr Ziel. Mit 50 % Wahrscheinlichkeit erhöht sie ihren eigenen Schaden.",
    3,
    0,
    "selbst"
)


# ══════════════════════════════════════════════════════════════
# Mars-Wachroboter
# ══════════════════════════════════════════════════════════════

def mars_wachroboter_stoss_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 1.3
    HP_verändern(wen, schaden)

mars_wachroboter_stoss = faehigkeit(
    "mars_wachroboter_stoss",
    mars_wachroboter_stoss_obj,
    "Der Wachroboter führt einen verstärkten Angriff aus.",
    2,
    0,
    "gegner"
)


def mars_wachroboter_schild_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(wer, status_effekte.schaden_erhalten_minus)

mars_wachroboter_schild = faehigkeit(
    "mars_wachroboter_schild",
    mars_wachroboter_schild_obj,
    "Der Wachroboter aktiviert seinen Schutzschild und erleidet weniger Schaden.",
    3,
    0,
    "selbst"
)


# ══════════════════════════════════════════════════════════════
# Marsianischer Wächter
# ══════════════════════════════════════════════════════════════

def marsianischer_waechter_schild_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(wer, status_effekte.schaden_erhalten_minus)

marsianischer_waechter_schild = faehigkeit(
    "marsianischer_waechter_schild",
    marsianischer_waechter_schild_obj,
    "Der Wächter aktiviert seine Verteidigung und erleidet weniger Schaden.",
    3,
    0,
    "selbst"
)


def marsianischer_waechter_markieren_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.schaden_minus)

marsianischer_waechter_markieren = faehigkeit(
    "marsianischer_waechter_markieren",
    marsianischer_waechter_markieren_obj,
    "Der Wächter markiert einen Gegner und schwächt dessen Angriffe.",
    2,
    0,
    "gegner"
)


# ══════════════════════════════════════════════════════════════
# Marsianischer Soldat
# ══════════════════════════════════════════════════════════════

def marsianischer_soldat_salvo_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 1.6
    HP_verändern(wen, schaden)

marsianischer_soldat_salvo = faehigkeit(
    "marsianischer_soldat_salvo",
    marsianischer_soldat_salvo_obj,
    "Der Soldat feuert eine starke Salve auf den Gegner.",
    3,
    0,
    "gegner"
)


def marsianischer_soldat_adrenalin_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(wer, status_effekte.schaden_plus)

marsianischer_soldat_adrenalin = faehigkeit(
    "marsianischer_soldat_adrenalin",
    marsianischer_soldat_adrenalin_obj,
    "Der Soldat erhöht seinen Angriffsschaden.",
    3,
    0,
    "selbst"
)

# ══════════════════════════════════════════════════════════════
# Stationsdrohne
# ══════════════════════════════════════════════════════════════

def stationsdrohne_reparatur_obj(wer, wen, team=None):

    heilung = 35

    charakter = charaktere.Charaktere[wen]
    charakter.hp += heilung

    if charakter.hp > charakter.max_hp:
        charakter.hp = charakter.max_hp


stationsdrohne_reparatur = faehigkeit(
    "stationsdrohne_reparatur",
    stationsdrohne_reparatur_obj,
    "Die Drohne repariert einen Verbündeten um 35-HP.",
    3,
    0,
    "verbündete"
)


def stationsdrohne_stoerung_obj(wer, wen, team=None):

    if random.random() < 0.5:
        status_effekte.status_effekte_hinzufügen(wen,status_effekte.betaeubt)

stationsdrohne_stoerung = faehigkeit(
    "stationsdrohne_stoerung",
    stationsdrohne_stoerung_obj,
    "Die Drohne versucht, das Ziel zu stören. Mit 50 % Wahrscheinlichkeit wird es betäubt.",
    3,
    0,
    "gegner"
)


# ══════════════════════════════════════════════════════════════
# Infizierter Roboter
# ══════════════════════════════════════════════════════════════

def infizierter_roboter_aeon_energie_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 1.4
    HP_verändern(wen, schaden)

    if random.random() < 0.5:
        status_effekte.status_effekte_hinzufügen(wen, status_effekte.damage_over_time_1)

infizierter_roboter_aeon_energie = faehigkeit(
    "infizierter_roboter_aeon_energie",
    infizierter_roboter_aeon_energie_obj,
    "Der Roboter setzt instabile Aeon-Energie frei. Mit 50 % Wahrscheinlichkeit erleidet das Ziel zusätzlich Schaden über Zeit.",
    3,
    0,
    "gegner"
)


def infizierter_roboter_selbstreparatur_obj(wer, wen, team=None):

    heilung = 60

    charakter = charaktere.Charaktere[wer]
    charakter.hp += heilung

    if charakter.hp > charakter.max_hp:
        charakter.hp = charakter.max_hp

infizierter_roboter_selbstreparatur = faehigkeit(
    "infizierter_roboter_selbstreparatur",
    infizierter_roboter_selbstreparatur_obj,
    "Der infizierte Roboter repariert sich selbst um 60-HP.",
    3,
    0,
    "selbst"
)


# ══════════════════════════════════════════════════════════════
# Das neue Wir
# ══════════════════════════════════════════════════════════════

def neues_wir_uebernahme_obj(wer, wen, team=None):

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.schaden_minus)

    if random.random() < 0.5:
        status_effekte.status_effekte_hinzufügen(
            wen,
            status_effekte.betaeubt
        )

neues_wir_uebernahme = faehigkeit(
    "neues_wir_uebernahme",
    neues_wir_uebernahme_obj,
    "Das neue Wir versucht, das Ziel zu kontrollieren. Der Schaden des Ziels wird verringert und mit 50 % Wahrscheinlichkeit wird es betäubt.",
    4,
    0,
    "gegner"
)


def neues_wir_anpassung_obj(wer, wen, team=None):

    if random.random() < 0.5:
        status_effekte.status_effekte_hinzufügen(wer, status_effekte.schaden_plus)
    else:
        status_effekte.status_effekte_hinzufügen(wer, status_effekte.schaden_erhalten_minus)

neues_wir_anpassung = faehigkeit(
    "neues_wir_anpassung",
    neues_wir_anpassung_obj,
    "Das neue Wir passt sich an. Mit 50 % Wahrscheinlichkeit erhöht es seinen Schaden sonnst verringert es seinen erlittenen Schaden.",
    3,
    0,
    "selbst"
)


# ══════════════════════════════════════════════════════════════
# Neues Wir – Elite
# ══════════════════════════════════════════════════════════════

def neues_wir_elite_strain_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 1.8
    HP_verändern(wen, schaden)

    if random.random() < 0.5:
        status_effekte.status_effekte_hinzufügen(wen, status_effekte.damage_over_time_1)

neues_wir_elite_strain = faehigkeit(
    "neues_wir_elite_strain",
    neues_wir_elite_strain_obj,
    "Das Elite-Exemplar setzt eine starke Energieentladung frei. Mit 50 % Wahrscheinlichkeit wird zusätzlich ein Schaden-über-Zeit-Effekt verursacht.",
    3,
    0,
    "gegner"
)


def neues_wir_elite_regeneration_obj(wer, wen, team=None):

    charakter = charaktere.Charaktere[wer]

    if charakter.hp < charakter.max_hp * 0.5:
        charakter.hp += 40

        if charakter.hp > charakter.max_hp:
            charakter.hp = charakter.max_hp
    else:
        status_effekte.status_effekte_hinzufügen(wer, status_effekte.schaden_erhalten_minus)

neues_wir_elite_regeneration = faehigkeit(
    "neues_wir_elite_regeneration",
    neues_wir_elite_regeneration_obj,
    "Das Elite-Exemplar regeneriert sich bei niedriger Gesundheit oder aktiviert andernfalls seine Verteidigung.",
    4,
    0,
    "selbst"
)


# ══════════════════════════════════════════════════════════════
# Aeon-Splitter
# ══════════════════════════════════════════════════════════════

def aeon_splitter_verfall_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 0.7
    HP_verändern(wen, schaden)

    if random.random() < 0.5:
        status_effekte.status_effekte_hinzufügen(wen, status_effekte.damage_over_time_1)

aeon_splitter_verfall = faehigkeit(
    "aeon_splitter_verfall",
    aeon_splitter_verfall_obj,
    "Der Splitter verursacht geringen Schaden und kann das Ziel mit Aeon-Energie infizieren.",
    2,
    0,
    "gegner"
)


def aeon_splitter_zerfall_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 1.5
    HP_verändern(wen, schaden)

aeon_splitter_zerfall = faehigkeit(
    "aeon_splitter_zerfall",
    aeon_splitter_zerfall_obj,
    "Der Splitter entlädt seine Energie in einem starken Angriff.",
    3,
    0,
    "gegner"
)


# ══════════════════════════════════════════════════════════════
# Aeon-Jäger
# ══════════════════════════════════════════════════════════════

def aeon_jaeger_sprung_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 1.5
    HP_verändern(wen, schaden)

    if random.random() < 0.5:
        status_effekte.status_effekte_hinzufügen(wen, status_effekte.betaeubt)

aeon_jaeger_sprung = faehigkeit(
    "aeon_jaeger_sprung",
    aeon_jaeger_sprung_obj,
    "Der Aeon-Jäger springt auf das Ziel. Mit 50 % Wahrscheinlichkeit wird es betäubt.",
    3,
    0,
    "gegner"
)


def aeon_jaeger_blutrausch_obj(wer, wen, team=None):

    charakter = charaktere.Charaktere[wer]

    HP_verändern(wer, 70)

    if charakter.hp <= charakter.max_hp * 0.5:
        status_effekte.status_effekte_hinzufügen(
            wer,
            status_effekte.schaden_plus
        )


aeon_jaeger_blutrausch = faehigkeit(
    "aeon_jaeger_blutrausch",
    aeon_jaeger_blutrausch_obj,
    "Wenn der Aeon-Jäger stark geschwächt ist, erhöht er seinen Schaden. Außerdem heilt er sich um 70-HP",
    3,
    0,
    "selbst"
)


# ══════════════════════════════════════════════════════════════
# Aeon
# ══════════════════════════════════════════════════════════════

def aeon_energiebruch_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 2
    HP_verändern(wen, schaden)

    if random.random() < 0.7:
        status_effekte.status_effekte_hinzufügen(wen, status_effekte.betaeubt)

aeon_energiebruch = faehigkeit(
    "aeon_energiebruch",
    aeon_energiebruch_obj,
    "Der Aeon setzt eine gewaltige Energiewelle frei. Mit 70 % Wahrscheinlichkeit wird das Ziel betäubt.",
    3,
    0,
    "gegner"
)


def aeon_anpassung_obj(wer, wen, team=None):

    zufall = random.random()

    if zufall < 0.5:
        status_effekte.status_effekte_hinzufügen(wer, status_effekte.schaden_erhalten_minus)
    else:
        status_effekte.status_effekte_hinzufügen(wer, status_effekte.schaden_plus)

aeon_anpassung = faehigkeit(
    "aeon_anpassung",
    aeon_anpassung_obj,
    "Der Aeon verändert sich. Er erhält entweder eine stärkere Verteidigung oder erhöhten Schaden.",
    3,
    0,
    "selbst"
)


# ══════════════════════════════════════════════════════════════
# Schattenwesen
# ══════════════════════════════════════════════════════════════

def schattenwesen_sprung_aus_der_dunkelheit_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) * 2

    HP_verändern(wen, schaden)

    if random.random() < 0.5:
        status_effekte.status_effekte_hinzufügen(
            wen,
            status_effekte.betaeubt
        )

schattenwesen_sprung_aus_der_dunkelheit = faehigkeit(
    "schattenwesen_sprung_aus_der_dunkelheit",
    schattenwesen_sprung_aus_der_dunkelheit_obj,
    "Das Schattenwesen springt aus der Dunkelheit und fügt dem Ziel massiven Schaden zu. Zu 50% Chance wird das Ziel auch betäubt.",
    4,
    1,
    "gegner"
)


def schattenwesen_schrecken_obj(wer, wen, team=None):

    schaden = entgültigen_schaden_berechnen(wer) // 2

    HP_verändern(wen, schaden)

    if random.random() < 0.4:
        status_effekte.status_effekte_hinzufügen(wen, status_effekte.schaden_minus)
        status_effekte.status_effekte_hinzufügen(wen, status_effekte.damage_over_time_1)

schattenwesen_schrecken = faehigkeit(
    "schattenwesen_schrecken",
    schattenwesen_schrecken_obj,
    "Das Schattenwesen stößt einen unheimlichen Schrei aus und fügt dem Ziel Schaden zu. Zu 40% Chance wird das Ziel verängstigt.",
    3,
    0,
    "gegner"
)


# ══════════════════════════════════════════════════════════════
# Traum Sara
# ══════════════════════════════════════════════════════════════

def traum_sara_schattenangriff_obj(wer, wen, team=None):
    schaden = entgültigen_schaden_berechnen(wer)
    HP_verändern(wen, schaden)


traum_sara_schattenangriff = faehigkeit(
    "traum_sara_schattenangriff",
    traum_sara_schattenangriff_obj,
    "Traum-Sara greift ihr Ziel mit einer dunklen, unnatürlichen Energie an.",
    0,
    0,
    "gegner"
)


def traum_sara_zerreissender_griff_obj(wer, wen, team=None):
    schaden = entgültigen_schaden_berechnen(wer) * 2
    HP_verändern(wen, schaden)


traum_sara_zerreissender_griff = faehigkeit(
    "traum_sara_zerreissender_griff",
    traum_sara_zerreissender_griff_obj,
    "Traum-Sara greift ihr Ziel mit ihren unnatürlich langen Gliedmaßen an und fügt massiven Schaden zu.",
    4,
    0,
    "gegner"
)


def traum_sara_es_beginnt_obj(wer, wen, team=None):
    schaden = entgültigen_schaden_berechnen(wer) * 3
    HP_verändern(wen, schaden)


traum_sara_es_beginnt = faehigkeit(
    "traum_sara_es_beginnt",
    traum_sara_es_beginnt_obj,
    "Traum-Sara flüstert ihrem Ziel zu: Es beginnt ...",
    5,
    1,
    "gegner"
)













# ══════════════════════════════════════════════════════════════

# NPCs

# ══════════════════════════════════════════════════════════════

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

    status_effekte.status_effekte_hinzufügen(
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
    cooler_schlag,

    #Down in Mars

    #John
    john_geziehlter_schuss,
    john_taktischer_angriff,

    #Sara
    sara_geziehlter_schuss,
    sara_ausweichen,

    #Lara
    lara_erste_hilfe,
    lara_unterstuetzung,

    #Rico
    rico_starker_schuss,
    rico_feuerstoss,

    #Chasker
    chasker_schutz,
    chasker_schwerer_angriff,

    #Gegner

    #Mars-Sicherheitsdrohne
    mars_sicherheitsdrohne_stoerimpuls,
    mars_sicherheitsdrohne_scan,

    #Mars-Wachroboter
    mars_wachroboter_stoss,
    mars_wachroboter_schild,

    #Marsianischer Wächter
    marsianischer_waechter_schild,
    marsianischer_waechter_markieren,

    # Marsianischer Soldat
    marsianischer_soldat_salvo,
    marsianischer_soldat_adrenalin,

    # Stationsdrohne
    stationsdrohne_reparatur,
    stationsdrohne_stoerung,

    # Infizierter Roboter
    infizierter_roboter_aeon_energie,
    infizierter_roboter_selbstreparatur,

    # Neues Wir
    neues_wir_uebernahme,
    neues_wir_anpassung,

    # Neues Wir Elite
    neues_wir_elite_strain,
    neues_wir_elite_regeneration,

    # Aeon-Splitter
    aeon_splitter_verfall,
    aeon_splitter_zerfall,

    # Aeon-Jäger
    aeon_jaeger_sprung,
    aeon_jaeger_blutrausch,

    # Aeon
    aeon_energiebruch,
    aeon_anpassung,

    #Schattenwesen
    schattenwesen_sprung_aus_der_dunkelheit,
    schattenwesen_schrecken,

    #Traum Sara
    traum_sara_schattenangriff,
    traum_sara_zerreissender_griff,
    traum_sara_es_beginnt
]