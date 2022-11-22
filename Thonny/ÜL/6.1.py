def banner(reklaam):
    lause = reklaam.upper()
    return lause

kordus = int(input("Mitu korda soovite reklaamlauset kuvada? "))
reklaamlause = input("Sisestage reklaamlause: ")
 
for i in range(kordus):
    print(banner(reklaamlause))