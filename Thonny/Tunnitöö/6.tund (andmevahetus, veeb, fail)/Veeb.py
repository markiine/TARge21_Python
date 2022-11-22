from urllib.request import urlopen
 
failVeebis = urlopen("https://courses.cs.ut.ee/2018/eprogalused/uploads/Main/mesipuu.txt")
baidid = failVeebis.read()  # kogu fail baitidena
tekst = baidid.decode()     # baitidest saab sõne
failVeebis.close()
print(tekst)

print()
print()

from urllib.request import urlopen
 
failVeebis = urlopen("https://courses.cs.ut.ee/2018/eprogalused/uploads/Main/mesipuu.txt")
baidid = failVeebis.read()
tekst = baidid.decode()            # baitidest saab sõne
ridadeKaupa = tekst.splitlines()   # sõne jaotatakse reavahetuse kohtadelt
failVeebis.close()
print(ridadeKaupa[4])

print()
print()

from urllib.request import urlopen

failVeebis = urlopen("http://www.cs.ut.ee")
baidid = failVeebis.read(121)  # 121 esimest
tekst = baidid.decode()        # baitidest saab sõne
print(tekst)
failVeebis.close()