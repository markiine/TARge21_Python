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


# Arvesse tuleksid ka need juhud, kus vahetult sõna järel on mingi kindel kirjavahemärk

# if s.strip(".,?") == "tõde":
    # tõde += 1
# if s.strip(".,?") == "õigus":
    # õigus += 1


# Kontrollitakse, kas sõna “tõde” (“õigus”) sisaldub vaadeldavas sõnes:

# if "tõde" in s:
    # tõde += 1
# if "õigus" in s:
    # õigus += 1


# Tahame suurte tähtedega variante arvesse võtta:

# if "tõde" in s.lower():
    # tõde += 1
# if "õigus" in s.lower():
    # õigus += 1


f = open("anton_hansen_tammsaare_tode_ja_oigus_i.txt", encoding='UTF-8')
 
tõde = 0   # loendaja
õigus = 0  # loendaja
 
for rida in f:           # ridade kaupa
    sõnad = rida.split() # rea sõnad järjendisse
    for s in sõnad:      # sõnade kaupa
        if s.lower().strip(".,?") == "tõde" or "tõde" in s.lower().strip(".,?"):
            tõde += 1
        if s.lower().strip(".,?") == "õigus" or "õigus" in s.lower().strip(".,?"):
            õigus += 1
 
print("Failis sõna 'tõde' on", tõde,  "korda.")
print("Failis sõna 'õigus' on", õigus, "korda.")
 
f.close()

