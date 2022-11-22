a = ['A', 'B', 'C', 'D', 'E']
print(a[0:2])
print(a[:2])
print(a[2:5])
print(a[2:])
print(a[-2:])

print()

sõne1 = 'Tartu'
print(sõne1[1:4])
sõne2 = sõne1
print(sõne2[-2:])
print("Väike-Maarja"[4:9])

print()

b = [1, 2, 3, 4]
print(b[:])

print()

a = [5, 8]
a.append(7)
print(a)
b = [5, 8]
b += [7]
print(b)

print()

nädalapäevad = ["esmaspäev", "teisipäev", "kolmapäev", "neljapäev", "reede", "laupäev", "pühapäev"]
print(nädalapäevad)
print(min(nädalapäevad))
print(max(nädalapäevad))