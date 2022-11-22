from datetime import * 

failinimi = input("Sisestage failinimi: ")
nimed = []
with open(failinimi, encoding="UTF-8") as fail:
    for rida in fail:
        nimed.append(rida.rstrip("\n"))

kuupäev = int(datetime.now().day)        
print("Vastama tuleb: " , nimed [kuupäev - 1])

