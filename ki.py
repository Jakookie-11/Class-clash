import time
import random
import charaktere
import status_effekte
import faehigkeiten


# ══════════════════════════════════════════════════════════════
# KI-Einstellungen
# ══════════════════════════════════════════════════════════════

GEWINNEN = 10000
TOETEN = 5000
VERLIEREN = -10000

HP_GEWICHT = 2
SCHADEN_GEWICHT = 3
HEILUNG_GEWICHT = 2
BUFF_GEWICHT = 800
DEBUFF_GEWICHT = 700
BETAEUBUNG_GEWICHT = 1200


# ══════════════════════════════════════════════════════════════
# Hilfsfunktionen
# ══════════════════════════════════════════════════════════════


def hp_prozent(name):

    charakter = charaktere.Charaktere[name]

    if charakter.max_hp <= 0:
        return 0

    return charakter.hp / charakter.max_hp


def ist_am_leben(name):

    return charaktere.Charaktere[name].hp > 0


def team_hp(team):

    hp = 0

    for name in team:

        charakter = charaktere.Charaktere[name]

        if charakter.hp > 0:
            hp += charakter.hp

    return hp


def team_max_hp(team):

    hp = 0

    for name in team:
        hp += charaktere.Charaktere[name].max_hp

    return hp


def anzahl_lebende(team):

    anzahl = 0

    for name in team:

        if ist_am_leben(name):
            anzahl += 1

    return anzahl


def hat_status(name, status_name):

    return status_effekte.status_effekt_vorhanden(
        name,
        status_name
    )


# ══════════════════════════════════════════════════════════════
# Zielauswahl
# ══════════════════════════════════════════════════════════════


def moegliche_ziele(faehigkeit, team_1, team_2):

    if faehigkeit.zieltyp == "gegner":

        return [
            name
            for name in team_1
            if ist_am_leben(name)
        ]

    elif faehigkeit.zieltyp == "verbündete":

        return [
            name
            for name in team_2
            if ist_am_leben(name)
        ]

    return []


def zufaellige_aktion(faehigkeiten_liste, team_1, team_2):

    aktionen = []

    for faehigkeit in faehigkeiten_liste:

        ziele = moegliche_ziele(
            faehigkeit,
            team_1,
            team_2
        )

        if ziele:
            aktionen.append((faehigkeit, ziele))

    if not aktionen:
        return None, None

    faehigkeit, ziele = random.choice(aktionen)

    return faehigkeit, random.choice(ziele)


# ══════════════════════════════════════════════════════════════
# Gefährlichkeit eines Charakters
# ══════════════════════════════════════════════════════════════


def gefaehrlichkeit(name):

    charakter = charaktere.Charaktere[name]

    wert = 0

    # Schaden
    wert += abs(charakter.schaden) * 10

    # Geschwindigkeit
    wert += charakter.speed * 2

    # Niedrige HP
    if hp_prozent(name) <= 0.3:
        wert += 500

    faehigkeiten = [
        charakter.faehigkeit_1,
        charakter.faehigkeit_2,
        charakter.faehigkeit_3
    ]

    # Charaktere mit Heilfähigkeiten sind gefährlicher
    for faehigkeit in faehigkeiten:

        if faehigkeit is None:
            continue

        if faehigkeit.zieltyp == "verbündete":
            wert += 300

    return wert


# ══════════════════════════════════════════════════════════════
# Fähigkeit bewerten
# ══════════════════════════════════════════════════════════════


