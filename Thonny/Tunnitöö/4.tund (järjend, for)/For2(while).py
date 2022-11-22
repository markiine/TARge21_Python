a = [12, 23, 34, 45, 56]
i = 0
while i < len(a):
    print(a[i])
    i += 1

print()

a = [12, 23, 34, 45, 56]
i = 0
while i < len(a):
    if a[i] > 30:
        a[i] = 0
    i += 1
print(a)