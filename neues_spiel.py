import os
import time
import re

import charaktere
import menues
import status_effekte
import funktions
import confic
import faehigkeiten
import ki
import kampange
import geheimes
import copy


GRUEN = "\033[32m"
GELB = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"


def neues_spiel(spieler_name):

    neues_spiel_menue = True

    while neues_spiel_menue == True:

        os.system(confic.terminal_clear)

        wahl = funktions.menue(menues.neues_spiel_menue, spieler_name)

        if wahl == 1:
            is_break_kampf = benutzerdefinierten_kampf_starten()

            if is_break_kampf == 1 or is_break_kampf == 2 or is_break_kampf == 3:
                continue

        elif wahl == 2:
            is_break_kampangen = kampange.kampangen(spieler_name)

            if is_break_kampangen == 1:
                continue

        else:
            return 1




def charakter_anzeigen(name):
    charakter = charaktere.Charaktere[name]

    print(f"Name    : {charakter.name}")
    print(f"Level   : {charakter.level}")
    print(f"Klasse  : {charakter.klasse}")
    print(f"HP      : {charakter.hp:.2f}")
    print(f"Schaden : {charakter.schaden}")
    print(f"Speed   : {charakter.speed}")




def verfuegbare_charaktere():
    return [
        name
        for name in charaktere.Charaktere
    ]


def ganzzahl_einlesen(prompt, minimum, maximum):
    while True:
        wahl = input(prompt).strip()

        if wahl.isdigit() and minimum <= int(wahl) <= maximum:
            return int(wahl)

        print(f"Bitte eine Zahl zwischen {minimum} und {maximum} eingeben.")


def benutzerdefinierten_kampf_starten():
    os.system(confic.terminal_clear)

    print("===== Benutzerdefinierter Kampf =====")
    print()
    print("Passe deinen Kampf an.")
    print()

    team_groesse_1 = ganzzahl_einlesen(
        "Teamgröße deines Teams (1-4): ",
        1,
        4
    )
    team_groesse_2 = ganzzahl_einlesen(
        "Teamgröße des gegnerischen Teams (1-4): ",
        1,
        4
    )

    print()
    print("[1] Gegner wird von der KI gesteuert")
    print("[2] Zweiter Spieler steuert das Gegnerteam")
    gegner_typ = ganzzahl_einlesen("Auswahl: ", 1, 2)

    ki_stufe = 1
    if gegner_typ == 1:
        print()
        print("KI-Stufen: 1 Zufällig, 2 Taktisch, 3 Stark, 4 Meister")
        ki_stufe = ganzzahl_einlesen("KI-Stufe (1-4): ", 1, 4)

    input("\nEnter zum Starten...")

    return kampf(
        team_groesse_1=team_groesse_1,
        team_groesse_2=team_groesse_2,
        Ki=ki_stufe,
        gegner_ki=gegner_typ == 1
    )


def charaktere_auswaelen(nur_eigenes_team=False, team_groesse=2):

    os.system(confic.terminal_clear)

    print("Verfügbare Charaktere:")
    print()
    if nur_eigenes_team:
        print("NPC-Charaktere sind im eigenen Team nicht erlaubt.")
    else:
        print("Jeder existierende Charakter kann ausgewählt werden.")
    print()
    for name in verfuegbare_charaktere():
        print(name)
    print()
    print(f"Wähle {team_groesse} Charakter(e) aus:")
    print()
    team = []
    for nummer in range(1, team_groesse + 1):
        while True:
            name = input(f"Charakter {nummer}: ").strip()
            ist_gueltig = name in charaktere.Charaktere
            ist_npc = (
                ist_gueltig
                and charaktere.Charaktere[name].klasse == "npc"
            )

            if ist_gueltig and not (nur_eigenes_team and ist_npc):
                team.append(name)
                break

            if not ist_gueltig:
                print("--- Dieser Charakter existiert nicht. ---")
            else:
                print("--- NPC-Charaktere sind im eigenen Team nicht erlaubt. ---")
            funktions.zeilen_loeschen(2)

    print()
    print("Team:")
    for name in team:
        print(f"- {name}")
    input("\nEnter zum Bestätigen...")
    return team


    

