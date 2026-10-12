import time
import os

import confic

ressourcen = {
    "Credits" : 1000,
    "M_Credits" : 1000,
    "Material 1" : 50,
    "Energie" : 100
}

def ressourcen_anzeigen():
    for schlüssel, wert in ressourcen.items():
        print(f"{schlüssel :10} : {wert}")


def ressourcen_verändern(welche_1, wie_viel_1, welche_2=None, wie_viel_2=None):
    #-Bestätigung-#
    bestaetigung = input(f"Möchtest du den Deal {wie_viel_1} {welche_1} eingehen? ")

    if bestaetigung == "ja":

        if wie_viel_1 < 0:
            if welche_2 != None and wie_viel_2 != None:
                if abs(wie_viel_1) <= ressourcen[welche_1] and abs(wie_viel_2) <= ressourcen[welche_2]:
                    ressourcen[welche_1] = ressourcen[welche_1] + wie_viel_1
                    ressourcen[welche_2] = ressourcen[welche_2] + wie_viel_2
                
                else:
                    print(f"Zu wenig {welche_1} oder {welche_2}")
                    time.sleep(2)
                    os.system(confic.terminal_clear)
                    return 1

            elif welche_2 == None and wie_viel_2 == None:
                if abs(wie_viel_1) <= ressourcen[welche_1]:
                    ressourcen[welche_1] = ressourcen[welche_1] + wie_viel_1
                
                else:
                    print(f"Zu wenig {welche_1}")
                    time.sleep(2)
                    os.system(confic.terminal_clear)
                    return 1

    else:
        print("Kauf abgebrochen.")
        time.sleep(2)
        os.system(confic.terminal_clear)
        return 1