täisarv = int(input("Sisestage täisarv: "))

i = 0
summa = 0
while i < täisarv:
    summa = int(2 ** i)
    i += 1


print("Nisuteri " + str(täisarv) + "." + " ruudu eest: " + str(summa))
