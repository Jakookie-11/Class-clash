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
        hauptmenue = True
        funktions.bestaetigung_menue("Neues Spiel startet...")

    elif wahl == 2:
        os.system("cls")
        while True:
            charakter_bip.charakter_bip()

    elif wahl == 3:
        os.system("cls")
        print("oeffne Einstellungen...")
        hauptmenue = True
        funktions.bestaetigung_menue("oeffne Einstellungen...")

    elif wahl == 4:
        os.system("cls")
        print("BYE")
        print()
        time.sleep(4)
        hauptmenue = False                  
