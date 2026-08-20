import os
import funktions
import menues
import ressourcen

def shop():

    while  True:
        os.system("cls")
        print()
        ressourcen.ressourcen_anzeigen()
        print()

        wahl = funktions.menue(menues.shop)

        if wahl == 1:
            ressourcen.ressourcen_verändern("Credits   ", 1000)

        elif wahl == 2:
            ressourcen.ressourcen_verändern("Material 1", 20)

        elif wahl == 3:
            ressourcen.ressourcen_verändern("Energie   ", 20)

        else:
            return 1 