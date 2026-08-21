import os
import funktions
import menues
import ressourcen

def shop():

    while  True:
        os.system("cls")
        print("==================")
        print("       Shop       ")
        print("==================")
        print()
        print("=====Guthaben=====")
        ressourcen.ressourcen_anzeigen()
        print("==================")
        print()
        print("Zu Kaufen:")
        print()

        wahl = funktions.menue(menues.shop_menue)

        if wahl == 1:
            ressourcen.ressourcen_verändern("Credits   ", 1000)

        elif wahl == 2:
            ressourcen.ressourcen_verändern("Material 1", 20)

        elif wahl == 3:
            ressourcen.ressourcen_verändern("Energie   ", 20)

        else:
            return 1 