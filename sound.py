import pygame
from pathlib import Path
import time

pygame.mixer.init()

MUSIK_ORDNER = Path(__file__).parent / "musik"

SOUNDS = {}


def musik_abspielen(datei, lautstaerke=0.3):
    dateipfad = MUSIK_ORDNER / datei

    pygame.mixer.music.load(str(dateipfad))
    pygame.mixer.music.set_volume(lautstaerke)
    pygame.mixer.music.play(-1)


def musik_einmal_abspielen(datei, lautstaerke=0.5):
    dateipfad = MUSIK_ORDNER / datei

    pygame.mixer.music.load(str(dateipfad))
    pygame.mixer.music.set_volume(lautstaerke)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


def sound_abspielen(datei, lautstaerke=1.0):
    if datei not in SOUNDS:
        dateipfad = MUSIK_ORDNER / datei
        SOUNDS[datei] = pygame.mixer.Sound(str(dateipfad))

    sound = SOUNDS[datei]
    sound.set_volume(lautstaerke)
    sound.play()


def musik_lautstaerke(lautstaerke):
    pygame.mixer.music.set_volume(lautstaerke)


def musik_stoppen():
    pygame.mixer.music.stop()