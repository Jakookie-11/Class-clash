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
        max_schaden: None,
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
        self.max_schaden = max_schaden
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














# ============================================================
# Down in Mars – Storycharaktere
# ============================================================

John = charakter(
    "John",
    "down_in_mars",
    180,
    180,
    180,
    -18,
    -18,
    "down_in_mars",
    70,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.john_geziehlter_schuss,
    faehigkeit_3=faehigkeiten.john_taktischer_angriff
)


Sara = charakter(
    "Sara",
    "down_in_mars",
    150,
    150,
    150,
    -15,
    -15,
    "down_in_mars",
    90,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.sara_geziehlter_schuss,
    faehigkeit_3=faehigkeiten.sara_ausweichen
)


Lara = charakter(
    "Lara",
    "down_in_mars",
    140,
    140,
    140,
    -12,
    -12,
    "down_in_mars",
    65,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.lara_erste_hilfe,
    faehigkeit_3=faehigkeiten.lara_unterstuetzung
)


Rico = charakter(
    "Rico",
    "down_in_mars",
    160,
    160,
    160,
    -22,
    -22,
    "down_in_mars",
    60,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.rico_starker_schuss,
    faehigkeit_3=faehigkeiten.rico_feuerstoss
)


Chasker = charakter(
    "Chasker",
    "down_in_mars",
    240,
    240,
    240,
    -16,
    -16,
    "down_in_mars",
    40,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.chasker_schutz,
    faehigkeit_3=faehigkeiten.chasker_schwerer_angriff
)


# ══════════════════════════════════════════════════════════════
# Down in Mars – Gegner
# ══════════════════════════════════════════════════════════════


mars_sicherheitsdrohne = charakter(
    "mars_sicherheitsdrohne",
    "down_in_mars_gegener",
    60,
    60,
    60,
    -7,
    -7,
    "down_in_mars_gegener",
    80,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.mars_sicherheitsdrohne_stoerimpuls,
    faehigkeit_3=faehigkeiten.mars_sicherheitsdrohne_scan
)


mars_wachroboter = charakter(
    "mars_wachroboter",
    "down_in_mars_gegener",
    100,
    100,
    100,
    -10,
    -10,
    "down_in_mars_gegener",
    55,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.mars_wachroboter_stoss,
    faehigkeit_3=faehigkeiten.mars_wachroboter_schild
)


marsianischer_waechter = charakter(
    "marsianischer_waechter",
    "down_in_mars_gegener",
    130,
    130,
    130,
    -9,
    -9,
    "down_in_mars_gegener",
    45,
    1,
    faehigkeit_1= faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.marsianischer_waechter_schild,
    faehigkeit_3=faehigkeiten.marsianischer_waechter_markieren
)


marsianischer_soldat = charakter(
    "marsianischer_soldat",
    "down_in_mars_gegener",
    95,
    95,
    95,
    -13,
    -13,
    "down_in_mars_gegener",
    70,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.marsianischer_soldat_salvo,
    faehigkeit_3=faehigkeiten.marsianischer_soldat_adrenalin
)


stationsdrohne = charakter(
    "stationsdrohne",
    "down_in_mars_gegener",
    75,
    75,
    75,
    -8,
    -8,
    "down_in_mars_gegener",
    85,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.stationsdrohne_reparatur,
    faehigkeit_3=faehigkeiten.stationsdrohne_stoerung
)


infizierter_roboter = charakter(
    "infizierter_roboter",
    "down_in_mars_gegener",
    115,
    115,
    115,
    -11,
    -11,
    "down_in_mars_gegener",
    50,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.infizierter_roboter_aeon_energie,
    faehigkeit_3=faehigkeiten.infizierter_roboter_selbstreparatur
)


neues_wir = charakter(
    "neues_wir",
    "down_in_mars_gegener",
    125,
    125,
    125,
    -12,
    -12,
    "down_in_mars_gegener",
    65,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.neues_wir_uebernahme,
    faehigkeit_3=faehigkeiten.neues_wir_anpassung
)


