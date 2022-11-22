fail = open("rebased.txt", encoding = "UTF-8")
vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))

aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))

if aasta == 2011:
    vastuvõetuid = vastuvõetud [0]
elif aasta == 2012:
    vastuvõetuid = vastuvõetud [1]
elif aasta == 2013:
    vastuvõetuid = vastuvõetud [2]
elif aasta == 2014:
    vastuvõetuid = vastuvõetud [3]
elif aasta == 2015:
    vastuvõetuid = vastuvõetud [4]
elif aasta == 2016:
    vastuvõetuid = vastuvõetud [5]
elif aasta == 2017:
    vastuvõetuid = vastuvõetud [6]
elif aasta == 2018:
    vastuvõetuid = vastuvõetud [7]
elif aasta == 2019:
    vastuvõetuid = vastuvõetud [8]
    
fail.close()

print(aasta , ". aastal oli vastuvõetuid" , vastuvõetuid)