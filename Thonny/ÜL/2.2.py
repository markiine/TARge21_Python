punktisumma = float(input("Palun sisesta punktisumma: "))
if punktisumma >= 0 and punktisumma < 66:
    print("Vähem kui kandideerimiseks vajalik.")
elif punktisumma >= 66 and punktisumma < 85:
    print("Kandideerimine vastuvõtule.")
elif punktisumma >= 85 and punktisumma <=100:
    print ("Vastuvõtt tagatud.")
else:
    print("Vigane punktisumma.")