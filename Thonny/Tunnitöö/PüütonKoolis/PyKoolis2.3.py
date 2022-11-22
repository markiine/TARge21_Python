# Koosta lihtne kalkulaator. Kasutajalt küsitakse kaks arvu ja tehtemärk ning seejärel kuvatakse tehe koos vastusega. Näiteks:
# Sisestage esimene arv: 2
# Sisestage esimene arv: 2
# Sisestage teine arv: 3
# Sisestage tehe: +
# Tulemus: 2+3=5

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
    
print("Tulemus: " , esimene_arv, tehe, teine_arv, "=", tulemus)
