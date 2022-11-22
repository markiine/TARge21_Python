from easygui import*

def anna_tagasisidet(arv):
    if arv == 4:
        return("Suurepärane, Sa vastasid kõik vastused õigesti!")
    elif arv == 3:
        return("Sa olid tubli, ainult 1 vale vastus.")
    elif arv == 2:
        return("Sa vastasid pooled õigesti.")
    elif arv == 1:
        return("Sul oli 1 õige vastus, aga harjutamine teeb meistriks.")
    elif arv == 0:
        return("Proovi veel, 0 õiget vastust.")
    
kasutajanimi = enterbox("Tere! Palun sisesta oma nimi!")

while True:
    skoor = 0
    image = "kolmnurk.jpg"
    msg = "MIS KUJUND ON PILDIL?"
    choices = ["KOLMNURK","RUUT","RING","RISTKÜLIK"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply =="KOLMNURK":
        msgbox("Õige vastus! " + "See on tõesti " + reply + "!")
        skoor += 1
    else:
        msgbox("Vale vastus! Sa pakkusid " + reply + "!")
    image = "ristkülik.png"
    msg = "MIS KUJUND ON PILDIL?"
    choices = ["KOLMNURK","RUUT","RING","RISTKÜLIK"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply =="RISTKÜLIK":
        msgbox("Õige vastus! " + "See on tõesti " + reply + "!")
        skoor += 1
    else:
        msgbox("Vale vastus! Sa pakkusid " + reply + "!")

    image = "ruut.png"
    msg = "MIS KUJUND ON PILDIL?"
    choices = ["KOLMNURK","RUUT","RING","RISTKÜLIK"]
    reply = buttonbox(msg, image=image, choices=choices)

    if reply == "RUUT":
        msgbox("Õige vastus! " + "See on tõesti " + reply + "!")
        skoor += 1
    else:
        msgbox("Vale vastus! Sa pakkusid " + reply + "!")

    image = "ring.png"
    msg = "MIS KUJUND ON PILDIL?"
    choices = ["KOLMNURK","RUUT","RING","RISTKÜLIK"]
    reply = buttonbox(msg, image=image, choices=choices)

    if reply == "RING":
        msgbox("Õige vastus! " + "See on tõesti " + reply + "!")
        skoor += 1
    else:
        msgbox("Vale vastus! Sa pakkusid " + reply + "!")

    väljund = msgbox("Olid tubli mängija, " + kasutajanimi + "!")
    tagasiside = msgbox(anna_tagasisidet(skoor))
    while True:
        vastus = enterbox("Kas soovid uuesti mängida? 'jah'või'ei' ")
        if vastus in("jah","ei"):
            break
        print("Error!")
        
    if vastus == "jah":
        continue
    else :
        msgbox("Head aega!")
        break