def faehigkeit_bewerten(
    wer,
    wen,
    faehigkeit,
    eigenes_team,
    gegner_team
):

    charakter = charaktere.Charaktere[wer]
    ziel = charaktere.Charaktere[wen]

    wert = 0

    name = faehigkeit.name.lower()

    # ══════════════════════════════════════════════════════════
    # Angriff
    # ══════════════════════════════════════════════════════════

    if faehigkeit.zieltyp == "gegner":

        erwarteter_schaden = abs(charakter.schaden)

        wert += erwarteter_schaden * SCHADEN_GEWICHT

        # Gegner kann getötet werden
        if ziel.hp <= erwarteter_schaden:

            wert += TOETEN

        # Sehr verletzte Gegner priorisieren
        if hp_prozent(wen) <= 0.2:

            wert += 1500

        elif hp_prozent(wen) <= 0.4:

            wert += 600

        # Gefährliche Gegner priorisieren
        wert += gefaehrlichkeit(wen)

        # Betäubung
        if "starker" in name or "horden" in name:

            if not hat_status(wen, "betaeubt"):

                wert += BETAEUBUNG_GEWICHT

        # Schaden über Zeit
        if "bleibender" in name:

            if not hat_status(wen, "damage_over_time_1"):

                wert += 500

        # Gegner schwächen
        if "blutig" in name or "falsch" in name:

            if not hat_status(wen, "schaden_minus"):

                wert += DEBUFF_GEWICHT

    # ══════════════════════════════════════════════════════════
    # Heilung / Buffs
    # ══════════════════════════════════════════════════════════

    elif faehigkeit.zieltyp == "verbündete":

        fehlende_hp = ziel.max_hp - ziel.hp

        wert += fehlende_hp * HEILUNG_GEWICHT

        # Sehr verletzte Charaktere stark priorisieren
        if hp_prozent(wen) <= 0.2:

            wert += 2500

        elif hp_prozent(wen) <= 0.4:

            wert += 1000

        # Heilung auf volle HP vermeiden
        if ziel.hp >= ziel.max_hp:

            wert -= 2000

        # Buffs
        if "staerkend" in name or "sonnenbrille" in name:

            if not hat_status(wen, "schaden_plus"):

                wert += BUFF_GEWICHT

    # ══════════════════════════════════════════════════════════
    # Gesamtsituation
    # ══════════════════════════════════════════════════════════

    eigene_hp = team_hp(eigenes_team)
    gegner_hp = team_hp(gegner_team)

    # Eigenes Team ist stark angeschlagen
    if eigene_hp < team_max_hp(eigenes_team) * 0.3:

        wert += 300

    # Gegner ist fast besiegt
    if gegner_hp < team_max_hp(gegner_team) * 0.25:

        wert += 500

    return wert


# ══════════════════════════════════════════════════════════════
# Beste Aktion finden
# ══════════════════════════════════════════════════════════════


def beste_aktion(wer, team_1, team_2):

    charakter = charaktere.Charaktere[wer]

    faehigkeiten = [
        charakter.faehigkeit_1,
        charakter.faehigkeit_2,
        charakter.faehigkeit_3
    ]

    verfuegbare_faehigkeiten = []

    for faehigkeit in faehigkeiten:

        if faehigkeit is None:
            continue

        if faehigkeit.abklingzeit == 0:

            verfuegbare_faehigkeiten.append(
                faehigkeit
            )

    if not verfuegbare_faehigkeiten:

        return None, None

    beste_faehigkeit = None
    bestes_ziel = None
    bester_wert = -999999

    # Jede Fähigkeit testen
    for faehigkeit in verfuegbare_faehigkeiten:

        ziele = moegliche_ziele(
            faehigkeit,
            team_1,
            team_2
        )

        # Jedes mögliche Ziel testen
        for ziel in ziele:

            wert = faehigkeit_bewerten(
                wer,
                ziel,
                faehigkeit,
                team_2,
                team_1
            )

            # Kleine Zufälligkeit verhindert,
            # dass die KI immer exakt gleich handelt
            wert += random.uniform(-20, 20)

            if wert > bester_wert:

                bester_wert = wert
                beste_faehigkeit = faehigkeit
                bestes_ziel = ziel

    return beste_faehigkeit, bestes_ziel




# ══════════════════════════════════════════════════════════════
# KI STUFE 4
# Mehrere Züge vorausdenken
# ══════════════════════════════════════════════════════════════


def charakter_grundwert(name):

    charakter = charaktere.Charaktere[name]

    wert = 0

    # Lebenspunkte
    wert += charakter.hp * 2

    # Schaden
    wert += abs(charakter.schaden) * 8

    # Geschwindigkeit
    wert += charakter.speed * 2

    # Lebende Charaktere sind sehr wichtig
    if charakter.hp > 0:
        wert += 500

    return wert


def team_wert(team):

    wert = 0

    for name in team:

        charakter = charaktere.Charaktere[name]

        if charakter.hp <= 0:
            continue

        wert += charakter_grundwert(name)

        # Buffs
        if hat_status(name, "schaden_plus"):
            wert += 500

        # Debuffs
        if hat_status(name, "schaden_minus"):
            wert -= 400

        # Betäubung
        if hat_status(name, "betaeubt"):
            wert -= 700

        # Schaden über Zeit
        if hat_status(name, "damage_over_time_1"):
            wert -= 300

    return wert


def stellung_bewerten(eigenes_team, gegner_team):

    eigener_wert = team_wert(eigenes_team)
    gegner_wert = team_wert(gegner_team)

    return eigener_wert - gegner_wert


