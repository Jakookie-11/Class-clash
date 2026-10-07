import pygame
from pathlib import Path
import time

pygame.mixer.init()

MUSIK_ORDNER = Path(__file__).parent / "musik"

SOUNDS = {}

_aktuelle_musik = None
_musik_fadeout_aktiv = False


def musik_abspielen(datei, lautstaerke=1):
    global _aktuelle_musik, _musik_fadeout_aktiv

    if (
        pygame.mixer.music.get_busy()
        and _aktuelle_musik == datei
        and not _musik_fadeout_aktiv
    ):
        return

    pygame.mixer.music.stop()

    dateipfad = MUSIK_ORDNER / datei

    pygame.mixer.music.load(str(dateipfad))
    pygame.mixer.music.set_volume(lautstaerke)
    pygame.mixer.music.play(-1)
    _aktuelle_musik = datei
    _musik_fadeout_aktiv = False


def musik_einmal_abspielen(datei, lautstaerke=1):
    global _aktuelle_musik, _musik_fadeout_aktiv

    dateipfad = MUSIK_ORDNER / datei

    pygame.mixer.music.load(str(dateipfad))
    pygame.mixer.music.set_volume(lautstaerke)
    pygame.mixer.music.play()
    _aktuelle_musik = datei
    _musik_fadeout_aktiv = False


def sound_abspielen(datei, lautstaerke=1.0):
    if datei not in SOUNDS:
        dateipfad = MUSIK_ORDNER / datei
        SOUNDS[datei] = pygame.mixer.Sound(str(dateipfad))

    sound = SOUNDS[datei]
    sound.set_volume(lautstaerke)
    sound.play()


def musik_lautstaerke(lautstaerke):
    pygame.mixer.music.set_volume(lautstaerke)


def musik_stoppen(dauer=2000):
    global _musik_fadeout_aktiv

    pygame.mixer.music.fadeout(dauer)
    _musik_fadeout_aktiv = pygame.mixer.music.get_busy()