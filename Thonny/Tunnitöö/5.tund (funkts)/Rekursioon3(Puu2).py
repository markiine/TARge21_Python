from turtle import *
 
def puu(pikkus):
    if pikkus < 5:
        forward(pikkus)    
        back(pikkus)
    else:
        forward(pikkus)
        left(40)           # Pöörame nüüd hoopis 40 kraadi
        puu(0.6 * pikkus)
        right(90)
        puu(0.6 * pikkus)
        left(50)           # ja siin 50 kraadi
        back(pikkus)
 
delay(0)
speed(10)
left(90)
puu(100)
 
exitonclick()