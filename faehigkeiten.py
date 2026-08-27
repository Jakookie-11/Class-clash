import charaktere
import status_effekte



def HP_verändern(wem, wie_viel):
    charaktere.Charaktere[wem].hp = charaktere.Charaktere[wem].hp +wie_viel



def effekte_berügsichtigen(wer):

    to_return = 1

    if status_effekte.status_effekt_vorhanden(wer, "schaden_plus"):
        if status_effekte.status_effekt_vorhanden(wer, "schaden_minus"):
            to_return = 1
        else:
            to_return = 1.3

    if status_effekte.status_effekt_vorhanden(wer, "schaden_minus"):
        if status_effekte.status_effekt_vorhanden(wer, "schaden_plus"):
            to_return = 1
        else:
            to_return = 0.7

    return to_return



def entgültigen_schaden_berechnen(wer):

    faktor_1 = charaktere.Charaktere[wer].schaden
    faktor_2 = effekte_berügsichtigen(wer)

    schaden = faktor_1 * faktor_2

    return schaden

#----------------------Fähigkeiten----------------------#

def einfacher_angriff(wer, wen):

    schaden =  entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.8

    HP_verändern(wen, schaden)



def blutiger_schlag(wer, wen):

    schaden =  entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.8

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.schaden_minus)

    HP_verändern(wen, schaden)


def einfache_heilung(wer, wen):

    HP_verändern(wen, 50)



def staerkende_heilung(wer, wen):

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.schaden_plus)

    HP_verändern(wen, 50)



def starker_schlag(wer, wen):

    schaden =  entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.8

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.betaeubt)

    HP_verändern(wen, schaden)



def bleibender_schlag(wer, wen):

    schaden =  entgültigen_schaden_berechnen(wer)

    if charaktere.Charaktere[wer].seite == charaktere.Charaktere[wen].seite:
        schaden *= 0.8

    status_effekte.status_effekte_hinzufügen(wen, status_effekte.damage_over_time_1)

    HP_verändern(wen, schaden)