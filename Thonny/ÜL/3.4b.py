from random import randint

pöialpoisid = int(input("Mitu pöialpoissi tahab õunu? "))
õunu_kokku = 14
i = 0
summa = 0

while i < pöialpoisid:
    õunad = randint(1,2)
    summa += õunad
    i += 1
    print(õunad)
alles_õunu = õunu_kokku - summa
    
print("Lumivalgekesele jäi " + str(alles_õunu) + ".")