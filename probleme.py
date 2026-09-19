def behobene_fehler_herausfinden(von_wem_gemeldet):
    fehler = probleme[von_wem_gemeldet]

    behoben = 0

    for problem in fehler:
        if problem["status"] == "behoben":
            behoben += 1

    return behoben


def gesamte_fehler_herausfinden(von_wem_gemeldet):
    fehler = probleme[von_wem_gemeldet]

    gesamt = 0

    for problem in fehler:
        gesamt += 1

    return gesamt





probleme = {
    "Leonard": [
        {
            "id": "CC-001",
            "beschreibung": "Falsche Beschreibung der Stärkenden Heilung",
            "status": "behoben"
        },
        {
            "id": "CC-002",
            "beschreibung": "Im Shop werden die Ressourcen nicht angezeigt",
            "status": "behoben"
        },
        {
            "id": "CC-003",
            "beschreibung": "Kein resetten der Apklingzeiten nach dem Kampf",
            "status": "behoben"  
        },
        {
            "id": "CC-004",
            "beschreibung": "Lovis heisst Lovis_H und nicht Lovis",
            "status": "behoben"
        },
        {
            "id": "CC-005",
            "beschreibung": "Ganzes Gegnerteam tot, aber kein Win_Bildschirm",
            "status": "behoben"
        },
        {
            "id": "CC-06",
            "beschreibung": "Fehler beim Leveln in 1.03.01",
            "status": "behoben"
        },  
        {
            "id": "CC-07",
            "beschreibung": "Kein resetten der Cooldowns in 1.03.01",
            "status": "behoben"
        }, 
    ]
}