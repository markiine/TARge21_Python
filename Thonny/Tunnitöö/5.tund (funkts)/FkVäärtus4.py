def kas_raha_jätkub(kghind, kogus, raha):
    hind = kghind * kogus
    if hind <= raha:
        return True
    else:
        return False
 
if kas_raha_jätkub(2, 4.5, 10):
    print("Ostan")

print()

def reaktsioon(punkte):
    if punkte >= 50:
        return "Olid tubli!"
    else:
        return "Püüa veel!"
print(reaktsioon(50))