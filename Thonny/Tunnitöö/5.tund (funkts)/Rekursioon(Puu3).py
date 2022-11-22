from turtle import * 
from random import *      # Juhuslike arvude moodul
 
def puu(pikkus):
    if pikkus < 5:
        forward(pikkus)
        back(pikkus)
    else:
        forward(pikkus)
        left(40)
        puu(randint(6,7) / 10 * pikkus)   # Tegur on 0.6 või 0.7
        right(90)
        puu(randint(6,7) / 10 * pikkus)   # Tegur on 0.6 või 0.7
        left(50)
        back(pikkus)
 
delay(0)
speed(10)
left(90)
puu(100)
exitonclick()