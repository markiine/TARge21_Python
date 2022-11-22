def lõimede_pikkus(lõpp_pikkus, lõimede_arv):
    kogupikkus = round(lõimede_arv * ((lõpp_pikkus) * 1.2 + 0.5), 2)
    return kogupikkus

failinimi = input("Sisestage failinimi: ")
pikad_lõimed = int(input("Sisestage 5-meetriste ja pikemate vaipade lõimede arv: "))
lühikesed_lõimed = int(input("Sisestage lühemate vaipade lõimede arv: "))


fail = open(failinimi, encoding="UTF-8")
lõimed = []
for rida in fail:
    rida = rida.strip()
    lõimed.append(float(rida))

fail.close()

summa = 0

for vaip in lõimed:
    if vaip < 5:
        pikkus = lõimede_pikkus(vaip, lühikesed_lõimed)
        print(pikkus)
        summa += pikkus
    else:
        pikkus = lõimede_pikkus(vaip, pikad_lõimed)
        print(pikkus)
        summa += pikkus

print("Kõigi vaipade peale läheb vaja " + str(round(summa, 2)) + " meetrit lõimeniiti.") 