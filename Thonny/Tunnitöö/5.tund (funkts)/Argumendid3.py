def kasKiiruse√úletamine(kiirus, piirkiirus = 90):
    return kiirus > piirkiirus
 
print(kasKiiruse√úletamine(100))
print(kasKiiruse√úletamine(90, 70))

print()

# end = "\n" -sama- end = "reavahetus"
print("Tervitus ", "Tekst" , end = "reavahetus" , sep = "eraldaja")

print()
print()

print("tartu".capitalize())
print("Tartu".endswith("tu"))
print("Tartu".upper())
linn = "Tartu"
print(linn.lower())