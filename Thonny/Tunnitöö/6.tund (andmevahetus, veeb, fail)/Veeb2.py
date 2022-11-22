from urllib.request import urlopen
 
#valitud kuupäev
päev = 24
kuu = 10
aasta = 2018
 
#paneme lingi kokku
vastus = urlopen("http://meteo.physic.ut.ee/et/showperiod.php?type=setday&year="+str(aasta)+"&month="+str(kuu)+"&day="+str(päev))
#loeme terve faili
baidid = vastus.read()
tekst = baidid.decode()
 
#otsime failis sõna 'keskmine', mis on ümbritsetud HTML-märgenditega
otsitav = "<SMALL>keskmine</SMALL><BR><B>"
algus = tekst.index(otsitav)       #meetod index tagastab otsitava sõna positsiooni alguse
temp_algus = algus + len(otsitav)  #indeks, kust tekstis võib leida temperatuuri
deg = tekst.index(" &deg;")        #peale temperatuuri on tühik ja sümbol
temp = tekst[temp_algus:deg]       #lõikame temperatuuri välja
 
#väljastame kuupäeva ja keskmise temperatuuri
print(str(päev)+"."+str(kuu)+"."+str(aasta)+": "+str(temp))