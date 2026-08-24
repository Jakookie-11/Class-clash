import time
import os

ressourcen = {
    "Credits   " : 1000,
    "Material 1" : 50,
    "Energie   " : 100
}

def ressourcen_anzeigen():
    for schlüssel, wert in ressourcen.items():
        print(f"{schlüssel} : {wert}")


def ressourcen_verändern(welche, wie_viel):
    #-Bestätigung-#
    bestaetigung = input(f"Möchtest du den Deal {wie_viel} {welche} eingehen? ")

    if bestaetigung == "ja":

        if wie_viel < 0:
            if abs(wie_viel) <= ressourcen[welche]:
                ressourcen[welche] = ressourcen[welche] + wie_viel
            else:
                print(f"Zu wenig {welche}")
                time.sleep(2)
                os.system("cls")
                return 1

        elif wie_viel > 0:
            ressourcen[welche] = ressourcen[welche] + wie_viel

    else:
        return 1