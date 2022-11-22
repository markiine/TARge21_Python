from random import randint

istekoha_valik = input('Kas soovite istekoha ise valida ("ise") või loosida ("loos")? ')
if istekoha_valik == "ise":
    istekoha_soov = input('Kas soovite istuda akna ääres ("aken") või mitte ("muu")? ')
    if istekoha_soov == "aken":
        print("Valisite ise. Aknakoht.")
    else:
        print("Valisite ise. Vahekäigukoht.")
elif istekoha_valik == "loos":
    koht_aken = randint(1,3)
    if koht_aken == 1:
        print("Istekoht loositi. Aknakoht.")
    elif koht_aken != 1:
        print("Istekoht loositi. Vahekäigukoht.")

