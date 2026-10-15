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

#generell
betaeubt = StatusEffekt("betaeubt", 1, 0)
schaden_plus = StatusEffekt("schaden_plus", 2, 1.3)
schaden_minus = StatusEffekt("schaden_minus", 2, 0.7)
schaden_erhalten_minus = StatusEffekt("schaden_erhalten_minus", 5, 0.7)

damage_over_time_1 = StatusEffekt("damage_over_time_1", 2, -20)
healing_over_time_1 = StatusEffekt("healing_over_time_1", 2, 20)

#allgemein
beeindruckt = StatusEffekt("beeindruckt", 3, 1.2)
verunsichert = StatusEffekt("verunsichert", 2, 0.75)
unverwundbar = StatusEffekt("unverwundbar", 2, 1)
blossgestellt = StatusEffekt("blossgestellt", 2, 0.6)
wir_sind_ein_team = StatusEffekt("wir_sind_ein_team", 4, 1.2)
perfekte_vorlage = StatusEffekt("perfekte_vorlage", 1, 2)

#spezial
die_Roehre = StatusEffekt("die_Roehre", 99, 1)
belehrt_ueber_die_geschichte = StatusEffekt("belehrt_ueber_die_geschichte", 10, 1)
belehrt_ueber_die_geschichte_k = StatusEffekt("belehrt_ueber_die_geschichte_k", 3, 1)
von_Hannah_d_unterstuetzt = StatusEffekt("von_Hannah_d_unterstuetzt", 99, 1)



def status_effekte_ausgeben(von_wem):
    effekte = _charakter_abrufen(von_wem).status_effekte
    return effekte


def _charakter_schluessel_abrufen(wem):
    if isinstance(wem, str):
        return wem

    for name, charakter in charaktere.Charaktere.items():
        if charakter is wem:
            return name

    raise ValueError("Der Charakter ist nicht in charaktere.Charaktere registriert.")


def _charakter_abrufen(wem):
    return charaktere.Charaktere[_charakter_schluessel_abrufen(wem)]


def status_effekte_hinzufügen(wem, was):

    charakter = _charakter_abrufen(wem)
    effekte = charakter.status_effekte

    if isinstance(was, str):
        for effekt in globals().values():
            if isinstance(effekt, StatusEffekt) and effekt.name == was:
                was = effekt
                break
        else:
            return

    if not hasattr(was, "name"):
        return

    for i, effekt in enumerate(effekte):
        if effekt.name == was.name:
            effekt.dauer += was.dauer
            return

    effekte.append(copy.copy(was))


def status_effekt_vorhanden(bei_wem, name):

    for effekt in _charakter_abrufen(bei_wem).status_effekte:

        if effekt.name == name:
            return True

    return False

def status_effekte_aktualisieren(wer):

    charakter_schluessel = _charakter_schluessel_abrufen(wer)
    charakter = charaktere.Charaktere[charakter_schluessel]

    for effekt in charakter.status_effekte:

        #---Über Zeit Effekte---#
        if effekt.name == "damage_over_time_1":
           faehigkeiten.HP_verändern(charakter_schluessel, effekt.wert)

        if effekt.name == "healing_over_time_1":
           faehigkeiten.HP_verändern(charakter_schluessel, effekt.wert) 

        effekt.dauer -= 1

    charakter.status_effekte = [
        effekt for effekt in charakter.status_effekte
        if effekt.dauer > 0
    ]



def status_effekte_anzeigen(wem):

    ausgabe = ""

    for effekt in _charakter_abrufen(wem).status_effekte:
        ausgabe += f"[{effekt.name} {effekt.dauer}] "

    return ausgabe