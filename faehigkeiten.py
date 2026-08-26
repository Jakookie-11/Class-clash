import charaktere

def HP_verändern(wem, wie_viel):
    charaktere.Charaktere[wem].hp = charaktere.Charaktere[wem].hp +wie_viel




def einfacher_angriff(angreifer, ziel):

    schaden =  charaktere.Charaktere[angreifer].schaden

    if charaktere.Charaktere[angreifer].seite == charaktere.Charaktere[ziel].seite:
        schaden *= 0.8

    HP_verändern(ziel, schaden)




def einfache_heilung(wer, wen):

    HP_verändern(wen, 50)