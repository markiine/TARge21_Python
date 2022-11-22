# Täienda eelmist programmi selliselt, et kasutajal oleks arvu arvamiseks 5 korda, s. t. kui viie korra jooksul ära ei arvata, ütleb arvuti, et kaotasid, ning teatab õige arvu. Täienda vastavalt ka plokkskeemi.

from random import randint

juhuslik_arv = randint(1,20)
arvamisi = 0

while True:
    arvatud_arv = int(input("Sisesta täisarv 1-20: "))
    arvamisi += 1
    if arvatud_arv == juhuslik_arv:
        print("VÕITSID!")
        break
    elif arvamisi == 5:
        print("KAOTASID! Õige arv oli: " , juhuslik_arv)
        break
    elif arvatud_arv > juhuslik_arv:
        print("Liiga suur, proovi uuesti!")
    else:
        print("Liiga väike, proovi uuesti!")