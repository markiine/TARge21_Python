from easygui import *

#def arvuta_punktid():
    #siia vaja mõelda siis arvutamise funktsioon

kasutajanimi=input("Sisesta kasutajanimi: ")

image = "kolmnurk.jpg"
msg = "MIS KUJUND ON PILDIL?"
choices = ["KOLMNURK","RUUT","RING","RISTKÜLIK"]
reply = buttonbox(msg, image=image, choices=choices)
if reply =="KOLMNURK":
    msgbox("Valisid õigesti " + reply + "!")
else:
    msgbox("Vale astus! Sa pakkusid " + reply + "!")

image = "ristkülik.png"
msg = "MIS KUJUND ON PILDIL?"
choices = ["KOLMNURK","RUUT","RING","RISTKÜLIK"]
reply = buttonbox(msg, image=image, choices=choices)
if reply =="RISTKÜLIK":
    msgbox("Valisid õigesti " + reply + "!")
else:
    msgbox("Vale astus! Sa pakkusid " + reply + "!")

image = "ruut.png"
msg = "MIS KUJUND ON PILDIL?"
choices = ["KOLMNURK","RUUT","RING","RISTKÜLIK"]
reply = buttonbox(msg, image=image, choices=choices)

if reply =="RUUT":
    msgbox("Valisid õigesti " + reply + "!")
else:
    msgbox("Vale astus! Sa pakkusid " + reply + "!")

image = "ring.png"
msg = "MIS KUJUND ON PILDIL?"
choices = ["KOLMNURK","RUUT","RING","RISTKÜLIK"]
reply = buttonbox(msg, image=image, choices=choices)

if reply =="RING":
    msgbox("Valisid õigesti " + reply + "!")
else:
    msgbox("Vale astus! Sa pakkusid " + reply + "!")

skoor= 1
print("Olid tubli mängija",kasutajanimi,", sinu punktisumma on", skoor)