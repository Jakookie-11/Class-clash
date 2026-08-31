import os
import time

import charaktere
import menues
import status_effekte
import funktions
import confic
import faehigkeiten


def neues_spiel(spieler_name):

    neues_spiel_menue = True

    while neues_spiel_menue == True:

        wahl = funktions.menue(menues.neues_spiel_menue, spieler_name)

        os.system(confic.terminal_clear)

        if wahl == 1:
            kampf()

        elif wahl == 2:
            print("Kampangen in arbeit...")
            funktions.bestaetigung_menue("Kampangen in arbeit...")

        else:
            return 1




def charakter_anzeigen(name):
    charakter = charaktere.Charaktere[name]

    print(f"Name    : {charakter.name}")
    print(f"Level   : {charakter.level}")
    print(f"Klasse  : {charakter.klasse}")
    print(f"HP      : {charakter.hp}")
    print(f"Schaden : {charakter.schaden}")
    print(f"Seite   : {charakter.seite}")
    print(f"Speed   : {charakter.speed}")




def charaktere_auswaelen():

    os.system(confic.terminal_clear)

    print("Verfügbare Charaktere:")
    print()
    for schlüssel, wert in charaktere.Charaktere.items():
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

    time.sleep(1)
    os.system(confic.terminal_clear)

    while True:

        print("-----Team_1-----")

        charakter_anzeigen(Leader_team_1)

        print()

        charakter_anzeigen(spieler_2_team_1)

        print()
        print()

        print("-----Team_2-----")

        charakter_anzeigen(Leader_team_2)

        print()

        charakter_anzeigen(spieler_2_team_2)

        print()

        ready = input("Fertig? ")

        if ready == "ja":
            return Leader_team_1, spieler_2_team_1, Leader_team_2, spieler_2_team_2

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




def kampf():

    os.system(confic.terminal_clear)

    zug = 0

    #---Charaktere bekommen---#
    leader_1, spieler_2_1, leader_2, spieler_2_2 = charaktere_auswaelen()

    #---Charaktere als list speichern---#
    ausgewaehlte_charaktere = [
        leader_1,
        spieler_2_1,
        leader_2,
        spieler_2_2
    ]

    #---Teams---#
    team_1 = [
        leader_1,
        spieler_2_1
    ]

    team_2 = [
        leader_2,
        spieler_2_2
    ]


    #---reinfolge ermitteln---#
    reinfolge = schnellster_charakter_ermitteln(ausgewaehlte_charaktere)

    while True:

        os.system(confic.terminal_clear)

        print("=========================")
        print("          Kampf          ")
        print("=========================")
        print()
        #--Teams + HP anzeigen--#
        print("----Team 1----")
        print(f"{leader_1:<10} {charaktere.Charaktere[leader_1].hp:<10} HP   {status_effekte.status_effekte_anzeigen(leader_1)}")
        print(f"{spieler_2_1:<10} {charaktere.Charaktere[spieler_2_1].hp:<10} HP   {status_effekte.status_effekte_anzeigen(spieler_2_1)}")
        print()
        print()
        print("----Team 2----")
        print(f"{leader_2:<10} {charaktere.Charaktere[leader_2].hp:<10} HP   {status_effekte.status_effekte_anzeigen(leader_2)}")
        print(f"{spieler_2_2:<10} {charaktere.Charaktere[spieler_2_2].hp:<10} HP   {status_effekte.status_effekte_anzeigen(spieler_2_2)}")
        print()
        print("================================================================================")
        print()

        #--Wer ist am zug--#
        wer = reinfolge[zug]

        #--Betäubt?--#
        if status_effekte.status_effekt_vorhanden(wer, "betaeubt") == True:

            os.system(confic.terminal_clear)
            print(f"{wer} ist betaeubt und setzt aus!")
            time.sleep(2)
            status_effekte.status_effekte_aktualisieren(wer)

            zug += 1
            
            if zug >= len(reinfolge):
                zug = 0

        else:
            while True:       
                print(f"{wer} ist am zug!")
                print("----Status----")
                print(f"HP        : {charaktere.Charaktere[wer].hp}")
                print(f"Schaden   : {charaktere.Charaktere[wer].schaden}")
                print()
                print(f"1) {charaktere.Charaktere[wer].faehigkeit_1.__name__.replace('_', ' ').title()}")
                print(f"2) {charaktere.Charaktere[wer].faehigkeit_2.__name__.replace('_', ' ').title()}")
                print(f"3) {charaktere.Charaktere[wer].faehigkeit_3.__name__.replace('_', ' ').title()}")
                print()
                print("Doppelte Zahl für die Erklärung der Fähigkeit")
                print()

                wahl = input("wahl? ")

                if wahl == "1":
                    faehigkeit = charaktere.Charaktere[wer].faehigkeit_1
                    break

                elif wahl == "11":
                    print()
                    eval("faehigkeiten." + charaktere.Charaktere[wer].faehigkeit_1.__name__ + "_erklaerung()")
                    print()
                    fertig = input("Fertig? ")
                    if fertig == "ja":
                        funktions.zeilen_loeschen(16)

                elif wahl == "2":
                    faehigkeit = charaktere.Charaktere[wer].faehigkeit_2
                    break

                elif wahl == "22":
                    print()
                    eval("faehigkeiten." + charaktere.Charaktere[wer].faehigkeit_2.__name__ + "_erklaerung()")
                    print()
                    fertig = input("Fertig? ")
                    if fertig == "ja":
                        funktions.zeilen_loeschen(16)

                elif wahl == "3":
                    faehigkeit = charaktere.Charaktere[wer].faehigkeit_3
                    break

                elif wahl == "33":
                    print()
                    eval("faehigkeiten." + charaktere.Charaktere[wer].faehigkeit_3.__name__ + "_erklaerung()")
                    print()
                    fertig = input("Fertig? ")
                    if fertig == "ja":
                        funktions.zeilen_loeschen(16)

                else:
                    funktions.zeilen_loeschen(9)
                    print()
                    print("Diese Fähigkeit existiert nicht")
                    time.sleep(1)
                    funktions.zeilen_loeschen(2)


            ziel = input("Mit wem soll diese Faehigkeit interagieren? ")
            #---Eigentliche Fähigkeit---#
            faehigkeit(wer, ziel)

            #---Effekte aktuallisieren---#
            status_effekte.status_effekte_aktualisieren(wer)

            #---tote charaktäre entvernen---#
            ausgewaehlte_charaktere = tote_charaktere_entvernen(ausgewaehlte_charaktere)
            reinfolge = schnellster_charakter_ermitteln(ausgewaehlte_charaktere)

            #---Sieg?---#
            is_win_team_1 = is_win(team_2)
            if is_win_team_1 == True:
                os.system(confic.terminal_clear)
                print("Team 1 hat gewonnen!")
                time.sleep(5)
                os.system(confic.terminal_clear)

                #---Status Effekte zurücksetzen---#
                for name in charaktere.Charaktere:
                    charaktere.Charaktere[name].status_effekte = []

                break

            is_win_team_2 = is_win(team_1)
            if is_win_team_2 == True:
                os.system(confic.terminal_clear)
                print()
                print("Team 2 hat gewonnen!")
                time.sleep(5)
                os.system(confic.terminal_clear)

                #---Status Effekte zurücksetzen---#
                for name in charaktere.Charaktere:
                    charaktere.Charaktere[name].status_effekte = []
                    
                break        



            zug += 1

            if zug >= len(reinfolge):
                zug = 0