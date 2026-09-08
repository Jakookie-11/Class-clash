import os
import shutil


for datei in os.listdir("Class-clash/"):
    if datei.endswith(".py") and datei != "updater.py":
        os.remove("Class-clash/" + datei)
    elif datei.endswith(".txt"):
        os.remove("Class-clash/" + datei)
    elif datei.endswith(".json"):
        os.remove("Class-clash/" + datei)
    elif datei.endswith(".zib"):
        os.remove("Class-clash/" + datei)


shutil.rmtree("Class-clash/__pycache__")


for datei in os.listdir("Class-clash/update/Class-clash-Version-information-and-asking"):
    shutil.move(
        "Class-clash/update/Class-clash-Version-information-and-asking/" + datei,
        "Class-clash/"
    )


shutil.rmtree("Class-clash/update/")