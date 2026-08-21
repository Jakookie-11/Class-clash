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
            print()

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

    Leader_team_2    = input("Leader:")
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


    




    

    



def benutzer_definierter_kampf():
    print()