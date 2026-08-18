import os
import time
import funktions
import menues

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
        print("Spiel wird gestartet...")
        hauptmenue = True
        funktions.bestaetigung_menue("Spiel wird gestartet...")

    elif wahl == 2:
        os.system("cls")
        print("oeffne Bibliothek...")
        hauptmenue = True
        funktions.bestaetigung_menue("oeffne Bibliothek...")

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
