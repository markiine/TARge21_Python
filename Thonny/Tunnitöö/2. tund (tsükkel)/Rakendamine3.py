sisestatud_pin = ""
katseid = 3
while sisestatud_pin != "1234" and katseid > 0:
   print("Sisesta PIN-kood:")
   print("Jäänud on " + str(katseid) + " katset.")
   katseid -= 1
   sisestatud_pin = input()
print("Sisenesid pangaautomaati!")