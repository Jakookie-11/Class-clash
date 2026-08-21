import faehigkeiten

#---Jakob---#
Jakob = {
    "Name      "   : "Jakob",
    "Level     "   : 1,
    "Klasse    "   : "Tank",
    "HP        "   : 200,
    "Schaden   "   : -10,
    "Faehigkeit 1" : faehigkeiten.einfacher_angriff 
}


#---Leo---#
Leo = {
    "Name      "   : "Leo",
    "Level     "   : 1,
    "Klasse    "   : "Angreifer",
    "HP        "   : 70,
    "Schaden   "   : -20,
    "Faehigkeit 1" : faehigkeiten.einfacher_angriff
}


#---Simon---#
Simon = {
    "Name      "   : "Simon",
    "Level     "   : 1,
    "Klasse    "   : "Unterstützer",
    "HP        "   : 110,
    "Schaden   "   : -10,
    "Faehigkeit 1" : faehigkeiten.einfacher_angriff,
    "Faehigkeit 2" : faehigkeiten.einfache_heilung
}

#---Max---#
Max = {
    "Name      "   : "Max",
    "Level     "   : 1,
    "Klasse    "   : "Tank",
    "HP        "   : 200,
    "Schaden   "   : -10,
    "Faehigkeit 1" : faehigkeiten.einfacher_angriff   
}



#----Charaktere----#
Charaktere = {
    "Jakob" : Jakob,
    "Leo"   : Leo,
    "Simon" : Simon,
    "Max"   : Max
}