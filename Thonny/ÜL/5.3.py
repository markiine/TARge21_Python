fail = open("konto.txt", encoding="UTF-8")
tehingud = []

for rida in fail:
    tehingud.append(float(rida))

fail.close()

for i in tehingud:
    if i > 0:
        print(i)