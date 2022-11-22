from easygui import *  # faili kirjutamine koos salvestamise aknaga
 
nimi = enterbox("Palun sisesta oma nimi: ")
vanus = integerbox("Palun sisesta oma vanus: ", lowerbound = 1, upperbound = 120)
aadress = enterbox("Palun sisesta oma aadress: ")
 
failinimi = filesavebox()
 
f = open(failinimi, "w")
f.write(nimi + "\n")
f.write(str(vanus) + "\n")
f.write(aadress + "\n")
f.close()

print()

from easygui import *  # failist lugemine koos faili valimise aknaga
 
failinimi = fileopenbox()
 
f = open(failinimi)
 
nimi = f.readline().strip()
vanus = f.readline().strip()
aadress = f.readline().strip()
 
f.close()
 
tekst = "Nimi: " + nimi + "\n"+ "Vanus: " + vanus + " aastat\n" + "Aadress: " + aadress
 
msgbox(tekst)