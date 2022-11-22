kasutajanimi = "Mo\nty"
parool = "Py\thon"

f = open("testideks.txt", "w")
f.write("kasutajanimi:" + kasutajanimi + "\n")
f.write("parool:" + parool)
f.close()


def funkt(arv):
    a = 1
    b = arv
    while b - a > 2:
        b -= arv
        a += 2
    return b
print(funkt(4))


def kolmega(arv):
    return arv % 3
m = 1
while m < 60 and m !=4:
    print(kolmega(kolmega(m) + kolmega(m+1)))
    m += 3


järjend = [1, 0, 2, 2]

for i in range(1, len(järjend), 2):
    print(järjend[järjend[i]])


järjend = [2, 4, 9, 0, -1, 5, -1]
print(järjend[järjend[1]])
