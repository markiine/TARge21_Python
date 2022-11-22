# Eelmise ülesande alusel koostage programm M-Koer (Matemaatiline Koer), millele antakse samuti ette kaks arvu ja tehtemärk, kuid vastus ei kirjutata mitte arvulisel kujul, vaid esitatakse "haukudes". Igaks juhuks: tsükleid pole vaja kasutada, me pole neid veel õppinud.
# Sisestage esimene arv: 2
# Sisestage teine arv: 3
# Sisestage tehe: +
# Tulemus: auh auh auh auh auh

esimene_arv = int(input("Palun sisestage esimene : "))
teine_arv = int(input("Palun sisestage teine arv: "))
tehe = input("Palun sisestage tehtemärk: ")

if tehe == "+":
    tulemus = esimene_arv + tehe + teine_arv
elif tehe == "-":
    tulemus = esimene_arv - teine_arv
elif tehe == "*":
    tulemus = esimene_arv * teine_arv
elif tehe == "/":
    tulemus = esimene_arv / teine_arv
elif tehe == "-":
    tulemus = esimene_arv ** teine_arv

kordus = "auh " * tulemus
    
print("Tulemus: " , kordus)