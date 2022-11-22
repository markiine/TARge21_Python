# Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse kraadides ja väljastab tulemuse Fahrenheiti kraadides. Kuidas muuta programmi nii, et võimalik oleks teisendamine nii üht- kui teistpidi?

tempC = int(input("Palun sisestage temperatuur(°C) : "))
muudeCtoF = round((tempC * 1.8) + 32)

print("Temperatuur on: " , muudeCtoF , "°F")
