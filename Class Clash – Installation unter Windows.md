# Class Clash – Installation unter Windows

## 1. Vorraussetzungen

Class Clash läuft auf Windows 64-Bit und benötigt **Python 3.15 (64-Bit)**. Die mitgelieferte native Erweiterung `geheimes.cp315-win_amd64.pyd` ist speziell auf diese Version und das Betriebssystem abgestimmt.

> Hinweis: Für Nutzerinnen und Nutzer, die Markdown-Dateien nicht bequem lesen können, gibt es im Projektordner auch PDF-Versionen: `README.pdf`, `More info.pdf` und `Class Clash – Installation unter Windows.pdf`.

Wenn du ein anderes Python-Setup verwendest, kann das Spiel nicht korrekt starten.

---

## 2. Python 3.15 (64-Bit) installieren

### 2.1 Python herunterladen

1. Öffne die offizielle Python-Downloadseite: [Python für Windows herunterladen](https://www.python.org/downloads/release/python-3150/)
2. Wähle den **Windows Installer (64-bit)** für Python 3.15.
3. Lade die Datei herunter und öffne sie.

### 2.2 Installation durchführen

Im Installationsfenster:

1. Aktiviere **„Add python.exe to PATH“**, falls diese Option sichtbar ist.
2. Klicke auf **„Install Now“**.
3. Warte, bis die Installation abgeschlossen ist.

### 2.3 Prüfen, ob Python korrekt installiert ist

Öffne PowerShell und gib ein:

```powershell
py -3.15 --version
```

Erwartete Ausgabe:

```text
Python 3.15.x
```

Wenn die Version angezeigt wird, ist Python korrekt installiert.

Wenn nicht, prüfe:

```powershell
python --version
```

Falls auch das nicht funktioniert, ist Python nicht richtig im Pfad eingebunden. Dann bitte neu installieren und „Add python.exe to PATH“ aktivieren.

---

## 3. Class Clash herunterladen und entpacken

1. Lade das Projekt als ZIP oder über GitHub herunter.
2. Entpacke es in einen Ordner deiner Wahl.
3. Öffne diesen Ordner.

Wichtig: In diesem Ordner müssen die Dateien `main.py`, `requirements.txt` und die restlichen Projektdateien liegen.

---

## 4. PowerShell im richtigen Ordner öffnen

Du kannst PowerShell direkt im Projektordner öffnen:

1. Öffne den Class-Clash-Ordner im Datei-Explorer.
2. Klicke oben in die Adressleiste.
3. Schreibe dort `powershell` oder `cmd` und drücke **Enter**.

Damit öffnet sich die Konsole direkt im richtigen Ordner.

---

## 5. Abhängigkeiten installieren

Im geöffneten PowerShell-Fenster gib ein:

```powershell
python -m pip install -r requirements.txt
```

Oder falls du Python 3.15 explizit verwenden willst:

```powershell
py -3.15 -m pip install -r requirements.txt
```

Das installiert die benötigten Pakete aus `requirements.txt`.

> Hinweis: Eine aktive Internetverbindung ist erforderlich, damit die Pakete heruntergeladen werden können.

Falls du eine virtuelle Umgebung nutzen möchtest, kannst du diese vorab erstellen:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

---

## 6. Class Clash starten

Wenn die Installation abgeschlossen ist, starte das Spiel mit:

```powershell
python main.py
```

Oder mit expliziter Python-3.15-Version:

```powershell
py -3.15 main.py
```

Beim ersten Start prüft Class Clash automatisch, ob die Umgebung kompatibel ist. Fehlende Pakete aus `requirements.txt` können dabei ebenfalls automatisch installiert werden, sofern Internet verfügbar ist.

---

## 7. Beim späteren Start

Wenn du das Spiel erneut starten möchtest, brauchst du die Pakete meistens nicht erneut zu installieren.

1. Öffne den Projektordner.
2. Öffne PowerShell im Ordner.
3. Aktiviere die virtuelle Umgebung, falls du eine benutzt hast:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Starte das Spiel:

```powershell
python main.py
```

---

## 8. Python aktualisieren oder neu installieren

Wenn beim Start von Class Clash eine Meldung wie diese erscheint:

```text
Class Clash benötigt CPython 3.15 (64-Bit) für geheimes.cp315-win_amd64.pyd.
Verwendet wird Python X.Y.Z.
```

Dann ist genau die falsche Python-Version aktiv. Das Spiel verlangt **CPython 3.15 64-Bit**.

### 8.1 Wie du prüfst, welche Python-Version du gerade nutzt

In PowerShell gib ein:

```powershell
python --version
```

oder

```powershell
py -3.15 --version
```

Wenn `py -3.15 --version` funktioniert, dann liegt Python 3.15 auf dem System vor.

Wenn nur `python --version` eine andere Version zeigt, dann wird im Moment ein falsches Python verwendet.

---

### 8.2 Python 3.15 64-Bit sauber installieren

1. Öffne die offizielle Python-Downloadseite:
   [Python 3.15 für Windows](https://www.python.org/downloads/release/python-3150/)
2. Lade den **Windows installer (64-bit)** herunter.
3. Installiere Python erneut.
4. Achte dabei unbedingt auf:
   - **Add python.exe to PATH**
   - **Install for all users** oder **Install just for me**
5. Nach der Installation prüfe erneut:

```powershell
py -3.15 --version
```

Wenn dort `Python 3.15.x` erscheint, ist die richtige Version installiert.

---

### 8.3 Python komplett neu installieren (falls das Update nicht sauber wirkt)

Wenn die alte Installation kaputt oder veraltet ist, installiere Python neu:

1. Öffne **Systemsteuerung > Programme > Programme und Funktionen**.
2. Suche nach **Python**.
3. Wähle Python aus und klicke auf **Deinstallieren**.
4. Danach erneut die offizielle 3.15 64-Bit-Version installieren.
5. Danach in PowerShell prüfen:

```powershell
py -3.15 --version
```

Wenn diese Prüfung funktioniert, kann Class Clash normal gestartet werden.

---

### 8.4 Wenn `python` trotzdem auf die falsche Version zeigt

Manchmal bleibt in der Konsole eine alte Python-Umgebung aktiv oder ein anderer Python-Link wird bevorzugt.

Prüfe:

```powershell
where python
where py
```

Wenn mehrere Versionen auftauchen, nutze dort gezielt:

```powershell
py -3.15 main.py
```

Das startet Class Clash mit der richtigen Python-Version, auch wenn `python` standardmäßig etwas anderes verwendet.

---

### 8.5 Virtual Environment neu aufsetzen

Wenn du bereits eine `.venv` benutzt hast, kann es sinnvoll sein, sie neu zu erstellen:

```powershell
cd "C:\Pfad\zum\Class-clash-Ordner"
rmdir /S /Q .venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Danach:

```powershell
python main.py
```

---

### 8.6 `Python` bzw. `py` wird nicht erkannt

Prüfe, ob Python installiert ist:

```powershell
python --version
```

oder

```powershell
py -3.15 --version
```

Wenn beides fehlschlägt, ist Python nicht korrekt installiert oder nicht im Pfad gesetzt.

Lösung:

- Python 3.15 erneut installieren
- beim Installieren **„Add python.exe to PATH“** aktivieren
- Neustart des Computers oder der PowerShell

---

### 8.2 `requirements.txt` wurde nicht gefunden

Das passiert meistens, wenn PowerShell nicht im richtigen Ordner offen ist.

Prüfe mit:

```powershell
Get-ChildItem
```

Du solltest dort die Datei `requirements.txt` sehen.

Wenn nicht, wechsle in den richtigen Projektordner.

---

### 8.3 Paketinstallation schlägt fehl

Mögliche Ursachen:

- keine Internetverbindung
- Proxy/Einschränkungen im Netzwerk
- Python-Version nicht kompatibel
- virtualenv nicht aktiviert

Lösung:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Falls der Fehler weiter besteht, prüfe die Fehlermeldung und notiere sie genau.

---

### 8.4 Das Spiel startet nicht oder stürzt direkt ab

Das Spiel befindet sich noch in der Beta-Phase. Fehler können auftreten.

Wenn es abstürzt:

1. Notiere die angezeigte Fehlermeldung oder Fehler-ID.
2. Suche im Ordner `crash_logs/` nach der erzeugten Datei.
3. Mache einen Screenshot, wenn möglich.
4. Melde den Fehler im GitHub-Issue mit kurzer Beschreibung des Problems.

Das Spiel erzeugt automatisch Fehlerberichte, damit der Fehler nachvollziehbar bleibt.

---

### 8.5 Fehlermeldung zur Python-Version oder Erweiterung

Wenn die Meldung ungefähr so aussieht:

- „Python-Version nicht kompatibel“
- „Native Erweiterung fehlt“
- „cp315-win_amd64.pyd konnte nicht geladen werden“

Dann ist die Ursache in den meisten Fällen:

- falsche Python-Version
- falsche Bit-Version (32-Bit statt 64-Bit)
- fehlende oder falsch platzierte Erweiterungsdatei

Lösung:

- nur Python 3.15 64-Bit verwenden
- Projektordner prüfen
- sicherstellen, dass `geheimes.cp315-win_amd64.pyd` im richtigen Verzeichnis liegt
- Spiel neu starten

---

### 8.6 Das Spiel zeigt merkwürdige Fehler im Verlauf

Class Clash ist noch in Entwicklung. Einige Bereiche können noch unvollständig, instabil oder ausbalanciert sein.

Wenn du ein Problem findest:

- nutze die Crash-Datei
- notiere deinen Ablauf
- prüfe, ob das Problem mit einem bestimmten Menü, Kampf oder einer Kampagne zusammenhängt
- melde es sauber, damit es behoben werden kann

---

## 9. Wichtig zu wissen

- Das Spiel ist in der Beta-Phase
- Fehler sind möglich
- manche Inhalte sind noch provisorisch
- du solltest regelmäßige Sicherungen deiner Spielstände machen
- lokale Daten liegen in `saves/`
- Fehlerberichte liegen in `crash_logs/`

---

## 10. Viel Spaß

Wenn alles korrekt installiert ist, kannst du Class Clash mit

```powershell
python main.py
```

starten.

Wenn du Probleme hast, prüfe zuerst die oben genannten Punkte. Wenn der Fehler weiterhin besteht, melde ihn bitte mit der Fehler-ID und dem Log.

**Viel Spaß mit Class Clash!**