#----------Tests----------#

import json
import confic

datei = f"saves/confic_setup.json"
datei = open(datei, "w")

daten = {
    "starter_menue"  : confic.first_start_configurator,
    "terminal_clear" : confic.terminal_clear
}

json.dump(daten, datei)
datei.close()