inimeste_arv = int(input("Inimeste arv: "))
kohtade_arv = int(input("Kohtade arv: "))
bussis_kohti = 40

busse_vaja = (inimeste_arv // kohtade_arv)

if inimeste_arv % kohtade_arv > 0:
    uus_busse_vaja = busse_vaja + 1
    print("Busse vaja: " + str(uus_busse_vaja))
else:
    print("Busse vaja: " + str(busse_vaja))
    
viimases_bussis_inimesi = inimeste_arv % kohtade_arv
if viimases_bussis_inimesi == 0:
    print("Viimases bussis inimesi: " + str(kohtade_arv))
else:
    print("Viimases bussis inimesi: " + str(viimases_bussis_inimesi))
    