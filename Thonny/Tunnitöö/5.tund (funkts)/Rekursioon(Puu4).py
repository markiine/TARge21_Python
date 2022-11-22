from turtle import * 
from random import *
 
def puu(pikkus):
    if pikkus < 5:
        forward(pikkus)
        back(pikkus)
    else:
        forward(pikkus)
        left(45)
        puu(randint(6,7) / 10 * pikkus)
        right(90)
        puu(randint(6,7) / 10 * pikkus)
        left(45)
        back(pikkus)
 
def mets(puudearv):
    i = 0
    left(90)
    while i < puudearv:
 
        pendown()
        puu(randint(20,59))        # Juhusliku pikkusega puu
        penup()
        right(90)
        forward(randint(100,149))  # Puude vahe on ka juhuslik
        left(90)
        i = i + 1
 
delay(0)
speed(10)   
mets(4)
 
exitonclick()