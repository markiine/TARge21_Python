nimi = input("Sisestage oma nimi: ")
lubatud_kiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus (km/h): "))
kordaja = 3
esialgne_trahv = (tegelik_kiirus - lubatud_kiirus) * kordaja
trahv = min(190, esialgne_trahv)
tulemus = nimi + ", kiiruse ületamise eest on teie trahv " + str(trahv) + " eurot."
print(tulemus)