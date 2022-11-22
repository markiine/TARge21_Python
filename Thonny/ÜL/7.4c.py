#argument s on sõne, esialgu see on kuupäev, edasi juba arvutatud arv
def elutee(s):
    #abimuutaja numbri arvutamiseks
    n = 0
    # tsükkel, mis vaatab iga sümboli sõnes
    for i in s:
        if i != ".":
            n += int(i) # arvutame summat
    # kui saadud arv on väiksem kui 10, siis ongi elutee number käes
    if n < 10:
        return n
    # kui saadud arv on 10 või suurem, siis on vaja uuesti arvutada,
    #selleks kasutame jälle sama funktsiooni
    else:
        return elutee(str(n))

file = open("sunnikuupaevad.txt", encoding="UTF-8") #.read().splitlines()
ridadeKaupa = []
for rida in file:
    rida = rida.strip()
    ridadeKaupa.append(rida)

for i in range(len(ridadeKaupa)):
    eluteenumber = elutee(ridadeKaupa[i])
    for number in range(1,10):
        file = open("eluteenumber" + str(number) + ".txt", "a")
        if int(eluteenumber) == number:
            file.write(ridadeKaupa[i] + "\n")