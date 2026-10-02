import pygame
from pathlib import Path

pygame.mixer.init()

MUSIK_ORDNER = Path(__file__).parent / "musik"


def musik_abspielen(datei):
    dateipfad = MUSIK_ORDNER / datei

    pygame.mixer.music.load(str(dateipfad))
    pygame.mixer.music.play(-1)


def musik_stoppen():
    pygame.mixer.music.stop()