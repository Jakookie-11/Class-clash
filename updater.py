import os
import shutil
from urllib.request import urlopen
import zipfile
import subprocess
import sys


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
os.remove("update/main/updater.py")
shutil.rmtree("update/main/saves")
shutil.rmtree("update/main/.vscode")


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


for datei in os.listdir("update/main"):
    shutil.move(
        "update/main/" + datei,
        "."
    )


shutil.rmtree("update/")

subprocess.Popen([sys.executable, "main.py"])

sys.exit()