from turtle import *
 
def ruut(külg):            # Defineerime funktsiooni nimega ruut, mille argumendiks on ruudu külje pikkus
    i = 0
    while (i < 4):
        forward(külg)      # Siin kasutatakse argumenti
        left(90)
        i = i + 1
 
ruut(50)                   # Kilpkonn joonistab ruudu küljega 50 pikslit
ruut(75)                   # Kilpkonn joonistab ruudu küljega 75 pikslit
 
exitonclick()