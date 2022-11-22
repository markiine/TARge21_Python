faili_nimi = input("Palun sisestage failinimi: ")
fail = open(faili_nimi,  encoding = "UTF-8")

laulud = []

for rida in fail:
    laulud.append(str(rida.strip("\n")))

fail.close()

mitu_laulu = len(laulud)

print("Muusikapala valik: ")

for i in range(mitu_laulu):
    print(str(i + 1) + ". " + (laulud[i]))

print()

mitmes_laul = int(input("Valige laulu järjekorranumber: "))

positsioon = mitmes_laul - 1

print("Mängitav muusikapala on " + laulud[positsioon])

