import pygame
from pathlib import Path
import confic

pygame.mixer.init()

MUSIK_ORDNER = Path(__file__).parent / "musik"

SOUNDS = {}

_aktuelle_musik = None
_musik_fadeout_aktiv = False

# ══════════════════════════════════════════════════════════════
# Musik Class
# ══════════════════════════════════════════════════════════════
class musik:

    def __init__(
        self,
        titel = str,
        art = str,
        mp3 = str,
        balancing : int | float = 1
    ):
       self.titel = titel
       self.art = art
       self.mp3 = mp3
       self.balancing = balancing

# ══════════════════════════════════════════════════════════════
# Musik
# ══════════════════════════════════════════════════════════════
Hugs_and_Kisses = musik(
    "Hugs and Kisses",
    "musik",
    "Hugs and Kisses.mp3",
    2
)
Imaginary_Friend = musik(
    "Imaginary Friend",
    "musik",
    "Imaginary Friend.mp3",
    2.25
)
home = musik(
    "home",
    "musik",
    "home.mp3",
    2
)
test = musik(
    "test",
    "musik",
    "test.mp3",
    1.5
)
# ══════════════════════════════════════════════════════════════
# Soundeffekte
# ══════════════════════════════════════════════════════════════
acces_denied = musik(
    "acces denied",
    "soundeffekt",
    "acces denied.mp3",
    2.5
)
click = musik(
    "click",
    "soundeffekt",
    "click.mp3",
    3.5
)
good_morning = musik(
    "good morning",
    "soundeffekt",
    "good morning.mp3",
    2
)
shutdown = musik(
    "shutdown",
    "soundeffekt",
    "shutdown.mp3"
)
emergency_alarm = musik(
    "emergency alarm",
    "soundeffekt",
    "emergency alarm.mp3"
)
army_rank_up = musik(
    "army rank up",
    "soundeffekt",
    "army rank up.mp3",
    1.5
)
invalid_login_or_password = musik(
    "invalid-login-or-password",
    "soundeffekt",
    "invalid-login-or-password.mp3",
    2
)
# ══════════════════════════════════════════════════════════════
# jede Musik
# ══════════════════════════════════════════════════════════════
jede_musik = {
  # Musik
    Hugs_and_Kisses.titel           : Hugs_and_Kisses,
    Imaginary_Friend.titel          : Imaginary_Friend,
    home.titel                      : home,
    test.titel                      : test,

  # Soundeffekte
    acces_denied.titel              : acces_denied,
    click.titel                     : click,
    good_morning.titel              : good_morning,
    shutdown.titel                  : shutdown,
    emergency_alarm.titel           : emergency_alarm,
    army_rank_up.titel              : army_rank_up,
    invalid_login_or_password.titel : invalid_login_or_password,
}


# ══════════════════════════════════════════════════════════════
# Funktionen
# ══════════════════════════════════════════════════════════════

def musik_abspielen(titel):

    if confic.ton:

        obj = jede_musik[titel]

        if obj.titel == confic.Haupt_musik and confic.main_musik == False:
            return

        lautstaerke = obj.balancing * confic.lautstaerke

        global _aktuelle_musik, _musik_fadeout_aktiv

        if (
            pygame.mixer.music.get_busy()
            and _aktuelle_musik == obj.mp3
            and not _musik_fadeout_aktiv
        ):
            return

        pygame.mixer.music.stop()

        dateipfad = MUSIK_ORDNER / obj.mp3

        pygame.mixer.music.load(str(dateipfad))
        pygame.mixer.music.set_volume(lautstaerke)
        pygame.mixer.music.play(-1)
        _aktuelle_musik = obj.mp3
        _musik_fadeout_aktiv = False


def musik_einmal_abspielen(titel):

    if confic.ton:

        obj = jede_musik[titel]

        if obj.titel == confic.Haupt_musik and confic.main_musik == False:
            return

        lautstaerke = obj.balancing * confic.lautstaerke

        global _aktuelle_musik, _musik_fadeout_aktiv

        dateipfad = MUSIK_ORDNER / obj.mp3

        pygame.mixer.music.load(str(dateipfad))
        pygame.mixer.music.set_volume(lautstaerke)
        pygame.mixer.music.play()
        _aktuelle_musik = obj.mp3
        _musik_fadeout_aktiv = False


def sound_abspielen(titel):

    if confic.ton:

        obj = jede_musik[titel]

        lautstaerke = obj.balancing * confic.lautstaerke

        if obj.mp3 not in SOUNDS:
            dateipfad = MUSIK_ORDNER / obj.mp3
            SOUNDS[obj.mp3] = pygame.mixer.Sound(str(dateipfad))

        sound = SOUNDS[obj.mp3]
        sound.set_volume(lautstaerke)
        sound.play()


def musik_stoppen(dauer=2000):
    global _musik_fadeout_aktiv

    pygame.mixer.music.fadeout(dauer)
    _musik_fadeout_aktiv = pygame.mixer.music.get_busy()