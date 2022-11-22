f = open("andmed2.txt", encoding="UTF-8")
 
nimi = f.readline().strip() # ilma .strip lisab vaba rea print tõttu
vanus = f.readline().strip()
aadress = f.readline()
 
print("Nimi:", nimi)
print("Vanus:", vanus, "aastat")
print("Aadress:", aadress)
 
f.close()

print()

f = open("andmed2.txt", encoding="UTF-8")
loetud = f.readlines()
f.close() # faili ei lähe enam vaja
print(loetud)

print()

f = open("andmed2.txt", encoding="UTF-8")
loetud = f.read()
f.close() # faili ei lähe enam vaja
print(loetud)

print()

f = open("andmed2.txt", encoding="UTF-8")
loetud = f.read(5)
f.close() # faili ei lähe enam vaja
print(loetud)
