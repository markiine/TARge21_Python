def tervitus(jrk_nr):
    lause = jrk_nr
    return lause

külalisi = int(input('Sisestage külaliste arv: '))

for i in range(külalisi):
    i += 1
    print('Võõrustaja: "Tere!"')
    print('Täna' , (tervitus(i)) , '. kord tervitada, mõtiskleb võõrustaja.')
    print('Külaline: "Tere, suur tänu kutse eest!"')