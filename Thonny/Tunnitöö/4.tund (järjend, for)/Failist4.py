readfailist = open("RV031sm.csv")
aastad = []                              # järjend aastate jaoks
iibed = []                               # järjend iivete jaoks
for rida in readfailist:                 # reakaupa listist readfailist
    realt = rida.split(';')              # jaotada semikooloni kohalt
    aastad += [int(realt[0].strip('"'))] # aastate järjendisse juurde
    # või aastad.append(int(realt[0].strip('"')))
    iibed += [int(realt[1])]             # iivete järjendisse juurde
    # või iibed.append(int(realt[1]))
readfailist.close()                      # faili ei lähe enam vaja
print(aastad)
print(iibed)