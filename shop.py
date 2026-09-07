import os

import funktions
import menues
import ressourcen
import confic

def shop():

    bibliothek = menues.shop_menue

    while  True:
        os.system(confic.terminal_clear)
        print("══════════════════════════════")
        print("             Shop")
        print("══════════════════════════════")
        print()
        print("═══════════Guthaben═══════════")
        ressourcen.ressourcen_anzeigen()
        print("══════════════════════════════")
        print()
        print("Zu Kaufen:")
        print()

        for schlüssel, wert in bibliothek.items():
            print(schlüssel)

        wahl = input("Wahl? ")

        if wahl == "1":
            ressourcen.ressourcen_verändern("Credits   ", 1000)

        elif wahl == "2":
            ressourcen.ressourcen_verändern("Material 1", 20)

        elif wahl == "3":
            ressourcen.ressourcen_verändern("Energie   ", 20)

        else:
            return 1 