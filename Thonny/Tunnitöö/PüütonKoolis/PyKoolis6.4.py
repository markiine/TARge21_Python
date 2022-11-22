# Koer, kass, jänes, sipelgasiil ja lendorav hakkasid vaidlema, kellel on kõige pikem nimetus. Koosta programm, kus on antud loomanimede järjend. Loo funktsioon, mis saab argumendina ette looma nime ning tagastab (mitte ei trüki!) selle pikkuse. Lase programmil kutsuda funktsiooni välja iga loomanimede järjendi elemendiga ning trükib ekraanile nime pikkuse. Pärast pikkuste kontrollimist peab programm väljastama kõige pikema loomanime (võrdsete pikkuste puhul võib esitada vaid ühe pikimatest).

loomad = ["koer", "kass", "jänes", "sipelgasiil", "lendorav"]

def nime_pikkus(nimi):
    return len(nimi)

# pikim_nimi = max(loomad, key = len)  # Variant 2, parameerer = key
# print(pikim_nimi)

pikim_nimi = ""

for loom in loomad:
    pikkus = nime_pikkus(loom)  # pikkuse võib ära jätta ja asendada kohe nime_pikkus(loom)
    if pikkus > nime_pikkus(pikim_nimi):
        pikim_nimi = loom

print("Pikim nimi on: " + pikim_nimi)