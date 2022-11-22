# Väljasta ekraanile kõikvõimalikud kombinatsioonid kujul "x - y - z", kus x, y ja z on mistahes täisarvud 1-st 20-ni (20 kaasaarvatud). Samuti loenda, mitu sellist kombinatsiooni leiti. Tulemus:

# 1 - 1 - 1
# 1 - 1 - 2
# 1 - 1 - 3
# [...]
# 15 - 12 - 2
# 15 - 12 - 3
# [...]
# 20 - 20 - 19
# 20 - 20 - 20
# Kokku leiti 8000 kombinatsiooni.


kombinatsioone = 0

for x in range(1,21):
    for y in range(1,21):
        for z in range(1,21):
            print(x , "-", y , "-" , z)
            kombinatsioone += 1



print("Kokku leiti " , str(kombinatsioone) , " kombinatsiooni.")