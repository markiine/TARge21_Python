# Koosta programm, mis küsib kasutajalt nime ja vanust ja väljastab ekraanile nimelise tervituse koos tekstiga, mis ütleb, kas tegemist on 7-18-aastase inimesega.

nimi = input("Palun sisestage oma nimi: ")
vanus = float(input("Palun sisestage oma vanus: "))

if vanus >= 7 and vanus <= 18:
    print("Tere, " + nimi + "!")
else:
    print("Te ei ole 7-18-aastane!")