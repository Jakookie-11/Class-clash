import charaktere

def HP_verändern(wem, wie_viel):
    charaktere.Charaktere[wem]["HP        "] = charaktere.Charaktere[wem]["HP        "] +wie_viel




def einfacher_angriff(angreifer, ziel):

    schaden =  charaktere.Charaktere[angreifer]["Schaden   "]

    HP_verändern(ziel, schaden)




def einfache_heilung(wer, wen):

    HP_verändern(wen, 50)