from datetime import *

print("Sisestage failinimi:")
input = input()
fail= open(input, encoding="UTF-8")
kuupäev = datetime.now().day
nimed = []

for rida in fail:
    nimed.append(rida)

print("Vastama tuleb: " + nimed[kuupäev - 1])
    
fail.close()