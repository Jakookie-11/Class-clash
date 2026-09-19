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
            is_break_kampf = kampf()

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
    print(f"Seite   : {charakter.seite}")
    print(f"Speed   : {charakter.speed}")




def charaktere_auswaelen(nur_eigenes_team=False,team_groesse=2):

    os.system(confic.terminal_clear)

    print("Verfügbare Charaktere:")
    print()
    for schlüssel, charakter in charaktere.Charaktere.items():
        if charakter.klasse != "npc":
            if charakter.name != "Hannah_d":
                print(schlüssel)
    print()
    print("Team 1:")
    print()

    Leader_team_1    = input("Leader: ")

    if not Leader_team_1 in charaktere.Charaktere:
        print("---Dieser Charakter existiert nicht!---")
        time.sleep(2)
        funktions.zeilen_loeschen(2)
        Leader_team_1    = input("Leader: ")

    spieler_2_team_1 = input("Spieler_2: ")

    if not spieler_2_team_1 in charaktere.Charaktere:
        print("---Dieser Charakter existiert nicht!---")
        time.sleep(2)
        funktions.zeilen_loeschen(2)
        spieler_2_team_1 = input("Spieler_2: ")

    if team_groesse >= 3:
        spieler_3_team_1 = input("Spieler_3: ")

        if not spieler_3_team_1 in charaktere.Charaktere:
            print("---Dieser Charakter existiert nicht!---")
            time.sleep(2)
            funktions.zeilen_loeschen(2)
            spieler_3_team_1 = input("Spieler_3: ")

    if team_groesse >= 4:
        spieler_4_team_1 = input("Spieler_4: ")

        if not spieler_4_team_1 in charaktere.Charaktere:
            print("---Dieser Charakter existiert nicht!---")
            time.sleep(2)
            funktions.zeilen_loeschen(2)
            spieler_4_team_1 = input("Spieler_4: ")

    #---falls auch gegner---#

    if nur_eigenes_team == False:

        print()
        print("Team 2:")
        print()

        Leader_team_2    = input("Leader: ")

        if not Leader_team_2 in charaktere.Charaktere:
            print("---Dieser Charakter existiert nicht!---")
            time.sleep(2)
            funktions.zeilen_loeschen(2)
            Leader_team_2    = input("Leader: ")

        spieler_2_team_2 = input("Spieler_2: ")

        if not spieler_2_team_2 in charaktere.Charaktere:
            print("---Dieser Charakter existiert nicht!---")
            time.sleep(2)
            funktions.zeilen_loeschen(2)
            spieler_2_team_2 = input("Spieler_2: ")


        if team_groesse >= 3:
            spieler_3_team_2 = input("Spieler_3: ")

            if not spieler_3_team_2 in charaktere.Charaktere:
                print("---Dieser Charakter existiert nicht!---")
                time.sleep(2)
                funktions.zeilen_loeschen(2)
                spieler_3_team_1 = input("Spieler_3: ")

        if team_groesse >= 4:
            spieler_4_team_2 = input("Spieler_4: ")

            if not spieler_4_team_2 in charaktere.Charaktere:
                print("---Dieser Charakter existiert nicht!---")
                time.sleep(2)
                funktions.zeilen_loeschen(2)
                spieler_4_team_1 = input("Spieler_4: ")

    time.sleep(1)
    os.system(confic.terminal_clear)

    while True:

        print("-----Team_1-----")
        charakter_anzeigen(Leader_team_1)
        print()
        charakter_anzeigen(spieler_2_team_1)
        print()
        if team_groesse >= 3:
            charakter_anzeigen(spieler_3_team_1)
            print()
        if team_groesse >= 4:
            charakter_anzeigen(spieler_4_team_1)
            print()

        #---falls auch gegner---#
        if nur_eigenes_team == False:
            print()
            print("-----Team_2-----")
            charakter_anzeigen(Leader_team_2)
            print()
            charakter_anzeigen(spieler_2_team_2)
            print()
            if team_groesse >= 3:
                charakter_anzeigen(spieler_3_team_2)
                print()
            if team_groesse >= 4:
                charakter_anzeigen(spieler_4_team_2)
                print()

        ready = input("Fertig? ")

        if ready == "ja" or ready == "":

            if nur_eigenes_team == False:

                if team_groesse == 2:
                    return (
                        Leader_team_1,
                        spieler_2_team_1,
                        Leader_team_2,
                        spieler_2_team_2
                    )

                elif team_groesse == 3:
                    return (
                        Leader_team_1,
                        spieler_2_team_1,
                        spieler_3_team_1,
                        Leader_team_2,
                        spieler_2_team_2,
                        spieler_3_team_2
                    )

                elif team_groesse == 4:
                    return (
                        Leader_team_1,
                        spieler_2_team_1,
                        spieler_3_team_1,
                        spieler_4_team_1,
                        Leader_team_2,
                        spieler_2_team_2,
                        spieler_3_team_2,
                        spieler_4_team_2
                    )


            elif nur_eigenes_team == True:

                if team_groesse == 2:
                    return (
                        Leader_team_1,
                        spieler_2_team_1
                    )

                elif team_groesse == 3:
                    return (
                        Leader_team_1,
                        spieler_2_team_1,
                        spieler_3_team_1
                    )

                elif team_groesse == 4:
                    return (
                        Leader_team_1,
                        spieler_2_team_1,
                        spieler_3_team_1,
                        spieler_4_team_1
                    )

        else:
            os.system(confic.terminal_clear)


    

