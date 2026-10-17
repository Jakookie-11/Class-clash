GRUEN  = "\033[32m"
GELB   = "\033[33m"
CYAN   = "\033[36m"
ROT    = "\033[31m"
ORANGE = "\033[38;5;208m"
MAGENTA  = "\033[35m"

RESET  = "\033[0m"


anmelden_menue = [
    "[1] Anmelden",
    "[2] Registrieren",
    "[3] Admin",
]

hauptmenue = [
    "[1] Spiel Starten",
    "[2] Charaktere",
    "[3] Einstellungen",
    "[4] Shop         ",
    "[5] Herausforderungen",
    f"{ROT}[0] Beenden{RESET}" 
]

spiel_starten_menue = [
    "[1] Benutzerdefinierter Kampf",
    "[2] Kampange(n)",
    "[3] Herausforderungskaempfe",
    "[4] Endlos",
    "[0] Zurueck"
]

charakter_bip_menue = [
    "[1] Anzeigen",
    "[2] Leveln",
    "[0] Zurueck"
]

einstellungen_menue = [
    "[1] Profil",
    "[2] Audio",
    f"{MAGENTA}[3] Credits{RESET}",
    "[4] Wichtige Links",
    "[5] Hilfe & Fehlerbehebung",
    "[6] Leaderboard-Daten als CSV exportieren",
    "[0] Zurueck"
]
#->Y
profil_menue = [
    "[1] Passwort aendern",
    "[2] Profil Daten zeigen",
    f"{ORANGE}[3] Profil Zuruecksetzen{RESET}",
    f"{ROT}[4] Profil Loeschen{RESET}",
    "[5] Passwort-sichtbarkeit aendern",
    "[0] Zurueck"
]
#->Y
audio_menue = [
    "[1] Ton        (an/aus) schalten",
    "[2] Main Musik (an/aus) schalten",
    "[3] Generelle Lautstaerke aendern",
    "[0] Zurueck"
]

hilfe_menue = [
    "[1] Python 3.15 installieren / pruefen",
    "[2] Falsche Python-Version beheben",
    "[3] PDF-Hilfen oeffnen",
    "[4] Crash-Logs anzeigen",
    "[5] GitHub Issue melden",
    "[0] Zurueck"
]

shop_menue = [
    "[1] 1000 Credits   ",
    "[2] 1000 M_Credits",
    "[3] 20   Material 1",
    "[4] 20   Energie   ",
    "[0] Zurueck        "
]