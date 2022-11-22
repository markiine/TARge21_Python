def kuu_nimi(kuu_jrknr):
    kuu = kuud[kuu_jrknr - 1]
    return kuu

def kuupäev_sõnena(kuupäev):
    lahku = kuupäev.split(".")
    return lahku[0] + ". " + kuu_nimi(int(lahku[1])) + " " + lahku[2] + ". a"

kuud = ["jaanuar" , "veebruar" , "märts" , "aprill" , "mai" , "juuni" , "juuli" , "august" , "september" , "oktoober" , "november", "detsember"]

sisestus = input("Sisesta kuupäev kujul DD.MM.YYYY: ")

print(kuupäev_sõnena(sisestus))

# number = int(sisestus[3:5])
# kuu_nimi(int(sisestus[3:5]))
# <päev>. <kuu nimi> <aasta>.  
 