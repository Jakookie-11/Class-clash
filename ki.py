import time
import os
import random
import charaktere


def ki_zug(wer, team_1, team_2, Stufe_der_KI=1):

    charakter = charaktere.Charaktere[wer]

    print(f"{wer} wird von der KI gesteuert!")
    time.sleep(2)

    faehigkeiten = [
        charakter.faehigkeit_1,
        charakter.faehigkeit_2,
        charakter.faehigkeit_3
    ]

    verfuegbare_faehigkeiten = []

    for faehigkeit in faehigkeiten:
        if faehigkeit.abklingzeit == 0:
            verfuegbare_faehigkeiten.append(faehigkeit)

    # =========================
    # KI STUFE 1
    # =========================

    if Stufe_der_KI == 1:

        ausgewaehlte_faehigkeit = random.choice(verfuegbare_faehigkeiten)

        print(ausgewaehlte_faehigkeit.name)

        ausgewaehlte_faehigkeit_zieltyp = ausgewaehlte_faehigkeit.zieltyp

        if ausgewaehlte_faehigkeit_zieltyp == "gegner":
            ziel = random.choice(team_1)

        elif ausgewaehlte_faehigkeit_zieltyp == "verbündete":
            ziel = random.choice(team_2)

        print(ziel)

        time.sleep(3)

        return ausgewaehlte_faehigkeit, ziel

    # =========================
    # KI STUFE 2
    # =========================

    elif Stufe_der_KI == 2:

        verfuegbare_heilungs_faehigkeiten = []
        verfuegbare_angriffs_faehigkeiten = []

        for faehigkeit in verfuegbare_faehigkeiten:

            if faehigkeit.zieltyp == "verbündete":
                verfuegbare_heilungs_faehigkeiten.append(faehigkeit)

            elif faehigkeit.zieltyp == "gegner":
                verfuegbare_angriffs_faehigkeiten.append(faehigkeit)

        # -------------------------
        # Eigene Charaktere mit wenig HP
        # -------------------------

        charaktere_Team_2_mit_low_HP = []

        for charakter_name in team_2:

            charakter = charaktere.Charaktere[charakter_name]

            if charakter.hp <= charakter.max_hp * 0.3 and charakter.hp >= 0:
                charaktere_Team_2_mit_low_HP.append(charakter_name)

        charaktere_Team_2_mit_low_HP.sort(
            key=lambda charakter_name:
            charaktere.Charaktere[charakter_name].hp
        )

        # -------------------------
        # Gegner mit wenig HP
        # -------------------------

        charaktere_Team_1_mit_low_HP = []

        for charakter_name in team_1:

            charakter = charaktere.Charaktere[charakter_name]

            if charakter.hp <= charakter.max_hp * 0.3 and charakter.hp >= 0:
                charaktere_Team_1_mit_low_HP.append(charakter_name)

        charaktere_Team_1_mit_low_HP.sort(
            key=lambda charakter_name:
            charaktere.Charaktere[charakter_name].hp
        )

        # =========================
        # MÖGLICHKEITEN
        # =========================

        # Eigener Charakter hat wenig HP
        # UND es gibt eine Heilfähigkeit

        if (
            charaktere_Team_2_mit_low_HP != []
            and verfuegbare_heilungs_faehigkeiten != []
        ):

            faehigkeit = random.choice(
                verfuegbare_heilungs_faehigkeiten
            )

            ziel = charaktere_Team_2_mit_low_HP[0]

            print(faehigkeit.name)
            print(ziel)
            time.sleep(3)
            return faehigkeit, ziel

        # Gegner hat wenig HP

        elif charaktere_Team_1_mit_low_HP != []:

            faehigkeit = random.choice(
                verfuegbare_angriffs_faehigkeiten
            )

            ziel = charaktere_Team_1_mit_low_HP[0]

            print(faehigkeit.name)
            print(ziel)
            time.sleep(3)
            return faehigkeit, ziel

        # Keine besondere Situation:
        # irgendeine verfügbare Fähigkeit benutzen

        else:

            faehigkeit = random.choice(
                verfuegbare_faehigkeiten
            )

            ausgewaehlte_faehigkeit_zieltyp = faehigkeit.zieltyp

            if ausgewaehlte_faehigkeit_zieltyp == "gegner":
                ziel = random.choice(team_1)

            elif ausgewaehlte_faehigkeit_zieltyp == "verbündete":
                ziel = random.choice(team_2)

            print(faehigkeit.name)
            print(ziel)
            time.sleep(3)
            return faehigkeit, ziel