def schnellster_charakter_ermitteln (ausgewählte_charaktere_list):
    reinfolge = sorted(ausgewählte_charaktere_list, key=lambda name: charaktere.Charaktere[name].speed, reverse=True)
    return reinfolge




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

    for faehigkeit in faehigkeiten.alle_fähigkeiten:
        faehigkeit.abklingzeit = 0




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




def kampf(
    leader_1=None,
    spieler_2_1=None,
    spieler_3_1=None,
    spieler_4_1=None,
    leader_2=None,
    spieler_2_2=None,
    spieler_3_2=None,
    spieler_4_2=None,
    Ki=1,
    team_groesse=2
):

    os.system(confic.terminal_clear)

    zug = 0

    #---Charaktere bekommen---#

    if leader_1 == None and spieler_2_1 == None and leader_2 != None:

        if team_groesse == 2:
            leader_1, spieler_2_1 = charaktere_auswaelen(
                nur_eigenes_team=True,
                team_groesse=2
            )

        elif team_groesse == 3:
            leader_1, spieler_2_1, spieler_3_1 = charaktere_auswaelen(
                nur_eigenes_team=True,
                team_groesse=3
            )

        elif team_groesse == 4:
            leader_1, spieler_2_1, spieler_3_1, spieler_4_1 = charaktere_auswaelen(
                nur_eigenes_team=True,
                team_groesse=4
            )

    else:

        if team_groesse == 2:

            leader_1, spieler_2_1, leader_2, spieler_2_2 = charaktere_auswaelen(
                team_groesse=2
            )

        elif team_groesse == 3:

            leader_1, spieler_2_1, spieler_3_1, leader_2, spieler_2_2, spieler_3_2 = charaktere_auswaelen(
                team_groesse=3
            )

        elif team_groesse == 4:

            leader_1, spieler_2_1, spieler_3_1, spieler_4_1, leader_2, spieler_2_2, spieler_3_2, spieler_4_2 = charaktere_auswaelen(
                team_groesse=4
            )


    #---Charaktere als list speichern---#

    ausgewaehlte_charaktere = [
        leader_1,
        spieler_2_1
    ]

    if team_groesse > 2:
        ausgewaehlte_charaktere.append(spieler_3_1)

    if team_groesse > 3:
        ausgewaehlte_charaktere.append(spieler_4_1)


    if leader_2 != None:
        ausgewaehlte_charaktere.append(leader_2)
        ausgewaehlte_charaktere.append(spieler_2_2)

        if team_groesse > 2:
            ausgewaehlte_charaktere.append(spieler_3_2)

        if team_groesse > 3:
            ausgewaehlte_charaktere.append(spieler_4_2)


    #---Teams---#

    team_1 = [
        leader_1,
        spieler_2_1
    ]

    if team_groesse > 2:
        team_1.append(spieler_3_1)

    if team_groesse > 3:
        team_1.append(spieler_4_1)


    team_2 = []

    if leader_2 != None:
        team_2 = [
            leader_2,
            spieler_2_2
        ]

        if team_groesse > 2:
            team_2.append(spieler_3_2)

        if team_groesse > 3:
            team_2.append(spieler_4_2)
    #---reinfolge ermitteln---#
    reinfolge = schnellster_charakter_ermitteln(ausgewaehlte_charaktere)

    while True:

        os.system(confic.terminal_clear)

        print("═════════════════════════")
        print("          Kampf          ")
        print("═════════════════════════")
        print()
        #--Teams + HP anzeigen--#
        kampf_team_anzeigen(team_1, team_2)
        print("═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
        print()

        #--Wer ist am zug--#
        wer = reinfolge[zug]

        #--Betäubt?--#
        if status_effekte.status_effekt_vorhanden(wer, "betaeubt") == True:

            os.system(confic.terminal_clear)
            print(f"{wer} ist betaeubt und setzt aus!")
            time.sleep(2)

            status_effekte.status_effekte_aktualisieren(wer)

            ausgewaehlte_charaktere = tote_charaktere_entvernen(ausgewaehlte_charaktere)
            reinfolge = schnellster_charakter_ermitteln(ausgewaehlte_charaktere)

            if wer not in reinfolge:
                zug -= 1

            zug += 1

            if zug >= len(reinfolge):
                zug = 0

        else:

            if wer in team_1:

                #--Zugriff auf Fähigkeiten--#

                while True:       
                    print(f"{wer} ist am zug!")
                    print("----Status----")
                    print(f"HP        : {charaktere.Charaktere[wer].hp:.2f}")
                    print(f"Schaden   : {charaktere.Charaktere[wer].schaden}")
                    print()
                    print(f"[1] {charaktere.Charaktere[wer].faehigkeit_1.name :20}Cooldown: {charaktere.Charaktere[wer].faehigkeit_1.abklingzeit}")
                    print(f"[2] {charaktere.Charaktere[wer].faehigkeit_2.name :20}Cooldown: {charaktere.Charaktere[wer].faehigkeit_2.abklingzeit}")
                    print(f"[3] {charaktere.Charaktere[wer].faehigkeit_3.name :20}Cooldown: {charaktere.Charaktere[wer].faehigkeit_3.abklingzeit}")
                    print()
                    print("Doppelte Zahl für die Erklärung der Fähigkeit")
                    print("Abbrechen um den kampf abzubrechen")
                    print()

                    wahl = input("wahl? ")

                    #--Prüfen ob abbrechen--#
                    if wahl == "Abbrechen" or wahl == "abbrechen":
                        return 2

                    if wahl == "1":
                        faehigkeit = charaktere.Charaktere[wer].faehigkeit_1

                    elif wahl == "11":
                        faehigkeit = charaktere.Charaktere[wer].faehigkeit_1
                        print()
                        print(faehigkeit.erklaerung)
                        print()
                        input("Fertig? ")
                        funktions.zeilen_loeschen(17)
                        continue

                    elif wahl == "2":
                        faehigkeit = charaktere.Charaktere[wer].faehigkeit_2

                    elif wahl == "22":
                        faehigkeit = charaktere.Charaktere[wer].faehigkeit_2
                        print()
                        print(faehigkeit.erklaerung)
                        print()
                        input("Fertig? ")
                        funktions.zeilen_loeschen(17)
                        continue

                    elif wahl == "3":
                        faehigkeit = charaktere.Charaktere[wer].faehigkeit_3

                    elif wahl == "33":
                        faehigkeit = charaktere.Charaktere[wer].faehigkeit_3
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


                    if faehigkeit.abklingzeit > 0:
                        print()
                        print("Diese Fähigkeit ist noch auf Abklingzeit")
                        time.sleep(2)
                        funktions.zeilen_loeschen(15)
                        continue
                    else:

                        ziel = input("Mit wem soll diese Faehigkeit interagieren? ")

                        #---Ziel existiert?---#
                        if not ziel in ausgewaehlte_charaktere:
                            funktions.zeilen_loeschen(14)
                            print()
                            print("Dieser Charakter existiert nicht")
                            time.sleep(2)
                            funktions.zeilen_loeschen(2)
                            continue


                        #---Zieltyp überprüfen---#
                        if faehigkeit.zieltyp == "gegner":
                            if wer in team_1 and ziel in team_1 or wer in team_2 and ziel in team_2:
                                funktions.zeilen_loeschen(14)
                                print()
                                print("Diese Fähigkeit kann nur auf Gegner angewendet werden")
                                time.sleep(2)
                                funktions.zeilen_loeschen(2)
                                continue

                        if faehigkeit.zieltyp == "verbündete":
                            if wer in team_1 and ziel in team_2 or wer in team_2 and ziel in team_1:
                                funktions.zeilen_loeschen(14)
                                print()
                                print("Diese Fähigkeit kann nur auf Verbündete angewendet werden")
                                time.sleep(2)
                                funktions.zeilen_loeschen(2)
                                continue


                        #---Abklingzeit auf max setzen---#
                        faehigkeit.abklingzeit = faehigkeit.max_abklingzeit

                        #---Eigentliche Fähigkeit---#
                        faehigkeit.funktion(wer, ziel, team_1)

                        geheimes.wer_hat_wieviel_schaden_genommen(ziel, team_1, team_2)

                        abklingzeiten_aktualisieren(wer)
                        break

            else:
                faehigkeit, ziel = ki.ki_zug(wer, team_1, team_2, Ki)
                faehigkeit.abklingzeit = faehigkeit.max_abklingzeit
                faehigkeit.funktion(wer, ziel, team_2)

                geheimes.wer_hat_wieviel_schaden_genommen(ziel, team_1, team_2)

                abklingzeiten_aktualisieren(wer)



            #---Effekte aktuallisieren---#
            status_effekte.status_effekte_aktualisieren(wer)

            #---tote charaktäre entvernen---#

            ausgewaehlte_charaktere = tote_charaktere_entvernen(ausgewaehlte_charaktere)
            reinfolge = schnellster_charakter_ermitteln(ausgewaehlte_charaktere)

            if wer not in reinfolge:
                zug -= 1

            #---Sieg?---#
            is_win_team_1 = is_win(team_2)
            if is_win_team_1 == True:
                os.system(confic.terminal_clear)
                print("Team 1 hat gewonnen!")
                time.sleep(2)
                os.system(confic.terminal_clear)

                #---Status Effekte / HP / Abklingzeiten zurücksetzen---#
                alle_statuseffekte_resetten()
                alle_faehigkeits_abklingzeiten_resetten()
                HP_zuruecksetzen()

                return 1

            is_win_team_2 = is_win(team_1)
            if is_win_team_2 == True:
                os.system(confic.terminal_clear)
                print()
                print("Team 2 hat gewonnen!")
                time.sleep(2)
                os.system(confic.terminal_clear)

                #---Status Effekte / HP / Abklingzeiten zurücksetzen---#
                alle_statuseffekte_resetten()
                alle_faehigkeits_abklingzeiten_resetten()
                HP_zuruecksetzen()
                    
                return 3       



            zug += 1

            if zug >= len(reinfolge):
                zug = 0