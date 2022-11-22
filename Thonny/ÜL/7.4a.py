def eelarve(külalisi):
    summa = (10 * külalisi) + 55 
    return summa

failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")
tekst = fail.read()
ridadeKaupa = tekst.splitlines()

fail.close()

print("Kutsutud on " + str(len(ridadeKaupa)) + " inimest")
loendur = 0
for rida in ridadeKaupa:
    if rida [0] == "+":
        loendur += 1
print(str(loendur) + " inimest tuleb")

# kutsutud = int(input("Mitu inimest on kutsutud? "))
# tuleb = int(input("Mitu inimest on tuleb? "))

kutsutud = len(ridadeKaupa)
tuleb = loendur

print("Maksimaalne eelarve:" , (eelarve(kutsutud)) , "eurot")
print("Minimaalne eelarve:" , (eelarve(tuleb)) , "eurot")
