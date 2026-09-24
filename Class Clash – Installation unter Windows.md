# Class Clash – Installation unter Windows

## 1. Python 3.14 herunterladen und installieren

Damit Class Clash funktioniert, benötigst du **Python 3.14 (64-Bit)**.

### Schritt 1: Python herunterladen

1. Öffne die offizielle Python-Downloadseite: [Python für Windows herunterladen](https://www.python.org/downloads/release/python-3147/).
2. Suche nach Python 3.14 und lade den **Windows Installer (64-bit)** herunter.
3. Öffne die heruntergeladene Installationsdatei.

### Schritt 2: Python installieren

Im Installationsfenster:

1. Aktiviere unbedingt die Option **„Add python.exe to PATH“**, falls sie angezeigt wird.
2. Klicke auf **„Install Now“**.
3. Warte, bis die Installation abgeschlossen ist.

### Schritt 3: Installation überprüfen

Öffne PowerShell und gib Folgendes ein:

```powershell
py -3.14 --version
```

Wenn alles funktioniert, sollte eine Ausgabe ähnlich dieser erscheinen:

```text
Python 3.14.x
```

Die genaue Versionsnummer kann abweichen.

---

## 2. Class Clash vorbereiten

1. Lade das Class-Clash-Projekt herunter oder entpacke die bereitgestellte ZIP-Datei.
2. Öffne den Ordner, in dem sich die Datei `requirements.txt` und die `main.py` befinden.

**Wichtig:** Die folgenden Befehle müssen im Hauptordner von Class Clash ausgeführt werden.

---

## 3. PowerShell über die Adressleiste öffnen

Du kannst PowerShell direkt im richtigen Ordner öffnen, ohne den Pfad selbst eingeben zu müssen.

1. Öffne den Class-Clash-Ordner im Datei-Explorer.
2. Klicke oben auf die **Adressleiste**, in der der Ordnerpfad angezeigt wird.
3. Gib dort Folgendes ein:

```text
powershell <- Blauer Hintergrund    cmd <- schwarzer Hintergrund (mag ich lieber)
```

4. Drücke **Enter**.

PowerShell öffnet sich nun direkt in diesem Ordner.

---

## 4. Virtuelle Python-Umgebung erstellen

Eine virtuelle Umgebung sorgt dafür, dass die benötigten Pakete für Class Clash getrennt von anderen Python-Projekten installiert werden.

Gib in PowerShell folgenden Befehl ein:

```powershell
py -3.14 -m venv .venv
```

Dadurch wird im Projektordner ein neuer Ordner namens `.venv` erstellt.

---

## 5. Virtuelle Umgebung aktivieren

Aktiviere die Umgebung mit:

```powershell
.\.venv\Scripts\Activate.ps1
```

Wenn die Aktivierung erfolgreich war, steht am Anfang der PowerShell-Zeile normalerweise:

```text
(.venv)
```

### Falls die Aktivierung blockiert wird

Wenn PowerShell meldet, dass die Ausführung von Skripten nicht erlaubt ist, kannst du die Richtlinie für das aktuelle PowerShell-Fenster vorübergehend lockern:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Bestätige die Eingabe, falls du dazu aufgefordert wirst, und führe anschließend den Aktivierungsbefehl erneut aus.

Diese Einstellung gilt nur für das aktuelle PowerShell-Fenster.

---

## 6. Benötigte Pakete installieren

Class Clash benötigt verschiedene Python-Pakete, die in der Datei `requirements.txt` aufgelistet sind.

Installiere sie mit:

```powershell
python -m pip install -r requirements.txt
```

Python lädt nun automatisch alle benötigten Pakete herunter und installiert sie.

Warte, bis die Installation abgeschlossen ist.

**Hinweis:** Eine aktive Internetverbindung wird benötigt, damit die Pakete heruntergeladen werden können.

---

## 7. Class Clash starten

Wenn die Installation erfolgreich abgeschlossen ist, kannst du das Spiel starten:

```powershell
python main.py
```

Class Clash sollte nun im Terminal starten.

---

## 8. Class Clash bei zukünftigen Starts öffnen

Wenn du das Spiel später erneut starten möchtest, musst du die Pakete nicht noch einmal installieren.

1. Öffne den Class-Clash-Ordner.
2. Gib in der Adressleiste `powershell` ein und drücke Enter.
3. Aktiviere die virtuelle Umgebung:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Starte das Spiel:

```powershell
python main.py
```

---

## 9. Häufige Probleme

### Python wird nicht gefunden

Wenn `py -3.14` nicht funktioniert, überprüfe, ob Python 3.14 installiert wurde.

Du kannst alternativ Folgendes testen:

```powershell
python --version
```

### Die Datei `requirements.txt` wird nicht gefunden

Stelle sicher, dass PowerShell im richtigen Ordner geöffnet wurde.

Die Datei `requirements.txt` muss direkt im aktuellen Ordner liegen.

### Ein Paket kann nicht installiert werden

Überprüfe deine Internetverbindung und stelle sicher, dass die virtuelle Umgebung aktiviert ist.

Führe anschließend erneut aus:

```powershell
python -m pip install -r requirements.txt
```

### Class Clash startet nicht

Wenn eine Fehlermeldung erscheint, notiere sie oder mache einen Screenshot.

Bei Problemen kannst du dich an den Entwickler wenden. Weitere Informationen zum Melden von Fehlern findest du in der README.md.

---

**Viel Spaß mit Class Clash!**