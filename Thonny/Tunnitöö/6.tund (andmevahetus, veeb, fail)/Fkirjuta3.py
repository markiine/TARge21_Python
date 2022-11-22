print(ord("A"))
print(ord("a"))
print(ord("ä"))
print(ord("õ"))
print(ord(" "))

print()

print(chr(65))

print()

def kodeeri(sümbol, nihe):
     return chr(ord(sümbol) + nihe)
 
def šifreeri(failinimi, nihe):
    f = open(failinimi, "w") # open(aktseptorNimi, "w", encoding="UTF-8")
    kiri = input("Sisesta lause ")
    for sümbol in kiri:
        f.write(kodeeri(sümbol, nihe))
    f.close()
 
failinimi = input("Faili nimi? ")
nihe = int(input("Nihe? "))
šifreeri(failinimi, nihe)

print()

# while True:
    # sümbol = f.read(1)                      # loetakse üks sümbol
    # if sümbol == "":                        # kui sümboleid enam pole
        # break                               # tsükkel katkestatakse
    # print(dekodeeri(?????????), end = "")   # reavahetust ei tule