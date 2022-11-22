def mahlapakkide_arv(õunad_kg):
    arv = round((õunad_kg) * 0.4 / 3)
    return arv

õunad = float(input("Sisestage õunte kogus kilogrammides: "))

print(mahlapakkide_arv(õunad))