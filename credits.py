import os
import time

import confic

import probleme
import funktions


def credits():

    while True:

        os.system(confic.terminal_clear)

        print("══════════════════════════════")
        print("            CREDITS")
        print("══════════════════════════════")
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

        print("══════════════════════════════")
        print("          CLASS CLASH")
        print("            © 2026")
        print("══════════════════════════════")
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

            fertig = input("fertig? ")

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
    print(f"════{von_wem_gemeldet}════")
    print()

    for problem in probleme.probleme[von_wem_gemeldet]:
        print(f"----{problem['id']}----")
        print(f"Beschreibung: {problem['beschreibung']}")
        print(f"Status      : {problem['status']}")
        print()
