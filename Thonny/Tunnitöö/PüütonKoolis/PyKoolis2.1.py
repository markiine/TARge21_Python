# Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku ümbermõõdu ja pindala.

pikkus = int(input("Palun sisestage ristküliku pikkus: "))
laius = int(input("Palun sisestage ristküliku laius: "))

ümbermõõt = 2 * (pikkus + laius)
pindala = pikkus * laius

print("Ristküliku ümbermõõt on " + str(ümbermõõt) + " ja pindala on " + str(pindala) + ".")
