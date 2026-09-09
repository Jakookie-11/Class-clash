import os
import time
import confic
import sys

import funktions
import menues
import charakter_bip
import shop
import neues_spiel
import speichern
import begin
import einstellungen
import subprocess




spieler = begin.begin()

if spieler == "break":

    subprocess.run([sys.executable, "updater.py"])
    print("update wird durchgefuert...")
    time.sleep(2)
    os.system(confic.terminal_clear)
    os.execv(sys.executable, [sys.executable, "main.py"])

    spieler = begin.begin()

#-----Hauptmenü-----#

hauptmenue = True

while hauptmenue == True:
    wahl = funktions.menue(menues.hauptmenue, spieler)
    os.system(confic.terminal_clear)

    if wahl == 1:
        while True:    
            is_brake_neues_spiel = neues_spiel.neues_spiel(spieler)

            if is_brake_neues_spiel == 1:
                os.system(confic.terminal_clear)
                break

    elif wahl == 2:
        while True:
            is_brake_charakter_bib = charakter_bip.charakter_bip(spieler)

            if is_brake_charakter_bib == 1:
                os.system(confic.terminal_clear)
                break
                

    elif wahl == 3:
        while True:
            is_brake_einstellungen = einstellungen.einstellungen(spieler)

            if is_brake_einstellungen == 1:
                os.system(confic.terminal_clear)
                break

    elif wahl == 4:
        while True:
            is_brake_shop = shop.shop()

            if is_brake_shop == 1:
                os.system(confic.terminal_clear)
                break

    else:
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
