from datetime import * 

fail = open("nimekiri.txt", encoding="UTF-8")
nimed = []

for rida in fail:
    nimed.append(rida)

failinimi = input("Sisestage failinimi: ")
kuupäev = int(datetime.now().day)

fail.close()

for i in range(32):
    if i == kuupäev:
        print("Vastama tuleb: " , nimed [i - 1])