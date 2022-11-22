def suurim_element(arvud):
    # alustuseks oletame, et esimene element on suurim
    seni_suurim = arvud[0]

    # hakkame järjendit läbi vaatama
    # kui leiame seni leitust veel suurema, siis uuendame muutuja väärtust
    for arv in arvud:
        if arv > seni_suurim:
            seni_suurim = arv

    # kui kõik arvud on läbi vaadatud, siis ongi abimuutujasse jäänud õige vastus
    return seni_suurim

# katsetame seda funktsiooni
# nagu näha, järjendit, nagu iga teist väärtust, saab anda argumendiks
s = suurim_element([8, 45, 12, 331, 123])

print("Suurim element on " + str(s))