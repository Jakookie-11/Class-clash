import os
import shutil
from urllib.request import urlopen
import zipfile
import confic
import sys
import time


os.makedirs("update", exist_ok=True)
url = "https://raw.githubusercontent.com/Jakookie-11/Class-clash/main/update.zip"

antwort = urlopen(url)
inhalt = antwort.read()

datei = open("update/update.zip", "wb")
datei.write(inhalt)
datei.close()

datei = zipfile.ZipFile("update/update.zip", "r")
datei.extractall("update")
datei.close()

os.remove("update/update.zip")
os.remove("update/Class-clash-main/updater.py")
shutil.rmtree("update/Class-clash-main/saves")
shutil.rmtree("update/Class-clash-main/.vscode")


for datei in os.listdir("."):
    if datei.endswith(".py") and datei != "updater.py":
        os.remove(datei)
    elif datei.endswith(".txt"):
        os.remove(datei)
    elif datei.endswith(".json"):
        os.remove(datei)
    elif datei.endswith(".zip"):
        os.remove(datei)


shutil.rmtree("__pycache__")


for datei in os.listdir("update/Class-clash-main"):
    shutil.move(
        "update/Class-clash-main/" + datei,
        "."
    )


shutil.rmtree("update/")

os.system(confic.terminal_clear)
print("UPDATER FERTIG")

time.sleep(2)

sys.exit()