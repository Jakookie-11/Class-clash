import menues
import os
import time
import funktions
import charaktere

def charakter_bip():
    #---Menü---#
    charakter_bip_menue = True

    while charakter_bip_menue == True:

        os.system("cls")

        wahl = funktions.menue(menues.charakter_bip_menue)

        if wahl == 1:
            charaktere_anzeigen()

        elif wahl == 2:
            charaktere_aufleveln()

        elif wahl == 3:
            return 1



def charaktere_anzeigen():

    os.system("cls")

    charaktere_anzeigen = True

    while charaktere_anzeigen == True:

        print()
        for schlüssel, wert in charaktere.Charaktere.items():
            print(f"----{schlüssel}----")

            for eigenschaft, wert_der_eigenschaft in wert.items():
                print(f"{eigenschaft} : {wert_der_eigenschaft}")

            print()

        #---Ende---#
        ready = input("Fertig?" )
        if ready == "ja":
            charaktere_anzeigen = False
            os.system("cls")
        else:
            os.system("cls")
        

def level_up(wen):  
    charaktere.Charaktere[wen]["Level     "] = charaktere.Charaktere[wen]["Level     "] + 1
    charaktere.Charaktere[wen]["HP        "] = charaktere.Charaktere[wen]["HP        "] * 1.2
    charaktere.Charaktere[wen]["Schaden   "] = charaktere.Charaktere[wen]["Schaden   "] * 1.2 


def charaktere_aufleveln():
    os.system("cls")
    
    charaktere_aufleveln = True

    while charaktere_aufleveln == True:

        os.system("cls")
    
        wen = input("Wen möchtest du leveln? ")

        #--Eingentliches Level_up--#
        level_up(wen)

        os.system("cls")

        print(f"Gelevelt: {wen}")
        print("---Status---")
        for schlüssel, wert in charaktere.Charaktere[wen].items():
            print(f"{schlüssel} : {wert}")

        nochmal = input("Nochmal? ")

        os.system("cls")

        if nochmal == "ja":
           charaktere_aufleveln = True 

        else:
            charaktere_aufleveln = False