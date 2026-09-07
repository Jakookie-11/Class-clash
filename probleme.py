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
        }
    ]
}