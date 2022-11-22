ringide_arv = int(input("Sisesta ringide arv(mittenegatiivne täisarv): "))

i = 1
summa = 0
while i <= ringide_arv:
    summa += int(i * (i + 1) / 2)
    i += 1

print("Porgandite koguarv on " + str(summa) + ".")