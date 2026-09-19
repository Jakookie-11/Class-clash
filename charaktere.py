import faehigkeiten
import copy



class charakter:

    def __init__(
        self,
        name: str,
        klasse: str,
        hp: int,
        max_hp: int,
        max_max_hp,
        schaden: int,
        seite: str,
        speed: int,
        level: int = 1,
        faehigkeit_1=None,
        faehigkeit_2=None,
        faehigkeit_3=None        

    ):

        self.name = name
        self.klasse = klasse
        self.hp = hp
        self.max_hp = max_hp
        self.max_max_hp = max_max_hp
        self.schaden = schaden
        self.seite = seite
        self.speed = speed
        self.level = level

        self.faehigkeit_1 = copy.copy(faehigkeit_1)
        self.faehigkeit_2 = copy.copy(faehigkeit_2)
        self.faehigkeit_3 = copy.copy(faehigkeit_3)

        self.status_effekte = []
               



#---Jakob---#
Jakob = charakter(
    "Jakob",
    "Tank",
    200,
    200,
    200,
    -20,
    "light_side",
    100,
    1,
    faehigkeit_1=faehigkeiten.jakobs_basic,
    faehigkeit_2=faehigkeiten.starker_schlag,
    faehigkeit_3=faehigkeiten.bleibender_schlag
)


#---Hannah_d---#
Hannah_d = charakter(
    "Hannah_d",
    "Unterstuetzer",
    150,
    150,
    150,
    -25,
    "light_side",
    110,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.einfache_heilung,
    faehigkeit_3=faehigkeiten.staerkende_heilung
)


#---Leo---#
Leo = charakter(
    "Leo",
    "Angreifer",
    70,
    70,
    70,
    -20,
    "light_side",
    80,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.blutiger_schlag,
    faehigkeit_3=faehigkeiten.bleibender_schlag
)


#---Simon---#
Simon = charakter(
    "Simon",
    "Unterstuetzer",
    110,
    110,
    110,
    -10,
    "dark_side",
    70,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.einfache_heilung,
    faehigkeit_3=faehigkeiten.staerkende_heilung
)


#---Max---#
Max = charakter(
    "Max",
    "Tank",
    200,
    200,
    200,
    -10,
    "dark_side",
    90,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.blutiger_schlag,
    faehigkeit_3=faehigkeiten.staerkende_heilung
)


#---Lovis---#
Lovis = charakter(
    "Lovis",
    "unterstuetzer",
    100,
    100,
    100,
    -10,
    "dark_side",
    85,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.blutiger_schlag,
    faehigkeit_3=faehigkeiten.staerkende_heilung
)




#--------------------------------------------#
#--------------------npcs--------------------#
#--------------------------------------------#

fuenftklaessler = charakter(
    "fuenftklaessler", "npc", 70, 70, 70, -7, "npc", 50, 1,
    faehigkeit_1=faehigkeiten.radiergummi_wefen,
    faehigkeit_2=faehigkeiten.er_hat_nichts_gemacht,
    faehigkeit_3=faehigkeiten.hordenangriff
)


cooler_fuenftklaessler = charakter(
    "cooler_fuenftklaessler", "npc", 80, 80, 80, -8, "npc", 60, 1,
    faehigkeit_1=faehigkeiten.ey_was_guckst_du,
    faehigkeit_2=faehigkeiten.sonnenbrille_auf,
    faehigkeit_3=faehigkeiten.ranzenwurf
)


streber = charakter(
    "streber", "npc", 60, 60, 60, -6, "npc", 70, 1,
    faehigkeit_1=faehigkeiten.das_ist_falsch,
    faehigkeit_2=faehigkeiten.hausaufgaben_zeigen,
    faehigkeit_3=faehigkeiten.musterloesung
)


aufsicht = charakter(
    "aufsicht", "npc", 95, 95, 95, -9, "npc", 75, 1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.strafarbeit,
    faehigkeit_3=faehigkeiten.ordnungsruf
)

hausmeister = charakter(
    "hausmeister", "npc", 150, 150, 150, -12, "npc", 55, 1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.pausenbrot,
    faehigkeit_3=faehigkeiten.glockenschlag
)

direktor = charakter(
    "direktor", "npc", 230, 230, 230, -15, "npc", 65, 1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.autoritaet,
    faehigkeit_3=faehigkeiten.glockenschlag
)

klassenclown = charakter(
    "klassenclown", "npc", 115, 115, 115, -11, "npc", 95, 1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.streich,
    faehigkeit_3=faehigkeiten.lachanfall
)




#----Charaktere----#
Charaktere = {
    "Jakob"   : Jakob,
    "Leo"     : Leo,
    "Simon"   : Simon,
    "Max"     : Max,
    "Lovis"   : Lovis,
    "Hannah_d": Hannah_d,

    "fuenftklaessler": fuenftklaessler,
    "cooler_fuenftklaessler": cooler_fuenftklaessler,
    "streber": streber,
    "aufsicht": aufsicht,
    "hausmeister": hausmeister,
    "direktor": direktor,
    "klassenclown": klassenclown
}