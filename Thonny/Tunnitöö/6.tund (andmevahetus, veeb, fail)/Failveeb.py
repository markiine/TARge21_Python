f = open("anton_hansen_tammsaare_tode_ja_oigus_i.txt", encoding='UTF-8')
 
tõde = 0   # loendaja
õigus = 0  # loendaja
 
for rida in f:           # ridade kaupa
    sõnad = rida.split() # rea sõnad järjendisse
    for s in sõnad:      # sõnade kaupa
        if s == "tõde":
            tõde += 1
        if s == "õigus":
            õigus += 1
 
print("Failis sõna 'tõde' on", tõde,  "korda.")
print("Failis sõna 'õigus' on", õigus, "korda.")
 
f.close()