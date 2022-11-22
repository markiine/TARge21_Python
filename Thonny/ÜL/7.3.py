from easygui import *  # faili toimimiseks peab olema easygui kaustas

arv1 = integerbox("Sisestage esimene täisarv lõigus 1-10:", lowerbound = 1, upperbound = 10)
arv2 = integerbox("Sisestage teine täisarv lõigus 1-10:", lowerbound = 1, upperbound = 10)

nupud = ["+","-","*"]
vajutati = buttonbox("Valige tehe ", choices = nupud)

if nupud == "+":
    tulemus = arv1 + arv2
elif nupud == "-":
    tulemus = arv1 - arv2
else:
    tulemus = arv1 * arv2

msgbox("Tehte tulemus on " + str(tulemus) + ".")