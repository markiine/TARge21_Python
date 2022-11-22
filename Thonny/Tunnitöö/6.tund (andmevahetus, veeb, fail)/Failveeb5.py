failist = open("arvud.txt")
summa = 0
for rida in failist:
    summa = summa + int(rida)
print(summa)

print()

failist = open("arvud.txt")
summa = 0
for rida in failist:
    summa = summa + rida
print(summa)

# Suurusi summa (tüüp int) ja rida (tüüp str) ei saa omavahel liita.