# >>> 4 6 8 10 Korrutis on 1920

algus = int(input("Sisestage esimene arv "))
lõpp = int(input("Sisestage teine arv "))
korrutis = 1
for i in range(algus, lõpp, 2):
    print(i)
    korrutis *= i
print("Korrutis on " + str(korrutis))