from random import randint
elusid = 3
münte = 0
while elusid > 0:
    print("Jalutasid metsas ja nägid ", end = "") # ei vaheta rida
    kedaMida = randint(1, 3)
    if kedaMida == 1:
        print("seent", end = "") # ei vaheta rida
        if randint(1, 2) == 1:
            print(", mis kahjuks oli mürgiseen ja sa kaotasid ühe elu.")
            elusid -= 1
        else:
            print(", mis õnneks oli söögiseen ja sa said selle müügist ühe kuldmündi.")     
            münte += 1
    elif kedaMida == 2:
        print("karu", end = "") # ei vaheta rida
        if randint(1, 2) == 1:
            print(", kes kahjuks oli vihane ja sa kaotasid ühe elu.")
            elusid -= 1
        else:
            print(", kes õnneks oli rõõmus ja sa said temalt 5 kuldmünti.")     
            münte += 5
    else:
        print("kuldmünti ja said selle endale.")
        münte +=1
    print("Nüüd on sul " + str(elusid) + " elu ja " + str(münte) + " kuldmünti.")
    input("Jätkamiseks vajuta Enter-klahvi.")
print("Sellega on su seiklus kahjuks läbi.")