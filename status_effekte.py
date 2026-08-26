import os
import time
import charaktere




class StatusEffekt:

    def __init__(
        self,
        name: str,
        dauer: int
    ):
        
        self.name = name
        self.dauer = dauer



betaeubt = StatusEffekt("betaeubt", 1)



def status_effekte_ausgeben(von_wem):
    effekte = charaktere.Charaktere[von_wem].status_effekte
    return effekte


def status_effekte_hinzufügen(wem, was):
    if was not in charaktere.Charaktere[wem].status_effekte:
        charaktere.Charaktere[wem].status_effekte.append(was)


def status_effekt_vorhanden(bei_wem, name):

    for effekt in charaktere.Charaktere[bei_wem].status_effekte:

        if effekt.name == name:
            return True

    return False

def status_effekte_aktualisieren(wer):

    charakter = charaktere.Charaktere[wer]

    for effekt in charakter.status_effekte:
        effekt.dauer -= 1

    charakter.status_effekte = [
        effekt for effekt in charakter.status_effekte
        if effekt.dauer > 0
    ]