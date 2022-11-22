failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")

failisisu = fail.read().upper()

for rida in failisisu:
    for sümbol in rida:
        if sümbol == "Ä":
            print("AE", end = "")
        elif sümbol == "Õ":
            print("OE", end = "")
        elif sümbol == "Ö":
            print("OE", end = "")
        elif sümbol == "Ü":
            print("UE", end = "")
        else:
            print(sümbol, end = "")

fail.close()