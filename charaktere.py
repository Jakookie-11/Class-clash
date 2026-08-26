import faehigkeiten



class charakter:

    def __init__(
        self,
        name: str,
        klasse: str,
        hp: int,
        schaden: int,
        speed: int,
        level: int = 1,
        faehigkeit_1=None,
        faehigkeit_2=None,
        faehigkeit_3=None        

    ):

        self.name = name
        self.klasse = klasse
        self.hp = hp
        self.schaden = schaden
        self.speed = speed
        self.level = level

        self.faehigkeit_1 = faehigkeit_1
        self.faehigkeit_2 = faehigkeit_2
        self.faehigkeit_3 = faehigkeit_3        



#---Jakob---#
Jakob = charakter(
    "Jakob",
    "Tank",
    200,
    -100,
    100,
    faehigkeit_1=faehigkeiten.einfacher_angriff
)


#---Leo---#
Leo = charakter(
    "Leo",
    "Angreifer",
    70,
    -20,
    80,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
)


#---Simon---#
Simon = charakter(
    "Simon",
    "Unterstuetzer",
    100,
    -10,
    70,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.einfache_heilung
)


#---Max---#
Max = charakter(
    "Max",
    "Tank",
    200,
    -10,
    90,
    faehigkeit_1=faehigkeiten.einfacher_angriff
)


#----Charaktere----#
Charaktere = {
    "Jakob" : Jakob,
    "Leo"   : Leo,
    "Simon" : Simon,
    "Max"   : Max
}