import charaktere
import status_effekte

def HP_verändern(wem, wie_viel):
    charaktere.Charaktere[wem].hp = charaktere.Charaktere[wem].hp +wie_viel




def einfacher_angriff(wer, ziel):

    schaden =  charaktere.Charaktere[wer].schaden

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[ziel].seite:
        schaden *= 0.8

    HP_verändern(ziel, schaden)




def einfache_heilung(wer, wen):

    HP_verändern(wen, 50)




def starker_schlag(wer, ziel):

    schaden =  charaktere.Charaktere[wer].schaden

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[ziel].seite:
        schaden *= 0.8

    status_effekte.status_effekte_hinzufügen(ziel, status_effekte.betaeubt)

    HP_verändern(ziel, schaden)