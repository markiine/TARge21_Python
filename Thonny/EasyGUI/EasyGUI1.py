# Moodul EasyGUI ei ole osa Pythoniga vaikimisi kaasas olevatest moodulitest, seetõttu tuleb see esmalt
# paigaldada. Mooduli kasutamiseks tuleb programmiga samasse kausta paigutada fail easygui.py.

from easygui import *                              # EasyGui kasutamiseks importida
 
msgbox("Minu esimene graafiline kasutajaliides!!") # teateaken

print()

from easygui import *
 
nupud = ["lihtne","ok","keeruline"]
vajutati = buttonbox("Programmeerimine on ", choices = nupud)
msgbox("Te arvate, et programmeerimine on " + vajutati + "!")
