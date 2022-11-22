def eelarve(külalisi):
    summa = (10 * külalisi) + 55 
    return summa

failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")

kutsutud = 0
tuleb = 0

for rida in fail:
    nimed = rida.split()
    for sümbol in nimed:
        if sümbol == "+":
            tuleb += 1
        elif sümbol == "?":
            kutsutud += 1

fail.close()

kõik = kutsutud + tuleb

print("Kutsutud on " + str(kõik) + " inimest")
print(str(tuleb) + " inimest tuleb")

# kutsutud = int(input("Mitu inimest on kutsutud? "))
# tuleb = int(input("Mitu inimest on tuleb? "))

print("Maksimaalne eelarve:" , (eelarve(kõik)) , "eurot")
print("Minimaalne eelarve:" , (eelarve(tuleb)) , "eurot")

