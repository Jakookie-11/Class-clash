import os
import time

import funktions
import menues
import charakter_bip
import shop
import neues_spiel
from saves import speichern

hauptmenue = True

os.system("cls")

#---Vorbild---#
print("======================")
print("Willkommen bei ")
print("Class clash")
print("======================")
time.sleep(2)

#---Begrüsung_Spieler---#
os.system("cls")
spieler = input("Wie heisst du? ")
time.sleep(1)
os.system("cls")
print()
print(f"Willkommen {spieler}")
time.sleep(2)

os.system("cls")

speichern.spiel_laden(spieler)

#-----Hauptmenü-----#
while hauptmenue == True:
    wahl = funktions.menue(menues.hauptmenue)
    os.system("cls")

    if wahl == 1:
        os.system("cls")
        while True:
            is_brake_neues_spiel = neues_spiel.neues_spiel()

            if is_brake_neues_spiel == 1:
                os.system("cls")
                break

    elif wahl == 2:
        os.system("cls")
        while True:
            is_brake_charakter_bib = charakter_bip.charakter_bip()

            if is_brake_charakter_bib == 1:
                os.system("cls")
                break
                

    elif wahl == 3:
        os.system("cls")
        print("oeffne Einstellungen...")
        funktions.bestaetigung_menue("oeffne Einstellungen...")

    elif wahl == 4:
        while True:
            is_brake_shop = shop.shop()

            if is_brake_shop == 1:
                os.system("cls")
                break

    elif wahl == 5:
        os.system("cls")
        speichern.spiel_speichern(spieler)
        print("Spiel wird gespeichert...")
        time.sleep(1)
        os.system("cls")

    else:
        os.system("cls")
        print()
        print("BYE")
        print()
        time.sleep(4)
        os.system("cls")
        hauptmenue = False                  
