import os
import time

import charaktere
import menues
import faehigkeiten
import funktions


def neues_spiel():

    neues_spiel_menue = True

    while neues_spiel_menue == True:

        wahl = funktions.menue(menues.neues_spiel_menue)

        os.system("cls")

        if wahl == 1:
            kampf()

        elif wahl == 2:
            print("Kampangen in arbeit...")
            funktions.bestaetigung_menue("Kampangen in arbeit...")

        else:
            return 1




def charaktere_auswaelen():

    os.system("cls")

    print("Verfügbare Charaktere:")
    print()
    for schlüssel, wert in charaktere.Charaktere.items():
        print(schlüssel)

    print()
    print("Team 1:")
    print()

    Leader_team_1    = input("Leader: ")
    spieler_2_team_1 = input("Spieler_2: ")

    print()
    print("Team 2:")
    print()

    Leader_team_2    = input("Leader: ")
    spieler_2_team_2 = input("Spieler_2: ")

    time.sleep(1)
    os.system("cls")

    while True:

        print("-----Team_1-----")
        for schlüssel, wert in charaktere.Charaktere[Leader_team_1].items():
            print(f"{schlüssel} : {wert}")

        print()

        for schlüssel, wert in charaktere.Charaktere[spieler_2_team_1].items():
            print(f"{schlüssel} : {wert}")

        print()
        print()

        print("-----Team_2-----")
        for schlüssel, wert in charaktere.Charaktere[Leader_team_2].items():
            print(f"{schlüssel} : {wert}")

        print()

        for schlüssel, wert in charaktere.Charaktere[spieler_2_team_2].items():
            print(f"{schlüssel} : {wert}")

        time.sleep(1)

        print()
        ready = input("Fertig? ")

        if ready == "ja":
            return Leader_team_1, spieler_2_team_1, Leader_team_2, spieler_2_team_2
    
        else:
            os.system("cls")


    

def schnellster_charakter_ermitteln (ausgewählte_charaktere_list):
    reinfolge = sorted(ausgewählte_charaktere_list, key=lambda name: charaktere.Charaktere[name]["Speed     "], reverse=True)
    return reinfolge




def tote_charaktere_entvernen(ausgewaehlte_charaktere):

    neue_liste = []

    for name in ausgewaehlte_charaktere:
        if charaktere.Charaktere[name]["HP        "] >0:
            neue_liste.append(name)

    return neue_liste

    


def is_win(team):
    for name in team:
        if charaktere.Charaktere[name]["HP        "] >0:
            return False

    return True




def kampf():

    os.system("cls")

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

        os.system("cls")

        print("=========================")
        print("          Kampf          ")
        print("=========================")
        print()
        #--Teams + HP anzeigen--#
        print(f"{"Team 1:" :<30}{"Team 2:" :<30}")
        print(f"{charaktere.Charaktere[leader_1]["Name      "] :<10}{charaktere.Charaktere[leader_1]["HP        "] :<20}{charaktere.Charaktere[leader_2]["Name      "] :<10}{charaktere.Charaktere[leader_2]["HP        "]}")
        print(f"{charaktere.Charaktere[spieler_2_1]["Name      "] :<10}{charaktere.Charaktere[spieler_2_1]["HP        "] :<20}{charaktere.Charaktere[spieler_2_2]["Name      "] :<10}{charaktere.Charaktere[spieler_2_2]["HP        "]}")

        print()
        print("================================================================================")
        print()

        #--Wer ist am zug--#
        wer = reinfolge[zug]

        print(f"{wer} ist am zug!")
        print("----Status----")
        print(f"HP        : {charaktere.Charaktere[wer]["HP        "]}")
        print(f"Schaden   : {charaktere.Charaktere[wer]["Schaden   "]}")
        print()
        print(f"1) {charaktere.Charaktere[wer]["Faehigkeit 1"]}")
        print(f"2) {charaktere.Charaktere[wer]["Faehigkeit 2"]}")
        print(f"3) {charaktere.Charaktere[wer]["Faehigkeit 3"]}")

        wahl = input("wahl? ")

        if wahl == "1":
            faehigkeit = charaktere.Charaktere[wer]["Faehigkeit 1"]
        elif wahl == "2":
            faehigkeit = charaktere.Charaktere[wer]["Faehigkeit 2"]
        else:
            faehigkeit = charaktere.Charaktere[wer]["Faehigkeit 3"]


        ziel = input("Mit wem soll diese Faehigkeit interagieren? ")

        #---Eigentliche Fähigkeit---#
        faehigkeit(wer, ziel)

        #---tote charaktäre entvernen---#
        ausgewaehlte_charaktere = tote_charaktere_entvernen(ausgewaehlte_charaktere)
        reinfolge = schnellster_charakter_ermitteln(ausgewaehlte_charaktere)

        #---Sieg?---#
        is_win_team_1 = is_win(team_2)
        if is_win_team_1 == True:
            os.system("cls")
            print("Team 1 hat gewonnen!")
            time.sleep(5)
            break

        is_win_team_2 = is_win(team_1)
        if is_win_team_2 == True:
            os.system("cls")
            print()
            print("Team 2 hat gewonnen!")
            time.sleep(5)
            os.system("cls")

            break        



        zug += 1

        if zug >= len(reinfolge):
            zug = 0