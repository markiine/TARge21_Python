vanus = int(input("Sisestage enda vanus (täisarvuna): "))
sugu = input("Sisestage enda sugu (M, m, N, n): ")
treening = int(input("Sisestage treeningu tüüp (1 - tervisetreening, 2 - põhivastupidavuse treening, 3 - intensiivne aeroobne treening): "))
mehed = 220 - vanus
naised = 206 - (vanus * 88 / 100)

vähim1_m = round(0.5 * mehed)
suurim1_m = round(0.7 * mehed)
vähim2_m = round(0.7 * mehed)
suurim2_m = round(0.8 * mehed)
vähim3_m = round(0.8 * mehed)
suurim3_m = round(0.87 * mehed)

vähim1_n = round(0.5 * naised)
suurim1_n = round(0.7 * naised)
vähim2_n = round(0.7 * naised)
suurim2_n = round(0.8 * naised)
vähim3_n = round(0.8 * naised)
suurim3_n = round(0.87 * naised)

if (sugu.lower() == "m") and (treening == 1):
    print("Pulsisagedus peaks olema vahemikus " + str(vähim1_m) + " kuni " + str(suurim1_m) + ".")
elif (sugu.lower() == "m") and (treening == 2):
    print("Pulsisagedus peaks olema vahemikus " + str(vähim2_m) + " kuni " + str(suurim2_m) + ".")
elif (sugu.lower() == "m") and (treening == 3):
    print("Pulsisagedus peaks olema vahemikus " + str(vähim3_m) + " kuni " + str(suurim3_m) + ".")
elif (sugu.lower() == "n") and (treening == 1):
    print("Pulsisagedus peaks olema vahemikus " + str(vähim1_n) + " kuni " + str(suurim1_n) + ".")
elif (sugu.lower() == "n") and (treening == 2):
    print("Pulsisagedus peaks olema vahemikus " + str(vähim2_n) + " kuni " + str(suurim2_n) + ".")
elif (sugu.lower() == "n") and (treening == 3):
    print("Pulsisagedus peaks olema vahemikus " + str(vähim3_n) + " kuni " + str(suurim3_n) + ".")
    
    