def schnellster_charakter_ermitteln (ausgewählte_charaktere_list):
    reinfolge = sorted(ausgewählte_charaktere_list, key=lambda name: charaktere.Charaktere[name].speed, reverse=True)
    return reinfolge


def naechsten_zug_ermitteln(
    alte_reihenfolge,
    neue_reihenfolge,
    aktueller_name,
    aktueller_index
):
    if not neue_reihenfolge:
        return 0

    if aktueller_name in neue_reihenfolge:
        return (
            neue_reihenfolge.index(aktueller_name) + 1
        ) % len(neue_reihenfolge)

    for offset in range(1, len(alte_reihenfolge) + 1):
        kandidat = alte_reihenfolge[
            (aktueller_index + offset) % len(alte_reihenfolge)
        ]

        if kandidat in neue_reihenfolge:
            return neue_reihenfolge.index(kandidat)

    return 0




def tote_charaktere_entvernen(ausgewaehlte_charaktere):

    neue_liste = []

    for name in ausgewaehlte_charaktere:
        if charaktere.Charaktere[name].hp >0:
            neue_liste.append(name)

    return neue_liste

    


def is_win(team):
    for name in team:
        if charaktere.Charaktere[name].hp >0:
            return False

    return True




def abklingzeiten_aktualisieren(von_wem):

    charakter = charaktere.Charaktere[von_wem]

    if charakter.faehigkeit_1.abklingzeit > 0:
        charakter.faehigkeit_1.abklingzeit -= 1

    if charakter.faehigkeit_2.abklingzeit > 0:
        charakter.faehigkeit_2.abklingzeit -= 1

    if charakter.faehigkeit_3.abklingzeit > 0:
        charakter.faehigkeit_3.abklingzeit -= 1




def alle_faehigkeits_abklingzeiten_resetten():

    for charakter in charaktere.Charaktere.values():

        charakter.faehigkeit_1.abklingzeit = 0
        charakter.faehigkeit_2.abklingzeit = 0
        charakter.faehigkeit_3.abklingzeit = 0




def alle_statuseffekte_resetten():
    for name in charaktere.Charaktere:
        charaktere.Charaktere[name].status_effekte = []




def HP_zuruecksetzen():
    for charakter in charaktere.Charaktere.values():
        charakter.max_hp = charakter.max_max_hp
        charakter.hp = charakter.max_hp




def text_auffuellen(text, breite):
    sichtbare_laenge = len(re.sub(r"\033\[[0-9;]*m", "", text))
    return text + " " * max(0, breite - sichtbare_laenge)




def kampf_charakter_anzeigen(name):
    charakter = charaktere.Charaktere[name]

    gefuellt = int(20 * charakter.hp / charakter.max_hp)
    leer = 20 - gefuellt
    balken = "█" * gefuellt + "░" * leer

    text = []

    text.append(f"{CYAN}{name}{RESET}")
    text.append(
        f"{GRUEN}{balken} "
        f"{charakter.hp:.2f}/{charakter.max_hp:.2f} HP{RESET}"
    )

    text.append(f"Level {charakter.level} | {charakter.klasse}")

    if charakter.status_effekte:
        text.append(f"{GELB}Effekte:{RESET}")

        for effekt in charakter.status_effekte:
            text.append(f"{GELB}{effekt.name} ({effekt.dauer}){RESET}")
    else:
        text.append("Effekte: Keine")

    return text




def kampf_team_anzeigen(team_1, team_2):
        
    TEAM_BREITE = 40

    print(f"{'TEAM 1':<{TEAM_BREITE}}{'TEAM 2':<{TEAM_BREITE}}")
    print(f"{'────────────────────':<{TEAM_BREITE}}{'────────────────────':<{TEAM_BREITE}}")

    for i in range(max(len(team_1), len(team_2))):

        if i < len(team_1):
            links = kampf_charakter_anzeigen(team_1[i])
        else:
            links = [""] * 4

        if i < len(team_2):
            rechts = kampf_charakter_anzeigen(team_2[i])
        else:
            rechts = [""] * 4

        max_zeilen = max(len(links), len(rechts))

        for j in range(max_zeilen):
            if j < len(links):
                l = links[j]
            else:
                l = ""

            if j < len(rechts):
                r = rechts[j]
            else:
                r = ""

            print(text_auffuellen(l, TEAM_BREITE) + r)

        print()




