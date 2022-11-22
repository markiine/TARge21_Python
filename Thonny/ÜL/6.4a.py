def tervitus(jrk_nr):
    lause = print('Võõrustaja: "Tere!" \nTäna ' + str(jrk_nr) + '. kord tervitada, mõtiskleb võõrustaja. \nKülaline: "Tere, suur tänu kutse eest!"')
    return lause

külalisi = int(input('Sisestage külaliste arv: '))

for i in range(külalisi):
    tervitus(i + 1)