#rühmaliikmed: Anni Maasik, Eve Köse, Dagne Markiine Kotkas

#Mäng lasteaia ja esimese klassi lastele geomeetriliste kujundite õppimiseks.
#Programm kuvab ekraanile lihtsamad geomeetrilised kujundid ükshaaval
#ja annab mängijale 4 varianti, mille vahel valida.
#õige vastuse puhul ütleb ÕIGE!, vale vastuse puhul, teavitab valest vastusest.
#Programm küsib ka kasutajanime ja arvutab õigesti vastatud kordade skoori,
#mille kohta mängu lõppedes annab tagasiside. Peale seda küsib, et kas kasutaja
#soovib mängida uuesti, millele eeldatakse vastust 'jah' või 'ei.
#Vastates 'jah', algab mäng automaatselt uuesti, vastates 'ei', lõppeb mäng ja
#kasutajale soovitakse head aega!
#kujundid: ring, ruut, ristkülik, kolmnurk


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
        msgbox("ÕIGE! ")
        skoor += 1
    else:
        msgbox("VALE!")
    image = "ristkülik.png"
    msg = "MIS KUJUND ON PILDIL?"
    choices = ["KOLMNURK","RUUT","RING","RISTKÜLIK"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply =="RISTKÜLIK":
        msgbox("ÕIGE! ")
        skoor += 1
    else:
        msgbox("VALE!")

    image = "ruut.png"
    msg = "MIS KUJUND ON PILDIL?"
    choices = ["KOLMNURK","RUUT","RING","RISTKÜLIK"]
    reply = buttonbox(msg, image=image, choices=choices)

    if reply == "RUUT":
        msgbox("ÕIGE! ")
        skoor += 1
    else:
        msgbox("VALE!")

    image = "ring.png"
    msg = "MIS KUJUND ON PILDIL?"
    choices = ["KOLMNURK","RUUT","RING","RISTKÜLIK"]
    reply = buttonbox(msg, image=image, choices=choices)

    if reply == "RING":
        msgbox("ÕIGE! ")
        skoor += 1
    else:
        msgbox("VALE!")

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
