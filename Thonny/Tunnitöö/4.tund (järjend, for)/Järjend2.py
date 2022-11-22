# järjendi loomine
nädalapäevad = ["esmaspäev", "teisipäev", "kolmapäev", "neljapäev", "reede", "laupäev", "pühapäev"]
# järjendi ekraanile väljastamine
print(nädalapäevad)
# elementide arvu (järjendi pikkuse) leidmine
nädalapäevi = len(nädalapäevad)
print('Järjendis on ' + str(nädalapäevi) + ' elementi')
# järjendisse kuulumise kontroll
if "palgapäev" in nädalapäevad:
    print("Palgapäev on järjendis")
else:
    print("Palgapäev ei ole järjendis")
# konkreetse elemendi väärtus indeksi (järjekorranr) abil
print(nädalapäevad[1])
print(nädalapäevad[0])
print(nädalapäevad[6])
print(nädalapäevad[-1])

print()

linn = "Tartu"
print(linn[2])

print ()

print(nädalapäevad[1][1])