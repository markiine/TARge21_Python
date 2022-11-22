def juurdekasv(metsatüki_pindala, aasta_juurdekasv):
    metsatüki_juurdekasv = round((metsatüki_pindala * float(0.4047) * aasta_juurdekasv), 2)
    return metsatüki_juurdekasv

failinimi = input("Sisestage failinimi: ")
aastane_kasv = float(input("Sisestage aastane juurdekasv hektari kohta tihumeetrites: "))
piir = float(input("Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võetakse: "))

fail = open(failinimi, encoding="UTF-8")
ridade_kaupa = []

for rida in fail:
    rida = rida.strip()
    ridade_kaupa.append(float(rida))
    
fail.close()
    
summa = 0

for pindala in ridade_kaupa:
    if float(pindala) > piir:
        aastane_juurdekasv = juurdekasv(pindala, aastane_kasv)
        print ("Metsatüki aastane juurdekasv on " + str(aastane_juurdekasv))
        summa += 1
    else:
        print("Metsatükki ei võeta arvesse")

print("Arvutati " + str(summa) + " metsatüki juurdekasv.")