nimi = input("Palun sisesta oma nimi: ")
vanus = input("vanus: ")
aadress = input("aadress: ")
 
f = open("andmed3.txt", "w")
f.write(nimi + "\n")
f.write(vanus + "\n")
f.write(aadress + "\n")
f.close()

print()

doonorNimi = input("Mis failist info võtta? ")
aktseptorNimi = input("Millisesse faili info pannakse? ")
doonorFail = open(doonorNimi, encoding="UTF-8")
aktseptorFail = open(aktseptorNimi, "w")
for rida in doonorFail:
    aktseptorFail.write(rida.upper())
doonorFail.close()
aktseptorFail.close()