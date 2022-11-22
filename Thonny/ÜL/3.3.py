from random import randint

arv = int(input("Täringute arv: "))

i = 0
while i < arv:
    vise = randint(1,6)
    i += 1
    print(vise)
