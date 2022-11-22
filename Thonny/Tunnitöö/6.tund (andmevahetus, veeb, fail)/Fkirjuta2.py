from urllib.request import urlopen
 
fail = open("andmed0.txt", "a") # fail avatakse juurde kirjutamiseks (open(failiNimi, "a", encoding="UTF-8"))
päevad = [31,28,31,30,31,30,31,31,30,31,30,31]
aasta = 2017
 
for kuu in range(1,13): # välimine tsükkel kuude järjenumbrite kaupa
    for päev in range(1, päevad[kuu-1]+1): # sisemine tsükkel päevade kaupa
        # konkreetse päeva andmed
        vastus = urlopen("http://meteo.physic.ut.ee/et/showperiod.php?type=setday&year="+str(aasta)+"&month="+str(kuu)+"&day="+str(päev))
        baidid = vastus.read()
        tekst = baidid.decode()
 
        otsitav = "<SMALL>keskmine</SMALL><BR><B>"
        algus = tekst.index(otsitav) # leitakse õige koht
        temp_algus = algus + len(otsitav) # siit algab temperatuur
        deg = tekst.index(" &deg;") # siin lõpeb
        temp = tekst[temp_algus:deg] # viilutades leitakse temperatuur
        # funktsioon rjust paneb ühekohalisele päeva ja kuu järjenumbrile 0 ette, et oleks kahekohaline. 
        fail.write(str(päev).rjust(2,"0")+"."+str(kuu).rjust(2,"0")+"."+str(aasta)+": "+str(temp)+"\n")
 
 
vastus.close()
fail.close()