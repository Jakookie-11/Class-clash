import menues
import os
import time
import funktions

def charakter_bip():
    #---Menü---#

    charakter_bip_menue = True

    while charakter_bip_menue == True:

        os.system("cls")

        wahl = funktions.menue(menues.charakter_bip_menue)

        if wahl == 1:
            os.system("cls")
            print("Anzeige in Arbeit...")
            funktions.bestaetigung_menue("Anzeige in Arbeit...")

        elif wahl == 2:
            os.system("cls")
            print("Leveln in Arbeit...")
            funktions.bestaetigung_menue("Leveln in Arbeit...")

        elif wahl == 3:
            return 1