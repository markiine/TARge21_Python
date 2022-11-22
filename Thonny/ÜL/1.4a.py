ainepunktide_arv = int(input("Sisestage ainepunktide arv: "))
nädalate_arv = int(input("Sisestage nädalate arv: "))
ainepunktide_ajakulu = 26
ajakulu = round(ainepunktide_arv * ainepunktide_ajakulu / nädalate_arv)
print(ajakulu)