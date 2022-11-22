aasta = 2017                             # loendamist ei pea nullist alustama
arv = 1315635
iibe_kordaja = -1.33                     # Promillides (arvukuse muutus 1000 elaniku kohta)
while aasta < 2080:
   arv = arv + arv * iibe_kordaja / 1000 # Arvutame selle aasta uue arvu
   aasta = aasta + 1                     # Läheme järgmise aasta juurde
print("Aastal " + str(aasta) + " on elanikke " + str(round(arv)) + ".")


aasta = 2017
arv = 1315635
iibe_kordaja = 6
while arv < 2000000:
   arv = arv + arv * iibe_kordaja / 1000
   aasta = aasta + 1
print("Aastal " + str(aasta) + " on elanike arv " + str(round(arv)) + ".")