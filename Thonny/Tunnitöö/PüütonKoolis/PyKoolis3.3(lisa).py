
from random import randint

print("Tere! Õpime arvutama, esitan 10 liitmistehet, püüa vastata õigesti. ")

õigeid = 0
tehteid = int(input("Mitu tehet soovid teha? "))
min_arv = int(input("Milline on väikseim arv? "))
max_arv = int(input("Milline on suurim arv? "))

for i in range(tehteid):
    arv1 = randint(min_arv , max_arv)
    arv2 = randint(min_arv , max_arv)
    vastus = int(input(str(arv1) + "+" + str(arv2) + "="))
    if vastus == arv1 + arv2:
        print("Tubli!")
        õigeid += 1
    else:
        print("See läks mööda. Pinguta rohkem.")
        
print("Tehteid oli " , tehteid , "Vastasid õigesti", õigeid, "korda.")




