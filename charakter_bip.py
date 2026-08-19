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
            os.system("cls")
            print("Leveln in Arbeit...")
            funktions.bestaetigung_menue("Leveln in Arbeit...")

        elif wahl == 3:
            return 1



def charaktere_anzeigen():

    os.system("cls")

    for schlüssel, wert in charaktere.Jakob.items():
        print(schlüssel)

    print()

    for schlüssel, wert in charaktere.Leo.items():
        print(schlüssel)

    funktions.bestaetigung_menue(charaktere.Jakob)