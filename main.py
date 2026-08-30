import os
import time

import funktions
import menues
import charakter_bip
import shop
import neues_spiel
from saves import speichern
import confic

hauptmenue = True

os.system(confic.terminal_clear)

#---Vorbild---#
print("======================")
print("Willkommen bei ")
print("Class clash")
print("======================")
time.sleep(2)

#---Begrüsung_Spieler---#
os.system(confic.terminal_clear)
while True:
    spieler = input("Wie heisst du? ")
    passwort = input("Passwort? ")
    print()

    if passwort == confic.passwoerter[spieler]:
        print("Passwort korrekt")
        break
    else:
        print("Passwort falsch")
        time.sleep(2)
        os.system(confic.terminal_clear)
        funktions.zeilen_loeschen(4)

time.sleep(1)
os.system(confic.terminal_clear)
print()
print(f"Willkommen {spieler}")
time.sleep(2)

os.system(confic.terminal_clear)

speichern.spiel_laden(spieler)

#-----Hauptmenü-----#
while hauptmenue == True:
    wahl = funktions.menue(menues.hauptmenue, spieler)
    os.system(confic.terminal_clear)

    if wahl == 1:
        os.system(confic.terminal_clear)
        while True:
            is_brake_neues_spiel = neues_spiel.neues_spiel(spieler)

            if is_brake_neues_spiel == 1:
                os.system(confic.terminal_clear)
                break

    elif wahl == 2:
        os.system(confic.terminal_clear)
        while True:
            is_brake_charakter_bib = charakter_bip.charakter_bip(spieler)

            if is_brake_charakter_bib == 1:
                os.system(confic.terminal_clear)
                break
                

    elif wahl == 3:
        os.system(confic.terminal_clear)
        print("oeffne Einstellungen...")
        funktions.bestaetigung_menue("oeffne Einstellungen...")

    elif wahl == 4:
        while True:
            is_brake_shop = shop.shop(spieler)

            if is_brake_shop == 1:
                os.system(confic.terminal_clear)
                break

    elif wahl == 5:
        os.system(confic.terminal_clear)
        speichern.spiel_speichern(spieler)
        print("Spiel wird gespeichert...")
        time.sleep(1)
        os.system(confic.terminal_clear)

    else:
        os.system(confic.terminal_clear)
        speichern.spiel_speichern(spieler)
        print("Spiel wird gespeichert...")
        time.sleep(1)
        os.system(confic.terminal_clear)
        print()
        print("BYE")
        print()
        time.sleep(4)
        os.system(confic.terminal_clear)
        hauptmenue = False                  
