import os

import speichern
import menues
import ressourcen
import confic

def shop(spieler_name):

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

        for schlüssel, wert in menues.shop_menue.items():
            print(schlüssel)

        wahl = input("Wahl? ")

        if wahl == "1":
            ressourcen.ressourcen_verändern("Credits", 1000)

        elif wahl == "2":
            ressourcen.ressourcen_verändern("Material 1", 20)

        elif wahl == "3":
            ressourcen.ressourcen_verändern("Energie", 20)

        else:
            speichern.spiel_speichern(spieler_name)
            return 1 