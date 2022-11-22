from easygui import * # järjendiga
 
variandid = ["minu lemmik","lihtne","ok","keeruline"]
vajutati = choicebox("Programmeerimine on ", choices = variandid)
if vajutati == None:
    msgbox("Te ei valinud midagi!")
elif vajutati == "minu lemmik":
    msgbox("Programmeerimine on teie lemmik! Muidugi nii peakski olema!")
else:
    msgbox("Te arvate, et programmeerimine on " + vajutati + ", hmm, väga huvitav!")
    
print()

from easygui import * # andmete küsimine
 
nimi = enterbox("Tere, kuidas on teie nimi?")
vanus = integerbox("Kui vana te olete?", lowerbound = 1, upperbound = 120)
if nimi == None or vanus == None or nimi == "":
    msgbox("Palun sisestage andmed korrektselt!")
else:
    msgbox("Tere, " + str(vanus)  + "-aastane " + nimi + "!")