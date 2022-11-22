f = open("sms.txt", encoding="UTF-8")
 
while True:                     # lõpmatu tsükkel, kui ei katkestata
    sümbol = f.read(1)          # loetakse üks sümbol
    if sümbol == "":            # kui enam sümboleid pole
        break                   # tsükkel katkestatakse
    if sümbol == "õ":
        print("6", end = "")    # reavahetust ei tule
    else:
        print(sümbol, end = "") # reavahetust ei tule
 
f.close()                       # faili ei lähe enam vaja

print()
print()

# Kahe for-tsükliga

f = open("sms.txt", encoding="UTF-8")
 
for rida in f:                      # ridade kaupa
    for sümbol in rida:             # sümbolite kaupa
        if sümbol == "õ":
            print("6", end = "")    # reavahetust ei tule
        else:
            print(sümbol, end = "") # reavahetust ei tule
 
f.close()                           # faili ei lähe enam vaja

print()
print()

# Funktsiooni read kasutamine, replace

f = open("sms.txt", encoding="UTF-8")
 
failisisu = f.read()
 
asendatudõ = failisisu.replace("õ","6")
 
print(asendatudõ)
 
f.close()