def ziel_auswaehlen(wer, team_1, team_2, zieltyp):

    if zieltyp == "gegner":
        if wer in team_1:
            moegliche_ziele = team_2
        else:
            moegliche_ziele = team_1

    elif zieltyp == "verbündete":
        if wer in team_1:
            moegliche_ziele = team_1
        else:
            moegliche_ziele = team_2

    else:
        return None

    # Tote Charaktere entfernen
    moegliche_ziele = [
        name for name in moegliche_ziele
        if charaktere.Charaktere[name].hp > 0
    ]

    print()
    print("Ziele:")
    print()

    for nummer, name in enumerate(moegliche_ziele, start=1):
        print(f"[{nummer}] {name}")

    print()

    while True:
        wahl = input("Ziel? ")

        if wahl.isdigit():
            nummer = int(wahl)

            if 1 <= nummer <= len(moegliche_ziele):
                return moegliche_ziele[nummer - 1]

        print("Ungültige Auswahl!")
        funktions.zeilen_loeschen(2)



def kampf_charaktere_kopieren(ausgewaehlte_charaktere):
    neue_charaktere = []
    vorkommen = {}

    for name in ausgewaehlte_charaktere:

        if name not in vorkommen:
            vorkommen[name] = 1
            neue_charaktere.append(name)
            continue

        vorkommen[name] += 1
        neuer_name = f"{name}_{vorkommen[name]}"

        charaktere.Charaktere[neuer_name] = copy.deepcopy(
            charaktere.Charaktere[name]
        )

        neue_charaktere.append(neuer_name)

    return neue_charaktere






































