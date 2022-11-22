# Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa. Täienda seda programmi nii, et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta, vaid vajutab lihtsalt sisestusklahvi. Proovige seda ülesannet lahendada nii while- kui for-tsükliga.

summa = 0
while True:
    sisestus = input("Sisestage täisarv: ")
    if sisestus == "":
        break
    arv = int(sisestus)
    summa += arv
print("Sisestatud arvude summa on: " , summa)