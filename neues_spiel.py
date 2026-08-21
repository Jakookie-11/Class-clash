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
    



def kampf():

    os.system("cls")

    zug = 0

    #---Charaktere bekommen---#
    leader_1, spieler_2_1, leader_2, spieler_2_2 = charaktere_auswaelen()

    #---Charaktere als list speichern---#
    ausgewählte_charaktere = [
        leader_1,
        spieler_2_1,
        leader_2,
        spieler_2_2
    ]

    #---reinfolge ermitteln---#
    reinfolge = schnellster_charakter_ermitteln(ausgewählte_charaktere)

    while True:
        print("=========================")
        print("          Kampf          ")
        print("=========================")
        print()
        #--Teams + HP anzeigen--#
        print(f"{"Team 1:" :<20}{"Team 2:" :<20}")
        print(f"{charaktere.Charaktere[leader_1]["Name      "] :<10}{charaktere.Charaktere[leader_1]["HP        "] :<20}{charaktere.Charaktere[leader_2]["Name      "] :<10}{charaktere.Charaktere[leader_2]["HP        "]}")
        print(f"{charaktere.Charaktere[spieler_2_1]["Name      "] :<10}{charaktere.Charaktere[spieler_2_1]["HP        "] :<20}{charaktere.Charaktere[spieler_2_2]["Name      "] :<10}{charaktere.Charaktere[spieler_2_2]["HP        "]}")
        
        print("================================================================================")
        print()
        #--Wer ist am zug--#
        wer = reinfolge[zug]

        print(f"{wer} ist am zug!")
        print("----Stats----")
        print(f"HP        : {charaktere.Charaktere[wer]["HP        "]}")
        print(f"Schaden   : {charaktere.Charaktere[wer]["Schaden   "]}")









        zug += 1

        if zug >= len(reinfolge):
            zug = 0


    
