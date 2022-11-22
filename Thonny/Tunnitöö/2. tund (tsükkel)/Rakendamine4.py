from time import sleep
sisestatud_pin = ""
katseid = 3
while sisestatud_pin != "1234" and katseid > 0:
   print("Sisesta PIN-kood:")
   print("Jäänud on " + str(katseid) + " katset.")
   katseid -= 1
   sisestatud_pin = input()
if sisestatud_pin == "1234":                      #if katseid > 0
   print("Sisenesid pangaautomaati!")
else:
   print("Katsete arv ületatud! Turvatöötaja kutsutakse 10 sekundi pärast!")
   i = 10
   while i > 0:
      print(i)
      i -= 1
      sleep(1)
   print("Turvatöötaja kutsutud!")