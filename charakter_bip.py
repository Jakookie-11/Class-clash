import menues
import os
import time
import funktions

def charakter_bip():
    #---Menü---#
    for schlüssel, wert in menues.charakter_bip_menue.items():
        print(schlüssel)

    wahl = input("Wahl? ")

    funktions.menue(menues.charakter_bip_menue)    