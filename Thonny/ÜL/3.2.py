ringide_arv = int(input("Sisesta ringide arv(mittenegatiivne täisarv): "))

i = 2
summa = 0
while i <= ringide_arv:
    summa = summa + i
    i = i + 2
    
print("Porgandite koguarv on " + str(summa) + ".")