neues_wir_elite = charakter(
    "neues_wir_elite",
    "down_in_mars_gegener",
    180,
    180,
    180,
    -15,
    -15,
    "down_in_mars_gegener",
    75,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.neues_wir_elite_strain,
    faehigkeit_3=faehigkeiten.neues_wir_elite_regeneration
)


aeon_splitter = charakter(
    "aeon_splitter",
    "down_in_mars_gegener",
    55,
    55,
    55,
    -8,
    -8,
    "down_in_mars_gegener",
    95,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.aeon_splitter_verfall,
    faehigkeit_3=faehigkeiten.aeon_splitter_zerfall
)


aeon_jaeger = charakter(
    "aeon_jaeger",
    "down_in_mars_gegener",
    110,
    110,
    110,
    -14,
    -14,
    "down_in_mars_gegener",
    105,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.aeon_jaeger_sprung,
    faehigkeit_3=faehigkeiten.aeon_jaeger_blutrausch
)


aeon = charakter(
    "aeon",
    "down_in_mars_gegener",
    300,
    300,
    300,
    -18,
    -18,
    "down_in_mars_gegener",
    60,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.aeon_energiebruch,
    faehigkeit_3=faehigkeiten.aeon_anpassung
)


schattenwesen = charakter(
    "Schattenwesen",
    "down_in_mars_gegener",
    350,
    350,
    350,
    -40,
    -40,
    "down_in_mars_gegener",
    95,
    1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.schattenwesen_sprung_aus_der_dunkelheit,
    faehigkeit_3=faehigkeiten.schattenwesen_schrecken
)


traum_sara = charakter(
    "Traum-Sara",
    "down_in_mars_gegener",
    220,
    220,
    220,
    -18,
    -18,
    "down_in_mars_gegener",
    100,
    1,
    faehigkeit_1=faehigkeiten.traum_sara_schattenangriff,
    faehigkeit_2=faehigkeiten.traum_sara_zerreissender_griff,
    faehigkeit_3=faehigkeiten.traum_sara_es_beginnt
)

















#--------------------------------------------#
#--------------------npcs--------------------#
#--------------------------------------------#

fuenftklaessler = charakter(
    "fuenftklaessler", "npc", 70, 70, 70, -7, -7, "npc", 50, 1,
    faehigkeit_1=faehigkeiten.radiergummi_wefen,
    faehigkeit_2=faehigkeiten.er_hat_nichts_gemacht,
    faehigkeit_3=faehigkeiten.hordenangriff
)


cooler_fuenftklaessler = charakter(
    "cooler_fuenftklaessler", "npc", 80, 80, 80, -8, -8, "npc", 60, 1,
    faehigkeit_1=faehigkeiten.ey_was_guckst_du,
    faehigkeit_2=faehigkeiten.sonnenbrille_auf,
    faehigkeit_3=faehigkeiten.ranzenwurf
)


streber = charakter(
    "streber", "npc", 60, 60, 60, -6, -6, "npc", 70, 1,
    faehigkeit_1=faehigkeiten.das_ist_falsch,
    faehigkeit_2=faehigkeiten.hausaufgaben_zeigen,
    faehigkeit_3=faehigkeiten.musterloesung
)


aufsicht = charakter(
    "aufsicht", "npc", 95, 95, 95, -9, -9, "npc", 75, 1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.strafarbeit,
    faehigkeit_3=faehigkeiten.ordnungsruf
)

hausmeister = charakter(
    "hausmeister", "npc", 150, 150, 150, -12, -12, "npc", 55, 1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.pausenbrot,
    faehigkeit_3=faehigkeiten.glockenschlag
)

direktor = charakter(
    "direktor", "npc", 230, 230, 230, -15, -15, "npc", 65, 1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.autoritaet,
    faehigkeit_3=faehigkeiten.glockenschlag
)

