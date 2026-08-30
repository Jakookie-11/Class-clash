import os
import time
import copy

import charaktere
import faehigkeiten




class StatusEffekt:

    def __init__(
        self,
        name: str,
        dauer: int,
        wert: float
    ):
        
        self.name = name
        self.dauer = dauer
        self.wert = wert



#----Buffs----#
betaeubt = StatusEffekt("betaeubt", 1, 0)
schaden_plus = StatusEffekt("schaden_plus", 2, 1.3)
schaden_minus = StatusEffekt("schaden_minus", 2, 0.7)
damage_over_time_1 = StatusEffekt("damage_over_time_1", 2, -10 )
healing_over_time_1 = StatusEffekt("healing_over_time_1", 2, 10 )



def status_effekte_ausgeben(von_wem):
    effekte = charaktere.Charaktere[von_wem].status_effekte
    return effekte


def status_effekte_hinzufügen(wem, was):
    if was not in charaktere.Charaktere[wem].status_effekte:
        charaktere.Charaktere[wem].status_effekte.append(copy.copy(was))


def status_effekt_vorhanden(bei_wem, name):

    for effekt in charaktere.Charaktere[bei_wem].status_effekte:

        if effekt.name == name:
            return True

    return False

def status_effekte_aktualisieren(wer):

    charakter = charaktere.Charaktere[wer]

    for effekt in charakter.status_effekte:

        #---Über Zeit Effekte---#
        if effekt.name == "damage_over_time_1":
           faehigkeiten.HP_verändern(charakter.name, effekt.wert)

        if effekt.name == "healing_over_time_1":
           faehigkeiten.HP_verändern(charakter.name, effekt.wert) 

        effekt.dauer -= 1

    charakter.status_effekte = [
        effekt for effekt in charakter.status_effekte
        if effekt.dauer > 0
    ]



def status_effekte_anzeigen(wem):

    ausgabe = ""

    for effekt in charaktere.Charaktere[wem].status_effekte:
        ausgabe += f"[{effekt.name} {effekt.dauer}] "

    return ausgabe