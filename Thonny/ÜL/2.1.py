pilvede_kõrgus = input("Palun sisesta pilvede kõrgus (km): ")
piir = 6
if float(pilvede_kõrgus) > float(piir):
    print("Need on ülemised pilved.")
else:
    print("Need ei ole ülemised pilved.")