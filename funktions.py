import os
import time

import confic
from saves import speichern

def menue(bibliothek, spieler_name=None, clear_terminal=True):

    while True:

        if clear_terminal == True:
            os.system(confic.terminal_clear)

        #---printen der Wahlen---#
        for schlüssel, wert in bibliothek.items():
            print(schlüssel)

        #---Wahl---#
        auswahl = input("Wahl? ")

        if auswahl == "1":
            return(1)
        elif auswahl == "2":
            return (2)
        elif auswahl == "3":
            return(3)
        elif auswahl == "4":
            return(4)
        elif auswahl == "4":
            return(4)
        elif auswahl == "5":
            return(5)
        elif auswahl == "6":
            return(6)
        elif auswahl == "7":
            return(7)
        elif auswahl == "8":
            return(8)
        else:
            continue




def bestaetigung_menue(wofür):

    brake = False
    ready = input("Fertig?")

    while brake == False:

        if ready == "ja":
            brake = True
            os.system(confic.terminal_clear)

        else:
            os.system(confic.terminal_clear)
            if isinstance(wofür, str):
                print(wofür)

                ready = input("Fertig?")

            elif isinstance(wofür, dict):
                for schlüssel, wert in wofür.items():
                    print(schlüssel)

                ready = input("Fertig? ")



def zeilen_loeschen(anzahl):
    for _ in range(anzahl):
        print("\033[1A\033[2K", end="")
