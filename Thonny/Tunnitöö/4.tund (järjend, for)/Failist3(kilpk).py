from turtle import *
 
# faili avamine
fail = open("kilpkonn.txt")
# faili töötlemine ja kilpkonnaga joonistamine
for rida in fail:
    osad = rida.split()  # tühikute kohal osadeks
    liikumine = osad[0]  # kuidas liikuda
    arv = int(osad[1])   # kui palju
    if liikumine == "vasakule":
        left(arv)
    elif liikumine == "paremale":
        right(arv)
    elif liikumine == "edasi":
        forward(arv)
    elif liikumine == "tagasi":
        backward(arv)
    else:
        print("Ei saa sellest käsust aru!")
 
fail.close()
exitonclick()