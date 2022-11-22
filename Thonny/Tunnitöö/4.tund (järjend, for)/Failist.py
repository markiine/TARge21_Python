fail = open("jooks.txt", encoding="UTF-8")
kokku = 0
for rida in fail:
    kokku += float(rida)
fail.close()
print("Kokku joosti " + str(kokku) + " kilomeetrit.")

fail = open("jooks.txt", encoding="UTF-8")
kokku = 0
for rida in fail:
    kilomeetreid = float(rida)
    if kilomeetreid > 10:
        kokku += kilomeetreid
fail.close()
print("Kokku joosti pikki jookse " + str(kokku) + " kilomeetrit.")

fail = open("jooks.txt", encoding="UTF-8")
kokku = 0
jooksud = []
for rida in fail:
    jooksud.append(float(rida))
    # teine variant: jooksud += [float(rida)]     
fail.close()
print(jooksud[4])