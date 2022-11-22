ringide_arv = int(input("Sisesta ringide arv (mittenegatiivne täisarv): "))

i = 2
summa = 0
for i in range(0, ringide_arv + 1, 2):
    summa += i
    
print("Porgandite koguarv on " + str(summa) + ".")