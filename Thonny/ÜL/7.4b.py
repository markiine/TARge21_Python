from urllib.request import urlopen

kuu = input("Sisestage kuu: ")
päev = int(input("Sisestage päev: "))

failVeebis = urlopen("http://kodu.ut.ee/~eno/mooc/" + str(kuu))

baidid = failVeebis.read()
tekst = baidid.decode()
ridadeKaupa = tekst.splitlines()

failVeebis.close()

print("Kuupäeval " + str(päev) + ". " + kuu + " on nimepäevad järgmiste nimedega inimestel:\n" + ridadeKaupa[päev -1])