import os
import time

import menues
import funktions
import charaktere
import ressourcen
import confic





def charakter_bip(spieler_name):
    #---Menü---#
    charakter_bip_menue = True

    while charakter_bip_menue == True:

        os.system(confic.terminal_clear)

        wahl = funktions.menue(menues.charakter_bip_menue, spieler_name)

        if wahl == 1:
            charaktere_anzeigen()

        elif wahl == 2:
            charaktere_aufleveln()

        elif wahl == 3:
            return 1




def charaktere_anzeigen():

    os.system(confic.terminal_clear)

    charaktere_anzeigen = True

    while charaktere_anzeigen == True:

        print()
        for schlüssel, charakter in charaktere.Charaktere.items():
            print(f"----{schlüssel}----")

            print(f"Name         : {charakter.name}")
            print(f"Level        : {charakter.level}")
            print(f"Klasse       : {charakter.klasse}")
            print(f"HP           : {charakter.hp}")
            print(f"Schaden      : {charakter.schaden}")
            print(f"Speed        : {charakter.speed}")
            print(f"Faehigkeit 1 : {charakter.faehigkeit_1}")
            print(f"Faehigkeit 2 : {charakter.faehigkeit_2}")
            print(f"Faehigkeit 3 : {charakter.faehigkeit_3}")
            print()

        #---Ende---#
        ready = input("Fertig?" )
        if ready == "ja":
            charaktere_anzeigen = False
            os.system(confic.terminal_clear)
        else:
            os.system(confic.terminal_clear)
        



def level_up(wen):  
    charaktere.Charaktere[wen].level = charaktere.Charaktere[wen].level + 1
    charaktere.Charaktere[wen].hp = charaktere.Charaktere[wen].hp * 1.2
    charaktere.Charaktere[wen].schaden = charaktere.Charaktere[wen].schaden * 1.2 



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
    os.system(confic.terminal_clear)
    
    charaktere_aufleveln = True

    while charaktere_aufleveln == True:

        os.system(confic.terminal_clear)

        while True:
            wen = input("Wen möchtest du leveln? ")

            if not wen in charaktere.Charaktere:
                print()
                print("---Dieser Charakter existiert nicht!---")
                time.sleep(2)
                funktions.zeilen_loeschen(3)
            else:
                break

        #--Level des zu upgraden gewünschten charakters--#
        aktuelles_level_des_chrakters = charaktere.Charaktere[wen].level

        if aktuelles_level_des_chrakters == 13:
            print("Charakter auf maximalem Level.")
            time.sleep(2)
            os.system(confic.terminal_clear)
            break

        #--credit Kosten berechnen--#
        kosten_für_level_up = level_kosten_credits(aktuelles_level_des_chrakters)

        is_break = ressourcen.ressourcen_verändern("Credits   ", kosten_für_level_up)

        if is_break == 1:
            break

        #--Eingentliches Level_up--#
        level_up(wen)

        os.system(confic.terminal_clear)

        print(f"Gelevelt: {wen}")
        print("---Status---")

        charakter = charaktere.Charaktere[wen]

        print()
        print(f"----{wen}----")
        print(f"Name         : {charakter.name}")
        print(f"Level        : {charakter.level}")
        print(f"Klasse       : {charakter.klasse}")
        print(f"HP           : {charakter.hp}")
        print(f"Schaden      : {charakter.schaden}")
        print(f"Speed        : {charakter.speed}")
        print(f"Faehigkeit 1 : {charakter.faehigkeit_1}")
        print(f"Faehigkeit 2 : {charakter.faehigkeit_2}")
        print(f"Faehigkeit 3 : {charakter.faehigkeit_3}")

        print()

        nochmal = input("Nochmal? ")

        os.system(confic.terminal_clear)

        if nochmal == "ja":
           charaktere_aufleveln = True 

        else:
            charaktere_aufleveln = False