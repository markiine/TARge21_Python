def failistSõnejärjendisse(fail):
    järjend = []
    for rida in fail:
        järjend += [rida.strip()]  # alternatiivselt: järjend.append(rida.strip())
                                   # strip() võtab lõpust ära reavahetuse
    fail.close()
    return järjend
failinimi = input("Sisestage failinimi ")
fail = open(failinimi, encoding="UTF-8")
sõned = failistSõnejärjendisse(fail)
print(sõned)
print(sõned[3])