klassenclown = charakter(
    "klassenclown", "npc", 115, 115, 115, -11, -11, "npc", 95, 1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.streich,
    faehigkeit_3=faehigkeiten.lachanfall
)

normaler_6_klaessler = charakter(
    "normaler_6_klaessler", "npc", 80, 80, 80, -8, -8, "npc", 45, 1,
    faehigkeit_1=faehigkeiten.einfacher_angriff,
    faehigkeit_2=faehigkeiten.schubser,
    faehigkeit_3=faehigkeiten.rennen_gehen
)

aggressiver_6_klaessler = charakter(
    "aggressiver_6_klaessler", "npc", 65, 65, 65, -12, -12, "npc", 50, 1,
    faehigkeit_1=faehigkeiten.wütender_schlag,
    faehigkeit_2=faehigkeiten.voll_drauf,
    faehigkeit_3=faehigkeiten.noch_wuetender
)

starker_6_klaessler = charakter(
    "starker_6_klaessler", "npc", 120, 120, 120, -6, -6, "npc", 30, 1,
    faehigkeit_1=faehigkeiten.schlag,
    faehigkeit_2=faehigkeiten.festhalten,
    faehigkeit_3=faehigkeiten.nicht_weggehen
)

schlauer_6_klaessler = charakter(
    "schlauer_6_klaessler", "npc", 70, 70, 70, -5, -5, "npc", 40, 1,
    faehigkeit_1=faehigkeiten.klugscheissen,
    faehigkeit_2=faehigkeiten.hausaufgaben_helfen,
    faehigkeit_3=faehigkeiten.ich_hab_einen_plan
)

nerviger_6_klaessler = charakter(
    "nerviger_6_klaessler", "npc", 75, 75, 75, -7, -7, "npc", 55, 1,
    faehigkeit_1=faehigkeiten.nerven,
    faehigkeit_2=faehigkeiten.ablenken,
    faehigkeit_3=faehigkeiten.hoer_auf
)

cooler_6_klaessler = charakter(
    "cooler_6_klaessler", "npc", 90, 90, 90, -9, -9, "npc", 60, 1,
    faehigkeit_1=faehigkeiten.cooler_schlag,
    faehigkeit_2=faehigkeiten.sonnenbrille_auf,
    faehigkeit_3=faehigkeiten.ranzenwurf
)




#----Charaktere----#
Charaktere = {
    "Jakob"   : Jakob,
    "Leo"     : Leo,
    "Simon"   : Simon,
    "Max"     : Max,
    "Lovis"   : Lovis,
    "Hannah_d": Hannah_d,

    "John": John,
    "Sara": Sara,
    "Lara": Lara,
    "Rico": Rico,
    "Chasker": Chasker,

    "mars_sicherheitsdrohne": mars_sicherheitsdrohne,
    "mars_wachroboter": mars_wachroboter,
    "marsianischer_waechter": marsianischer_waechter,
    "marsianischer_soldat": marsianischer_soldat,
    "stationsdrohne": stationsdrohne,
    "infizierter_roboter": infizierter_roboter,
    "neues_wir": neues_wir,
    "neues_wir_elite": neues_wir_elite,
    "aeon_splitter": aeon_splitter,
    "aeon_jaeger": aeon_jaeger,
    "aeon": aeon,
    "schattenwesen": schattenwesen,

    "fuenftklaessler": fuenftklaessler,
    "cooler_fuenftklaessler": cooler_fuenftklaessler,
    "streber": streber,
    "aufsicht": aufsicht,
    "hausmeister": hausmeister,
    "direktor": direktor,
    "klassenclown": klassenclown,

    "normaler_6_klaessler" : normaler_6_klaessler,
    "aggressiver_6_klaessler" : aggressiver_6_klaessler,
    "starker_6_klaessler" : starker_6_klaessler,
    "schlauer_6_klaessler" : schlauer_6_klaessler,
    "nerviger_6_klaessler" : nerviger_6_klaessler,
    "cooler_6_klaessler" : cooler_6_klaessler

}