from turtle import *
 
def ruut():                # Defineerime funktsiooni nimega ruut
    i = 0
    while (i < 4):
        forward(100)
        left(90)
        i = i + 1

for i in range(45,360,45):
    ruut()                     # Kutsume funktsiooni ruut välja. Kilpkonn joonistab ruudu küljega 100 pikslit
    right(i)                  # Pöörame paremale 45°
    ruut()                     # Kutsume uuesti funktsiooni ruut välja
 
exitonclick()