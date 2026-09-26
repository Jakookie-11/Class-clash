import os
import time

import confic

import probleme
import funktions


SCHWARZ  = "\033[30m"
ROT      = "\033[31m"
GRUEN    = "\033[32m"
GELB     = "\033[33m"
BLAU     = "\033[34m"
MAGENTA  = "\033[35m"
CYAN     = "\033[36m"
WEISS    = "\033[37m"

RESET    = "\033[0m"

HELL_GRAU     = "\033[90m"
HELL_ROT      = "\033[91m"
HELL_GRUEN    = "\033[92m"
HELL_GELB     = "\033[93m"
HELL_BLAU     = "\033[94m"
HELL_MAGENTA  = "\033[95m"
HELL_CYAN     = "\033[96m"
HELL_WEISS    = "\033[97m"


def credits():

    while True:

        os.system(confic.terminal_clear)

        print(f"{MAGENTA}══════════════════════════════")
        print("            CREDITS")
        print(f"══════════════════════════════{RESET}")
        print()

        print("---Coder---")
        print("Jakob")
        print()

        print("PROBLEMFINDUNG")
        print()

        probleme_finder_anzeigen(clear=False)
        print()

        print("BESONDERER DANK")
        print("- An alle, die das Spiel getestet und Fehler gemeldet haben.")
        print("- Meine Klasse, die unfreiwillig an diesem Experiment teilnimmt")
        print()

        print(f"{MAGENTA}══════════════════════════════")
        print("          CLASS CLASH")
        print("            © 2026")
        print(f"══════════════════════════════{RESET}")
        print()
        print()

        genauere_informationen_zu_findern = input("möchtest du mehr über eine(n) Problemfinder(in) herausfinden? ")

        if genauere_informationen_zu_findern == "ja":

            funktions.zeilen_loeschen(1)

            while True:

                zu_wem = input("zu Wem? ")

                if zu_wem not in probleme.probleme:
                    print()
                    print("Diese Person hat keine Fehler gefunden")
                    time.sleep(2)
                    funktions.zeilen_loeschen(3)
                    continue

                elif zu_wem == "":
                    return 1

                else:
                    break

            probleme_anzeigen(zu_wem)

            input("fertig? ")

        else:
            return 1

  


def probleme_finder_anzeigen(clear=True):

    if clear == True:
        os.system(confic.terminal_clear)

    print("----Leute die Probleme gemeldet haben----")
    print()

    for leute_die_gemeldet_haben in probleme.probleme:

        behoben = 0

        for problem in probleme.probleme[leute_die_gemeldet_haben]:

            if problem["status"] == "behoben":
                behoben += 1
        
        print(f"Name: {leute_die_gemeldet_haben:<10} Probleme gemeldet: {len(probleme.probleme[leute_die_gemeldet_haben]) :<3}Davon behoben: {behoben}")







def probleme_anzeigen(von_wem_gemeldet):

    os.system(confic.terminal_clear)
    print(f"{CYAN}════ {von_wem_gemeldet} ════{RESET}")
    print()

    for problem in probleme.probleme[von_wem_gemeldet]:
        print(f"{HELL_MAGENTA}----{problem['id']}----{RESET}")
        print(f"Beschreibung: {problem['beschreibung']}")
        if problem['status'] == "behoben":
            print(f"{GRUEN}Status      : {problem['status']}{RESET}")
        else:
            print(f"{HELL_ROT}Status      : {problem['status']}{RESET}")
        print()
