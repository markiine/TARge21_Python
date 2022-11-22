fail = open("rebased.txt", encoding = "UTF-8")
vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))

aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))

positsioon = aasta - 2011
    
fail.close()

print(aasta , ". aastal oli vastuvõetuid" , vastuvõetud [positsioon])
