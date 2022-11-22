def faktoriaal(n):
    if n == 0:             # Rekursiooni baas
        return 1
    else:                  # Rekursiooni samm
        return n * faktoriaal(n-1)
 
print(faktoriaal(4))

print()

print(faktoriaal(0))

print()

print(faktoriaal(400))