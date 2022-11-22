piir = int(input("Millisest arvust väiksemaks peab tulemus jääma? "))
tulemus = 1
while tulemus < piir:
    print(tulemus)
    tulemus = tulemus * 3
    
piir = int(input("Mitu tulemust kuvada? "))
tulemus = 1
jrk = 0
while jrk < piir:
    print(str(jrk) + ". rida on " + str(tulemus))
    tulemus = tulemus * 3
    jrk = jrk + 1