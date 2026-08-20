import os
import time
import funktions
import menues
import charakter_bip

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


#-----Hauptmenü-----#
while hauptmenue == True:
    wahl = funktions.menue(menues.hauptmenue)
    os.system("cls")

    if wahl == 1:
        os.system("cls")
        print("Neues Spiel startet...")
        funktions.bestaetigung_menue("Neues Spiel startet...")

    elif wahl == 2:
        os.system("cls")
        while True:
            is_brake_charakter_bib = charakter_bip.charakter_bip()

            if is_brake_charakter_bib == 1:
                break

    elif wahl == 3:
        os.system("cls")
        print("oeffne Einstellungen...")
        funktions.bestaetigung_menue("oeffne Einstellungen...")

    elif wahl == 4:
        os.system("cls")
        print()
        print("BYE")
        print()
        time.sleep(4)
        hauptmenue = False                  
