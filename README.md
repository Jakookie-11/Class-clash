# Class Clash

Class Clash ist ein deutschsprachiges, rundenbasiertes Konsolenspiel mit Charakterauswahl, Kampagnen, Herausforderungen, Shop, Profilverwaltung und lokalen Spielständen. Das Spiel steckt noch in der Beta-Phase, ist aber bereits mit mehreren Spielmodi, eigener Charakter-Progression und einer längeren Story ausgestattet.

> Hinweis: Das Spiel befindet sich weiterhin in der Entwicklung. Fehler, unvollständige Inhalte und Balance-Änderungen können vorkommen. Bitte nutze die eingebetteten Fehlerberichte und melde Bugs über GitHub.

> PDF-Versionen der wichtigsten Hilfen sind ebenfalls im Projektordner verfügbar: `README.pdf`, `More info.pdf` und `Class Clash – Installation unter Windows.pdf`.

Für einen portablen Windows-Build als EXE siehe [Abschnitt 9 der Installationsanleitung](./Class%20Clash%20%E2%80%93%20Installation%20unter%20Windows.md#9-class-clash-als-exe-bauen-und-weitergeben). Der Build benötigt 64-Bit-CPython 3.15; auf dem PC, auf dem die fertige EXE gestartet wird, ist Python nicht erforderlich.

## Überblick

Class Clash kombiniert:

- ein eigenes Konto-System mit Registrierung und Anmeldung
- benutzerdefinierte Kämpfe gegen die KI oder einen zweiten lokalen Spieler
- Kampagnen mit Story, Dialogen und Boss-ähnlichen Gefechten
- Herausforderungen und Spezialkämpfe
- Charakterbibliothek mit Leveln und Statistiken
- Shop für Credits, Materialien und Energie
- Profil-, Audio- und Einstellungsmöglichkeiten
- automatisches Speichern und Crash-Reports
- Update-Prüfung über GitHub Releases

## Hauptfunktionen

### 1) Konto- und Profilsystem

- Registrierung und Anmeldung im Startmenü
- Passwortänderung und Passwortsichtbarkeit
- Profilinformationen anzeigen
- Profil zurücksetzen oder löschen
- Admin-Zugang im Anmelde-Menü
- lokale Speicherung der Kontodaten in `saves/`

### 2) Benutzerdefinierte Kämpfe

- Teamgröße frei wählbar (1 bis 4 Charaktere pro Team)
- Gegner können entweder von der KI gesteuert sein oder von Person 2 lokal kontrolliert werden
- KI-Stufen von 1 bis 4 verfügbar:
  - 1 = Zufällig
  - 2 = Taktisch
  - 3 = Stark
  - 4 = Meister
- Teamwahl aus den verfügbaren Charakteren
- Auswahl von Gegnern inklusive NPCs/Story-Gegnern je nach Modus

### 3) Kampagnen

Das Spiel enthält mehrere Kampagnen mit aufeinanderfolgenden Kämpfen, Storydialogen und Fortschrittssystem.

Aktuell vorhanden sind unter anderem:

- Kampagne 1: Der 100er Gang
- Kampagne 2: Weitere schulische Konflikte und Feinde
- Kampagne 3: Fortsetzung mit gesteigertem Schwierigkeitsgrad
- Kampagne 4: Die Liste
- Kampagne 5: Projekt K
- Kampagne 6: Down in Mars

Die Kampagne 6 ist die bisher am stärksten ausgearbeitete und wurde für den Beta-Test mit besonderer Aufmerksamkeit auf Balance und Story verständlich gemacht.

Kampagnen enthalten:

- Story-Sequenzen vor und nach Kämpfen
- Dialogfenster mit langsamem Text-Output
- Fortschrittsverwaltung pro Kampagne
- Belohnungen in Credits und Ressourcen
- Reset der Gegner-Level nach Kämpfen

### 4) Herausforderungen

Zusätzlich zu den Kampagnen können spezielle Herausforderungskaempfe gestartet werden. Diese ergänzen das Spiel mit zusätzlichen, oft anspruchsvolleren Gefechten und neuen Herausforderungen.

### 5) Charaktersystem

- Charaktere besitzen eigene Klasse, Level, HP, Schaden und Speed
- Jede Figur hat drei Fähigkeiten
- Charaktere können im Charakter-Menü angezeigt und aufgestockt werden
- Leveln kostet Credits, teilweise zusätzlich Materialien
- Die Charakterwerte werden bei einem Levelaufstieg neu berechnet
- Charakterbilder können in `bilder/` als PNG-Dateien eingebunden werden

### 6) Shop und Ressourcen

Im Shop stehen verschiedene Ressourcen zur Verfügung:

- 1000 Credits
- 1000 M_Credits
- 20 Material 1
- 20 Energie

Der Shop ist durch ein eigenes Shop-Passwort geschützt.

### 7) Einstellungen und Audio

Im Menü "Einstellungen" gibt es:

- Profil
- Audio
- Credits
- Wichtige Links

Audio-Optionen:

- Ton an/aus
- Hintergrundmusik an/aus
- Lautstärke anpassen

### 8) Spielstände und Speicherlogik

- Spielstände werden lokal in `saves/` gespeichert
- Jeder Spieler erhält eigene JSON-Dateien
- Fortschritt, Charakter-Level und Ressourcen werden automatisch gespeichert
- Beim Start wird eine lokale Konfigurationsdatei geladen
- Crash-Reports werden in `crash_logs/` abgelegt

### 9) Fehlerbehandlung und Updates

Das Spiel prüft beim Start die Umgebung und die Python-Version. Falls etwas fehlt, kann es fehlende Abhängigkeiten aus `requirements.txt` automatisch installieren bzw. einen Hinweis geben.

Zusätzlich bietet es:

- Crash-Reports mit Fehler-ID
- lokale Protokoll-Ordner für Abstürze
- GitHub-Release-Check für Updates

## Voraussetzungen

- Windows 64-Bit
- Python 3.15 (64-Bit)
- passende native Erweiterung: `geheimes.cp315-win_amd64.pyd`
- Terminal/Console
- Internetzugang für Updates und ggf. das Laden fehlender Pakete

## Installation

1. Repository klonen:

   ```bash
   git clone https://github.com/Jakookie-11/Class-clash.git
   cd Class-clash
   ```

2. Abhängigkeiten installieren:

   ```bash
   python -m pip install -r requirements.txt
   ```

   Alternativ kann eine virtuelle Umgebung verwendet werden:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Starten:

   ```bash
   python main.py
   ```

## Erster Start

Beim ersten Start fragt das Spiel nach dem Betriebssystem, damit die Konsole korrekt geleert werden kann. Danach kann ein neues Profil erstellt oder ein bestehendes Konto angemeldet werden.

## Spielmodi im Überblick

### Hauptmenü

- Spiel Starten
- Charaktere
- Einstellungen
- Shop
- Herausforderungen
- Beenden

### Menü "Spiel Starten"

- Benutzerdefinierter Kampf
- Kampagne(n)
- Herausforderungskaempfe
- Zurück

### Menü "Charaktere"

- Anzeigen
- Leveln
- Zurück

### Menü "Profil"

- Passwort ändern
- Profil-Daten anzeigen
- Profil zurücksetzen
- Profil löschen
- Passwortsichtbarkeit ändern
- Zurück

## Charakterbilder

Lege eigene Charakterbilder als PNG-Dateien im Ordner `bilder/` ab. Sie sollten im Muster `CC-<Charaktername>.png` benannt sein, z. B.:

```text
CC-Jakob.png
```

Diese Bilder werden im Spiel als Vorschau rechts im Kampf bzw. bei der Auswahl dargestellt.

## Spielstände und lokale Daten

Alle lokalen Daten werden im Ordner `saves/` gespeichert. Der Ordner wird beim ersten Start automatisch angelegt.

Wichtige Dateien:

- `saves/passwoerter.json` – Konten und Passwörter
- `saves/<Spielername>.json` – Spielstände und Fortschritt
- `crash_logs/` – Crash-Daten und Fehlerberichte

> Bitte teile diese Dateien nicht öffentlich, da sie dein lokales Spielprofil enthalten.

## Projektstruktur

```text
Class-clash/
├── begin.py                # Ersteinrichtung und Login/Register
├── main.py                 # Hauptspielschleife und Menüsteuerung
├── kampange.py             # Kampagnenlogik, Story und Kämpfe
├── spiel_starten.py        # Kampfstart, Benutzerkämpfe und KI-Setup
├── charaktere.py           # Charakterdaten, Werte und Basislogik
├── charakter_bip.py        # Charakterbibliothek und Leveln
├── shop.py                 # Shop und Ressourcenfunktionen
├── einstellungen.py        # Profil- und Audio-Einstellungen
├── herausforderungen.py    # Extra-Kampfmodi
├── speichern.py            # Speichern/Laden der Spielstände
├── crash_handler.py        # Fehlerberichte und Absturzprotokolle
├── sound.py                # Audio- und Musikfunktionen
├── menues.py               # Menüdefinitionen
├── ressourcen.py           # Ressourcenverwaltung
├── version.txt             # Aktuelle lokale Version
├── requirements.txt        # Python-Abhängigkeiten
├── README.md               # Projektbeschreibung
├── More info.md            # Zusatzinfos zur Beta und Mitarbeit
├── Class Clash – Installation unter Windows.md
├── Down_in_Mars/           # Kampagnen-Storytexte und Inhalte
├── bilder/                 # Lokale Charakterbilder
├── saves/                  # Spielstände und Profile
├── crash_logs/             # Automatische Fehlerlogs
└── .vscode/                # Editor-Einstellungen
```

## Fehler melden

Wenn ein Fehler auftritt:

1. Das Spiel erneut starten und die Fehler-ID notieren.
2. Die erzeugte Datei im `crash_logs/`-Ordner oder den Fehlerbericht mitnehmen.
3. Ein neues Issue auf GitHub erstellen und den Ablauf sauber beschreiben.

## Mitwirken

Verbesserungsvorschläge, Fehlerberichte und Pull Requests sind willkommen. Besonders hilfreich sind:

- neue Fähigkeiten und Ideen
- Balance-Verbesserungen
- Kampagnen-Feedback
- Story- und Dialogverbesserungen
- Charakterideen oder neue Spielmechaniken
- Testergebnisse und gezielte Bug-Meldungen

## Version und Releases

Die aktuelle lokale Version steht in `version.txt`. Changelogs und veröffentlichte Releases sind auf der GitHub Releases-Seite verfügbar.

## Abschluss

Class Clash ist ein in der Konsole spielbares, storiestriges Kampf- und Charakterspiel mit Kampagnen, Progression, Ressourcen, Profilsystemen und lokaler Spielstände-Logik. Gerade als Beta-Projekt ist es besonders wertvoll, Fehler, Balanceprobleme und Ideen für neue Inhalte zu sammeln.

Viel Spaß beim Spielen und beim Erkunden des Spiels!
