from datetime import datetime

kuupäev_kellaeg = datetime.today()

# print("Kuupäev ja kellaeg: " + str(kuupäev_kellaeg))

# fail = open("paevik.txt", "w")
# fail.write(str(kuupäev_kellaeg) + "\n")
# fail.write("Lahendan kontrollülesannet 7.2 " + "\n")

# fail.close()

sissekanne = input("Sisesta sissekande tekst: ")

fail = open("paevik.txt", "a")
fail.write(str(kuupäev_kellaeg) + "\n")
fail.write(sissekanne + "\n")

fail.close()