# Koosta mäng, kus saate ära arvata arvuti poolt mõeldud täisarvu ühest kahekümneni. nt:

# Mõtlesin ühele täisarvule 1-20ni. Mis arv see on?
# >> 15
# Liiga suur, proovi uuesti.
# >> 7
#Liiga väike, proovi uuesti.
# >> 9
# Liiga väike, proovi uuesti.
# >> 11
# Tubli, arvasid ära. Arv oli 11.
# Enne ülesande lahendamist mõelge välja mängu algoritm ja koostage selle kohta plokkskeem.

from random import randint

juhuslik_arv = randint(1,20)

while True:
    arvatud_arv = int(input("Sisesta täisarv 1-20: "))
    if arvatud_arv == juhuslik_arv:
        print("VÕITSID!")
        break
    elif arvatud_arv > juhuslik_arv:
        print("Liiga suur, proovi uuesti!")
    else:
        print("Liiga väike, proovi uuesti!")