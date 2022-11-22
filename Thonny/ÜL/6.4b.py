def pronksikarva_summa(arv):
    summa = 0
    for rida in arv:
        if rida < 10:
            summa += rida
    return summa
        
faili_nimi = input("Sisesta failinimi: ")
fail = open(faili_nimi,  encoding = "UTF-8")

pronks = []

for rida in fail:
    pronks.append(int(rida))

fail.close()

print("Hoiupõrsasse läheb " , str(pronksikarva_summa(pronks)) , " senti.")