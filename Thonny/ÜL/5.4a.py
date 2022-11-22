faili_nimi = input("Palun sisestage failinimi: ")
fail = open(faili_nimi,  encoding = "UTF-8")
i = 1
laulud = []

print("Muusikapala valik: ")

for rida in fail:
    laulud.append(str(rida))
    print(str(i) + ". " + (rida.strip()))
    i += 1

fail.close()

number = int(input("Valige laulu järjekorranumber: "))

positsioon = number - 1

print("Mängitav muusikapala on " + laulud[positsioon])

