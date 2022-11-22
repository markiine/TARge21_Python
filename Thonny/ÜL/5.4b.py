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

for i in range(10):
    rändesaldo = sisse[i] - välja[i]
    saldo.append(int(rändesaldo))
print(saldo)

max_num = max(saldo)
# print(max_num)

if max_num > 0:
    indeks = saldo.index(max_num) + 1
    print("Suurim positiivne rändesaldo oli " , str(indeks) , ". aastal.")
else:
    print("Positiivse rändesaldoga aastaid ei ole.")
