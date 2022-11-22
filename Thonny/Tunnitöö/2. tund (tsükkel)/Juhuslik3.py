from random import randint
i = 1
tulemus = 0
while i < 6:
    vise = randint(1, 6)
    print("Täringu " + str(i) + ". viskel saadi " + str(vise) + ".")
    if vise == 6:
        print("Hurraaaaaaaa!")
    tulemus += vise
    i += 1
print("Kogutulemus on " + str(tulemus) + ".")