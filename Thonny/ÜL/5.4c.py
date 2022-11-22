from datetime import * 

fail = open("nimekiri.txt", encoding="UTF-8")
nimed = []

for rida in fail:
    nimed.append(rida)

failinimi = input("Sisestage failinimi: ")
kuupäev = int(datetime.now().day)
positsioon = kuupäev - 1

fail.close()

print("Vastama tuleb: " , nimed [positsioon])