def virtuelle_schadens_bewertung(wer, wen, faehigkeit):

    charakter = charaktere.Charaktere[wer]
    ziel = charaktere.Charaktere[wen]

    schaden = abs(charakter.schaden)

    name = faehigkeit.name.lower()

    # Fähigkeiten mit erhöhtem Schaden
    if "ranzenwurf" in name:
        schaden *= 2

    return schaden


def virtuelle_heilung(faehigkeit):

    if faehigkeit.name == "einfache_heilung":
        return 50

    if faehigkeit.name == "staerkende_heilung":
        return 50

    if faehigkeit.name == "hausaufgaben_zeigen":
        return 40

    return 0


def virtuelle_aktion_bewerten(
    wer,
    wen,
    faehigkeit,
    eigenes_team,
    gegner_team
):

    ziel = charaktere.Charaktere[wen]

    wert = stellung_bewerten(
        eigenes_team,
        gegner_team
    )

    # ══════════════════════════════════════════════════════════
    # Angriff simulieren
    # ══════════════════════════════════════════════════════════

    if faehigkeit.zieltyp == "gegner":

        schaden = virtuelle_schadens_bewertung(
            wer,
            wen,
            faehigkeit
        )

        neuer_hp = ziel.hp - schaden

        # Töten ist extrem wertvoll
        if neuer_hp <= 0:

            wert += 10000

        else:

            # Schaden selbst ist wertvoll
            wert += schaden * 10

            # Gegner mit wenig HP werden priorisiert
            if neuer_hp <= ziel.max_hp * 0.2:
                wert += 1500

            elif neuer_hp <= ziel.max_hp * 0.4:
                wert += 700

        # Besondere Effekte
        if "starker" in faehigkeit.name:

            if not hat_status(wen, "betaeubt"):
                wert += 1500

        if "horden" in faehigkeit.name:

            if not hat_status(wen, "betaeubt"):
                wert += 1500

        if "blutig" in faehigkeit.name:

            if not hat_status(wen, "schaden_minus"):
                wert += 800

        if "bleibender" in faehigkeit.name:

            if not hat_status(wen, "damage_over_time_1"):
                wert += 700

    # ══════════════════════════════════════════════════════════
    # Heilung simulieren
    # ══════════════════════════════════════════════════════════

    elif faehigkeit.zieltyp == "verbündete":

        heilung = virtuelle_heilung(
            faehigkeit
        )

        fehlende_hp = ziel.max_hp - ziel.hp

        tatsaechliche_heilung = min(
            heilung,
            max(0, fehlende_hp)
        )

        wert += tatsaechliche_heilung * 8

        # Fast tote Charaktere retten
        if hp_prozent(wen) <= 0.2:

            wert += 3000

        elif hp_prozent(wen) <= 0.4:

            wert += 1200

        # Heilung auf volle HP ist schlecht
        if fehlende_hp <= 0:

            wert -= 2500

        # Buff
        if (
            faehigkeit.name == "staerkende_heilung"
            or faehigkeit.name == "sonnenbrille_auf"
        ):

            if not hat_status(wen, "schaden_plus"):

                wert += 1000

    return wert


