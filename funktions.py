import os
import time


def menue(bibliothek):


    while True:

        os.system("cls")

        #---printen der Wahlen---#
        for schlüssel, wert in bibliothek.items():
            print(schlüssel)

        time.sleep(1)

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
            print("Error 1")
            time.sleep(600)


def bestaetigung_menue(wofür):

    brake = False
    ready = input("Fertig?")

    while brake == False:

        if ready == "ja":
            brake = True

        else:
            os.system("cls")
            if isinstance(wofür, str):
                print(wofür)

                ready = input("Fertig?")

            elif isinstance(wofür, dict):
                for schlüssel, wert in wofür.items():
                    print(schlüssel)

                ready = input("Fertig? ")
