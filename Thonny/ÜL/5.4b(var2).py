sisse_fail = open("sisseränne.txt", encoding="UTF-8")
sisse = []

välja_fail = open("väljaränne.txt", encoding="UTF-8")
välja = []

for rida_sisse in sisse_fail:
    sisse.append(float(rida_sisse))
    
for rida_välja in välja_fail:
    välja.append(float(rida_välja))

sisse_fail.close()
välja_fail.close()

saldo = []

for i in range(len(sisse)):
    saldo.append(sisse[i] - välja[i])
print(saldo)

suurim_saldo = max(saldo)

if suurim_saldo < 0:
    print("Positiivse rändesaldoga aastaid ei ole.")
else:
    print("Suurim positiivne rändesaldo oli " , str(saldo.index(suurim_saldo) + 1) , ". aastal.")
    