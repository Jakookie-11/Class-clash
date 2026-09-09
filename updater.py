import os
import shutil


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


for datei in os.listdir("update/Class-clash-Version-information-and-asking"):
    shutil.move(
        "update/Class-clash-Version-information-and-asking/" + datei,
        "."
    )


shutil.rmtree("update/")