def beste_aktion_stufe_4(
    wer,
    team_1,
    team_2
):

    charakter = charaktere.Charaktere[wer]

    faehigkeiten = [
        charakter.faehigkeit_1,
        charakter.faehigkeit_2,
        charakter.faehigkeit_3
    ]

    verfuegbare_faehigkeiten = []

    for faehigkeit in faehigkeiten:

        if faehigkeit is None:
            continue

        if faehigkeit.abklingzeit == 0:

            verfuegbare_faehigkeiten.append(
                faehigkeit
            )

    if not verfuegbare_faehigkeiten:

        return None, None

    beste_faehigkeit = None
    bestes_ziel = None
    bester_wert = -999999

    # ══════════════════════════════════════════════════════════
    # ALLE MÖGLICHEN ZÜGE DURCHPROBIEREN
    # ══════════════════════════════════════════════════════════

    for faehigkeit in verfuegbare_faehigkeiten:

        ziele = moegliche_ziele(
            faehigkeit,
            team_1,
            team_2
        )

        for ziel in ziele:

            aktueller_wert = virtuelle_aktion_bewerten(
                wer,
                ziel,
                faehigkeit,
                team_2,
                team_1
            )

            # ══════════════════════════════════════════════
            # GEGENREAKTION DES GEGNERS
            # ══════════════════════════════════════════════

            gegnerische_beste_aktion = None
            gegnerischer_wert = -999999

            for gegner_name in team_1:

                if not ist_am_leben(gegner_name):
                    continue

                gegner = charaktere.Charaktere[gegner_name]

                gegner_faehigkeiten = [
                    gegner.faehigkeit_1,
                    gegner.faehigkeit_2,
                    gegner.faehigkeit_3
                ]

                for gegner_faehigkeit in gegner_faehigkeiten:

                    if gegner_faehigkeit is None:
                        continue

                    if gegner_faehigkeit.abklingzeit != 0:
                        continue

                    gegner_ziele = moegliche_ziele(
                        gegner_faehigkeit,
                        team_2,
                        team_1
                    )

                    for gegner_ziel in gegner_ziele:

                        gegenwert = virtuelle_aktion_bewerten(
                            gegner_name,
                            gegner_ziel,
                            gegner_faehigkeit,
                            team_1,
                            team_2
                        )

                        if gegenwert > gegnerischer_wert:

                            gegnerischer_wert = gegenwert
                            gegnerische_beste_aktion = (
                                gegner_faehigkeit,
                                gegner_ziel
                            )

            # ══════════════════════════════════════════════
            # KI berücksichtigt Gegenreaktion
            # ══════════════════════════════════════════════

            endwert = aktueller_wert - (
                gegnerischer_wert * 0.6
            )

            # Kleine Zufälligkeit
            endwert += random.uniform(-10, 10)

            if endwert > bester_wert:

                bester_wert = endwert
                beste_faehigkeit = faehigkeit
                bestes_ziel = ziel

    return beste_faehigkeit, bestes_ziel






# ══════════════════════════════════════════════════════════════
# KI-Zug
# ══════════════════════════════════════════════════════════════