def kampf(
    team_1=None,
    team_2=None,
    team_groesse_1=2,
    team_groesse_2=2,
    Ki=1,
    gegner_ki=False
):

    os.system(confic.terminal_clear)

    zug = 0
    runde = 1

    # ══════════════════════════════════════════════════════════════
    # Teams bestimmen
    # ══════════════════════════════════════════════════════════════

    # Team 1 vom Spieler auswählen
    if team_1 is None:

        team_1 = list(
            charaktere_auswaelen(
                nur_eigenes_team=True,
                team_groesse=team_groesse_1
            )
        )

    else:
        team_1 = list(team_1)


    # Team 2 auswählen, auch wenn es von der KI gesteuert wird
    if team_2 is None:
        team_2 = list(
            charaktere_auswaelen(
                nur_eigenes_team=False,
                team_groesse=team_groesse_2
            )
        )

    else:
        team_2 = list(team_2)


    # ══════════════════════════════════════════════════════════════
    # Überprüfen, ob die Teams gültig sind
    # ══════════════════════════════════════════════════════════════

    if len(team_1) == 0 or len(team_2) == 0:
        print("Ein Team darf nicht leer sein.")
        time.sleep(2)
        return 2


    # ══════════════════════════════════════════════════════════════
    # Alle Charaktere des Kampfes
    # ══════════════════════════════════════════════════════════════

    ausgewaehlte_charaktere = team_1 + team_2


    # ══════════════════════════════════════════════════════════════
    # Doppelte Charaktere kopieren
    # ══════════════════════════════════════════════════════════════

    ausgewaehlte_charaktere = kampf_charaktere_kopieren(
        ausgewaehlte_charaktere
    )


    # Durch das Kopieren müssen die Teams wieder
    # aus der gemeinsamen Liste aufgebaut werden.

    team_1 = ausgewaehlte_charaktere[:len(team_1)]
    team_2 = ausgewaehlte_charaktere[len(team_1):]


    # ══════════════════════════════════════════════════════════════
    # Zugreihenfolge
    # ══════════════════════════════════════════════════════════════

    reinfolge = schnellster_charakter_ermitteln(
        ausgewaehlte_charaktere
    )


    # ══════════════════════════════════════════════════════════════
    # Kampf
    # ══════════════════════════════════════════════════════════════

    while True:

        os.system(confic.terminal_clear)

        print("═════════════════════════")
        print("          Kampf          ")
        print(f"         Runde {runde}")
        print("═════════════════════════")
        print()

        # Teams anzeigen
        kampf_team_anzeigen(team_1, team_2)

        print(
            "═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════"
        )
        print()


        # Falls durch einen vorherigen Zug Charaktere gestorben sind
        # und die Reihenfolge leer geworden ist
        if not reinfolge:
            return 2


        # ══════════════════════════════════════════════════════════
        # Wer ist am Zug?
        # ══════════════════════════════════════════════════════════

        if zug >= len(reinfolge):
            zug = 0

        wer = reinfolge[zug]


        # ══════════════════════════════════════════════════════════
        # Betäubt?
        # ══════════════════════════════════════════════════════════

        if status_effekte.status_effekt_vorhanden(
            wer,
            "betaeubt"
        ):

            os.system(confic.terminal_clear)

            print(f"{wer} ist betaeubt und setzt aus!")
            time.sleep(2)

            status_effekte.status_effekte_aktualisieren(wer)

        else:

            # ══════════════════════════════════════════════════════
            # Spielerzug
            # ══════════════════════════════════════════════════════

            if wer in team_1:

                while True:

                    print(f"{wer} ist am zug!")
                    print("----Status----")
                    print(
                        f"HP        : "
                        f"{charaktere.Charaktere[wer].hp:.2f}"
                    )
                    print(
                        f"Schaden   : "
                        f"{charaktere.Charaktere[wer].schaden}"
                    )
                    print()

                    print(
                        f"[1] "
                        f"{charaktere.Charaktere[wer].faehigkeit_1.name :30}"
                        f"Cooldown: "
                        f"{charaktere.Charaktere[wer].faehigkeit_1.abklingzeit}"
                    )

                    print(
                        f"[2] "
                        f"{charaktere.Charaktere[wer].faehigkeit_2.name :30}"
                        f"Cooldown: "
                        f"{charaktere.Charaktere[wer].faehigkeit_2.abklingzeit}"
                    )

                    print(
                        f"[3] "
                        f"{charaktere.Charaktere[wer].faehigkeit_3.name :30}"
                        f"Cooldown: "
                        f"{charaktere.Charaktere[wer].faehigkeit_3.abklingzeit}"
                    )

                    print()
                    print(
                        "Doppelte Zahl für die Erklärung der Fähigkeit"
                    )
                    print("Abbrechen um den kampf abzubrechen")
                    print()

                    wahl = input("wahl? ")


                    # ──────────────────────────────────────────────
                    # Kampf abbrechen
                    # ──────────────────────────────────────────────

                    if wahl.lower() == "abbrechen":

                        alle_statuseffekte_resetten()
                        alle_faehigkeits_abklingzeiten_resetten()
                        HP_zuruecksetzen()

                        return 2


                    # ──────────────────────────────────────────────
                    # Fähigkeit auswählen
                    # ──────────────────────────────────────────────

                    if wahl == "1":

                        faehigkeit = (
                            charaktere.Charaktere[wer].faehigkeit_1
                        )

                    elif wahl == "11":

                        faehigkeit = (
                            charaktere.Charaktere[wer].faehigkeit_1
                        )

                        print()
                        print(faehigkeit.erklaerung)
                        print()

                        input("Fertig? ")

                        funktions.zeilen_loeschen(17)

                        continue


                    elif wahl == "2":

                        faehigkeit = (
                            charaktere.Charaktere[wer].faehigkeit_2
                        )

                    elif wahl == "22":

                        faehigkeit = (
                            charaktere.Charaktere[wer].faehigkeit_2
                        )

                        print()
                        print(faehigkeit.erklaerung)
                        print()

                        input("Fertig? ")

                        funktions.zeilen_loeschen(17)

                        continue


                    elif wahl == "3":

                        faehigkeit = (
                            charaktere.Charaktere[wer].faehigkeit_3
                        )

                    elif wahl == "33":

                        faehigkeit = (
                            charaktere.Charaktere[wer].faehigkeit_3
                        )

                        print()
                        print(faehigkeit.erklaerung)
                        print()

                        input("Fertig? ")

                        funktions.zeilen_loeschen(17)

                        continue


                    else:

                        funktions.zeilen_loeschen(13)

                        print()
                        print("Diese Fähigkeit existiert nicht")

                        time.sleep(1)

                        funktions.zeilen_loeschen(2)

                        continue


                    # ──────────────────────────────────────────────
                    # Cooldown überprüfen
                    # ──────────────────────────────────────────────

                    if faehigkeit.abklingzeit > 0:

                        print()
                        print(
                            "Diese Fähigkeit ist noch auf Abklingzeit"
                        )

                        time.sleep(2)

                        funktions.zeilen_loeschen(15)

                        continue


                    # ──────────────────────────────────────────────
                    # Ziel auswählen
                    # ──────────────────────────────────────────────

                    ziel = ziel_auswaehlen(
                        wer,
                        team_1,
                        team_2,
                        faehigkeit.zieltyp
                    )


                    # ──────────────────────────────────────────────
                    # Fähigkeit benutzen
                    # ──────────────────────────────────────────────

                    faehigkeit.abklingzeit = (
                        faehigkeit.max_abklingzeit
                    )

                    if faehigkeit.name == "knielauf" or faehigkeit.name == "jakobs_basic":
                        faehigkeit.funktion(
                            wer,
                            ziel,
                            team_1,
                            team_2
                        )
                    else:
                        faehigkeit.funktion(
                            wer,
                            ziel,
                            team_1
                        ) 

                    geheimes.wer_hat_wieviel_schaden_genommen(
                        wer,
                        ziel,
                        team_1,
                        team_2
                    )


                    abklingzeiten_aktualisieren(wer)

                    break


            # ══════════════════════════════════════════════════════
            # KI-Zug
            # ══════════════════════════════════════════════════════

            else:
                faehigkeit, ziel = ki.ki_zug(wer, team_1, team_2, Ki)

                if faehigkeit is None or ziel is None:
                    print("Die KI konnte kein gültiges Ziel finden.")
                    time.sleep(2)

                    if is_win(team_2):
                        return 1

                    if is_win(team_1):
                        return 3

                    return 2

                faehigkeit.abklingzeit = faehigkeit.max_abklingzeit
                faehigkeit.funktion(wer, ziel, team_2)

                geheimes.wer_hat_wieviel_schaden_genommen(
                    wer,
                    ziel,
                    team_1,
                    team_2
                )


                abklingzeiten_aktualisieren(wer)


            # ══════════════════════════════════════════════════════
            # Status-Effekte aktualisieren
            # ══════════════════════════════════════════════════════

            status_effekte.status_effekte_aktualisieren(wer)


        # ══════════════════════════════════════════════════════════
        # Tote Charaktere entfernen
        # ══════════════════════════════════════════════════════════

        alte_reihenfolge = reinfolge

        ausgewaehlte_charaktere = (
            tote_charaktere_entvernen(
                ausgewaehlte_charaktere
            )
        )

        reinfolge = schnellster_charakter_ermitteln(
            ausgewaehlte_charaktere
        )


        # ══════════════════════════════════════════════════════════
        # Sieg überprüfen
        # ══════════════════════════════════════════════════════════

        if is_win(team_2):

            os.system(confic.terminal_clear)

            print("Team 1 hat gewonnen!")

            time.sleep(2)

            os.system(confic.terminal_clear)

            alle_statuseffekte_resetten()
            alle_faehigkeits_abklingzeiten_resetten()
            HP_zuruecksetzen()

            return 1


        if is_win(team_1):

            os.system(confic.terminal_clear)

            print()
            print("Team 2 hat gewonnen!")

            time.sleep(2)

            os.system(confic.terminal_clear)

            alle_statuseffekte_resetten()
            alle_faehigkeits_abklingzeiten_resetten()
            HP_zuruecksetzen()

            return 3


        # ══════════════════════════════════════════════════════════
        # Nächster Zug
        # ══════════════════════════════════════════════════════════

        zug = naechsten_zug_ermitteln(
            alte_reihenfolge,
            reinfolge,
            wer,
            zug
        )

        if alte_reihenfolge and wer == alte_reihenfolge[-1]:
            runde += 1