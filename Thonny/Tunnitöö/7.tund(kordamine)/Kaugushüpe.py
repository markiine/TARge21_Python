def parandatud_tulemus(vigane_tulemus, parandus):
    tegelik_tulemus = vigane_tulemus + mõõteparandus / 100
    return tegelik_tulemus

failinimi = input("Sisestage failinimi: ")
mõõteparandus = int(input("Sisestage parandus sentimeetrites: "))
normatiiv = float(input("Sisestage meistrivõistluste normatiiv meetrites: "))

vigased_tulemused = []

fail = open(failinimi, encoding="UTF-8")
for rida in fail:
    vigased_tulemused += [float(rida)]
    
tegelikud_tulemused = []
print("Tegelikud tulemused")

for tulemus in vigased_tulemused:
    tegelik_tulemus = parandatud_tulemus(tulemus, mõõteparandus)
    print(round(tegelik_tulemus, 2))
    tegelikud_tulemused += [tegelik_tulemus]
    
arv = 0
summa = 0

for tulemus in tegelikud_tulemused:
    if tulemus >= normatiiv:
        arv += 1
        summa += tulemus
        
print("Normatiivi täitis " + str(arv) + ".")
if arv > 0:
    print("Täitnute keskmine on " + str(round(summa/arv, 2)) + ".")