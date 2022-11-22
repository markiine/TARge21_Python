def kasKiiruseÜletamine(kiirus, piirkiirus = 90):
    return kiirus > piirkiirus
 
print(kasKiiruseÜletamine(100))
print(kasKiiruseÜletamine(90, 70))

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