def ki_zug(wer, team_1, team_2, Stufe_der_KI=1):

    charakter = charaktere.Charaktere[wer]

    print(f"{wer} wird von der KI gesteuert!")
    time.sleep(1)

    # ══════════════════════════════════════════════════════════
    # KI STUFE 1
    # Zufällige KI
    # ══════════════════════════════════════════════════════════

    if Stufe_der_KI == 1:

        faehigkeiten = [
            charakter.faehigkeit_1,
            charakter.faehigkeit_2,
            charakter.faehigkeit_3
        ]

        verfuegbare_faehigkeiten = [
            faehigkeit
            for faehigkeit in faehigkeiten
            if faehigkeit is not None
            and faehigkeit.abklingzeit == 0
        ]

        if not verfuegbare_faehigkeiten:
            verfuegbare_faehigkeiten = [faehigkeiten.einfacher_angriff]

        faehigkeit, ziel = zufaellige_aktion(
            verfuegbare_faehigkeiten,
            team_1,
            team_2
        )

        if faehigkeit is None:
            return None, None

        print()
        print("═════════════════════════")
        print("       KI-ANALYSE")
        print("═════════════════════════")
        print()
        print("Die KI entscheidet zufällig.")
        print()
        print(f"Fähigkeit : {faehigkeit.name}")
        print(f"Ziel      : {ziel}")
        print()
        print(f"Erklärung : {faehigkeit.erklaerung}")
        print()
        print("═════════════════════════")
        print()

        input("Enter...")

        return faehigkeit, ziel


    # ══════════════════════════════════════════════════════════
    # KI STUFE 2
    # Deine bisherige taktische KI
    # ══════════════════════════════════════════════════════════

    elif Stufe_der_KI == 2:

        eigene_low_hp = []

        for name in team_2:

            if (
                ist_am_leben(name)
                and hp_prozent(name) <= 0.3
            ):

                eigene_low_hp.append(name)

        gegner_low_hp = []

        for name in team_1:

            if (
                ist_am_leben(name)
                and hp_prozent(name) <= 0.3
            ):

                gegner_low_hp.append(name)

        heilungen = []
        angriffe = []

        for faehigkeit in [
            charakter.faehigkeit_1,
            charakter.faehigkeit_2,
            charakter.faehigkeit_3
        ]:

            if faehigkeit is None:
                continue

            if faehigkeit.abklingzeit != 0:
                continue

            if faehigkeit.zieltyp == "verbündete":

                heilungen.append(faehigkeit)

            elif faehigkeit.zieltyp == "gegner":

                angriffe.append(faehigkeit)

        if eigene_low_hp and heilungen:

            ziel = min(
                eigene_low_hp,
                key=lambda name:
                charaktere.Charaktere[name].hp
            )

            faehigkeit = random.choice(heilungen)

            print()
            print("═════════════════════════")
            print("       KI-ANALYSE")
            print("═════════════════════════")
            print()
            print("Die KI hat einen verletzten Verbündeten erkannt.")
            print()
            print(f"Fähigkeit : {faehigkeit.name}")
            print(f"Ziel      : {ziel}")
            print()
            print(f"Erklärung : {faehigkeit.erklaerung}")
            print()
            print("═════════════════════════")
            print()

            input("Enter...")

            return faehigkeit, ziel

        if gegner_low_hp and angriffe:

            ziel = min(
                gegner_low_hp,
                key=lambda name:
                charaktere.Charaktere[name].hp
            )

            faehigkeit = random.choice(angriffe)

            print()
            print("═════════════════════════")
            print("       KI-ANALYSE")
            print("═════════════════════════")
            print()
            print("Die KI hat einen stark geschwächten Gegner erkannt.")
            print()
            print(f"Fähigkeit : {faehigkeit.name}")
            print(f"Ziel      : {ziel}")
            print()
            print(f"Erklärung : {faehigkeit.erklaerung}")
            print()
            print("═════════════════════════")
            print()

            input("Enter...")

            return faehigkeit, ziel

        verfuegbare_faehigkeiten = [
            f
            for f in [
                charakter.faehigkeit_1,
                charakter.faehigkeit_2,
                charakter.faehigkeit_3
            ]
            if f is not None and f.abklingzeit == 0
        ]

        if not verfuegbare_faehigkeiten:
            verfuegbare_faehigkeiten = [faehigkeiten.einfacher_angriff]

        faehigkeit, ziel = zufaellige_aktion(
            verfuegbare_faehigkeiten,
            team_1,
            team_2
        )

        if faehigkeit is None:
            return None, None

        print()
        print("═════════════════════════")
        print("       KI-ANALYSE")
        print("═════════════════════════")
        print()
        print("Kein besonderer taktischer Vorteil erkannt.")
        print("Die KI wählt daher eine verfügbare Fähigkeit.")
        print()
        print(f"Fähigkeit : {faehigkeit.name}")
        print(f"Ziel      : {ziel}")
        print()
        print(f"Erklärung : {faehigkeit.erklaerung}")
        print()
        print("═════════════════════════")
        print()

        input("Enter...")

        return faehigkeit, ziel

    # ══════════════════════════════════════════════════════════
    # KI STUFE 3
    # KRASSE TAKTISCHE KI
    # ══════════════════════════════════════════════════════════

    elif Stufe_der_KI == 3:

        faehigkeit, ziel = beste_aktion(
            wer,
            team_1,
            team_2
        )

        if faehigkeit is None:
            faehigkeit, ziel = zufaellige_aktion(
                [faehigkeiten.einfacher_angriff],
                team_1,
                team_2
            )

        if faehigkeit is None:
            return None, None

        print()
        print("═════════════════════════")
        print("       KI-ANALYSE")
        print("═════════════════════════")
        print()
        print(f"Fähigkeit : {faehigkeit.name}")
        print(f"Ziel      : {ziel}")
        print()
        print(f"Erklärung : {faehigkeit.erklaerung}")
        print()
        print("═════════════════════════")
        print()

        input("Enter...")

        return faehigkeit, ziel

    

    # ══════════════════════════════════════════════════════════
    # KI STUFE 4
    # Simulation + Gegenreaktion
    # ══════════════════════════════════════════════════════════

    elif Stufe_der_KI == 4:

        faehigkeit, ziel = beste_aktion_stufe_4(
            wer,
            team_1,
            team_2
        )

        if faehigkeit is None:
            faehigkeit, ziel = zufaellige_aktion(
                [faehigkeiten.einfacher_angriff],
                team_1,
                team_2
            )

        if faehigkeit is None:
            return None, None

        print()
        print("═════════════════════════")
        print("       KI-ANALYSE")
        print("═════════════════════════")
        print()
        print("Die KI simuliert mögliche Züge...")
        time.sleep(1)
        print()
        print(f"Fähigkeit : {faehigkeit.name}")
        print(f"Ziel      : {ziel}")
        print()
        print(f"Erklärung : {faehigkeit.erklaerung}")
        print()
        print("═════════════════════════")
        print()

        input("Enter...")

        return faehigkeit, ziel