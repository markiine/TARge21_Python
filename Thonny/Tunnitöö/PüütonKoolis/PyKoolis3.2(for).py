# Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa. Täienda seda programmi nii, et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta, vaid vajutab lihtsalt sisestusklahvi. Proovige seda ülesannet lahendada nii while- kui for-tsükliga.

summa = 0
for i in range(10):
    arv = int(input("Sisestage " + str(i + 1) + ". täisarv: "))
    summa += arv
    # summa = summa + arv
print("Sisestatud arvude summa on: " , summa)