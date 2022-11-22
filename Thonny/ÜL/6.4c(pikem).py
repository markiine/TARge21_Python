def kuu_nimi(kuu_jrknr):
    kuu_sõnana = kuud[kuu_jrknr - 1]
    return kuu_sõnana

def kuupäev_sõnena(kuupäev):
    lahku = kuupäev.split(".")
    päev = str(lahku[0])
    kuu = str(kuu_nimi(int(lahku[1])))
    aasta = str(lahku[2])
    lause = päev + ". " + kuu + " " + aasta + ". a"
    return lause

kuud = ["jaanuar" , "veebruar" , "märts" , "aprill" , "mai" , "juuni" , "juuli" , "august" , "september" , "oktoober" , "november", "detsember"]

sisestus = input("Sisesta kuupäev kujul DD.MM.YYYY: ")

print(kuupäev_sõnena(sisestus))

# <päev>. <kuu nimi> <aasta>.