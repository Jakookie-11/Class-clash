# Class Clash

**Class Clash** ist ein deutschsprachiges, rundenbasiertes Konsolenspiel in der Beta-Phase. Stelle dein Team zusammen, entwickle deine Charaktere weiter und bestreite die Kampagne auf dem Mars.

> **Hinweis:** Das Spiel befindet sich noch in Entwicklung. Fehler können auftreten. Bitte melde Probleme mit dem automatisch erzeugten Fehlerbericht als GitHub-Issue.

## Funktionen

- Benutzerkonto mit Registrierung und Anmeldung
- Benutzerdefinierte Kämpfe
- Kampagne **Down in Mars**
- Charakterbibliothek zum Anzeigen und Leveln der Charaktere
- Shop für Credits, Material und Energie
- Profil- und Passworteinstellungen
- Automatisches Speichern der Spielstände
- Crash-Reports zur Unterstützung bei der Fehlersuche
- Prüfung auf verfügbare Updates über GitHub-Releases

## Voraussetzungen

- Python 3.14 oder eine kompatible Python-Version
- Eine Konsole beziehungsweise ein Terminal
- Internetzugang nur für Updates erforderlich

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

   Optional empfiehlt sich dafür eine virtuelle Umgebung:

   ```bash
   python -m venv .venv
   ```

   Windows:

   ```bash
   .venv\Scripts\activate
   ```

   Linux/macOS:

   ```bash
   source .venv/bin/activate
   ```

## Starten

```bash
python main.py
```

Beim ersten Start wählst du das Betriebssystem aus, damit das Spiel den Bildschirm korrekt leeren kann. Anschließend kannst du ein Konto registrieren oder dich anmelden.

## Spielstände und lokale Daten

Lokale Spielstände und Profile werden im Ordner [`saves/`](./saves/) gespeichert. Der Ordner wird beim ersten Start automatisch angelegt. Teile die darin enthaltenen Dateien nicht öffentlich, da sie zu deinem lokalen Spielprofil gehören.

## Projektstruktur

| Datei/Ordner | Beschreibung |
| --- | --- |
| [`main.py`](./main.py) | Einstiegspunkt und Hauptspielschleife |
| [`begin.py`](./begin.py) | Ersteinrichtung, Registrierung und Anmeldung |
| [`neues_spiel.py`](./neues_spiel.py) | Benutzerdefinierte Kämpfe und Kampagnenstart |
| [`kampange.py`](./kampange.py) | Kampagnenlogik |
| [`charaktere.py`](./charaktere.py) | Charakterdaten und -funktionen |
| [`charakter_bip.py`](./charakter_bip.py) | Charakterbibliothek |
| [`shop.py`](./shop.py) | Shop und Ressourcen |
| [`speichern.py`](./speichern.py) | Speichern und Laden lokaler Daten |
| [`crash_handler.py`](./crash_handler.py) | Erstellen von Fehlerberichten |
| [`Down_in_Mars/`](./Down_in_Mars/) | Kampagnentexte |

## Version und Releases

Die aktuelle lokale Version steht in [`version.txt`](./version.txt). Changelogs und veröffentlichte Versionen findest du auf der [Releases-Seite](https://github.com/Jakookie-11/Class-clash/releases).

## Fehler melden

Wenn ein Fehler auftritt:

1. Starte das Spiel bei Bedarf erneut und notiere die angezeigte Fehler-ID.
2. Füge den erzeugten Fehlerbericht deiner Meldung bei.
3. Erstelle ein [neues GitHub-Issue](https://github.com/Jakookie-11/Class-clash/issues/new) mit einer kurzen Beschreibung der Schritte, die zum Fehler geführt haben.

## Mitwirken

Verbesserungsvorschläge, Fehlerberichte und Pull Requests sind willkommen. Beschreibe bei Änderungen möglichst klar, was angepasst wurde und wie die Änderung getestet wurde.

