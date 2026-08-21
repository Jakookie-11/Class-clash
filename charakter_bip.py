import os
import time

import menues
import funktions
import charaktere
import ressourcen




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



def level_kosten_credits(wievieltes_update):

    if   wievieltes_update == 1:
        return -100
    elif wievieltes_update == 2:
        return -300
    elif wievieltes_update == 3:
        return -500
    elif wievieltes_update == 4:
        return -1000
    elif wievieltes_update == 5:
        return -1500
    elif wievieltes_update == 6:
        return -2000
    elif wievieltes_update == 7:
        return -2500
    elif wievieltes_update == 8:
        return -3000
    elif wievieltes_update == 9:
        return -4000
    elif wievieltes_update == 10:
        return -5000
    elif wievieltes_update == 11:
        return -6500
    elif wievieltes_update == 12:
        return -8000



def charaktere_aufleveln():
    os.system("cls")
    
    charaktere_aufleveln = True

    while charaktere_aufleveln == True:

        os.system("cls")
    
        wen = input("Wen möchtest du leveln? ")

        #--Level des zu upgraden gewünschten charakters--#
        aktuelles_level_des_chrakters = charaktere.Charaktere[wen]["Level     "]

        if aktuelles_level_des_chrakters == 13:
            print("Charakter auf maximalem Level.")
            time.sleep(2)
            os.system("cls")
            break

        #--credit Kosten berechnen--#
        kosten_für_level_up = level_kosten_credits(aktuelles_level_des_chrakters)

        is_break = ressourcen.ressourcen_verändern("Credits   ", kosten_für_level_up)

        if is_break == 1:
            break

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