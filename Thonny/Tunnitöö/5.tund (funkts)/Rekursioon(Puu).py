from turtle import *
 
def puu(pikkus):          
    if pikkus < 5:         # Rekursiooni baas
        forward(pikkus)    # Ainult tüvi
        back(pikkus)
    else:                  # Rekursiooni samm
        forward(pikkus)    # Tüvi
        left(45)
        puu(0.6 * pikkus)  # Haru, mis on väiksem puu
        right(90)
        puu(0.6 * pikkus)  # Teine haru, mis on ka väiksem puu
        left(45)
        back(pikkus)       # Tüvepidi tagasi
 
delay(0)
speed(10)       
left(90)
puu(100)
 
exitonclick()