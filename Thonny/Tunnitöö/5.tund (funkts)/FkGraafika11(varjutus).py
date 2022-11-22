from turtle import *
 
def täht(pikkus, värv):   
    color(värv)
    begin_fill()                 
    i = 0
    while (i < 5):
        fd(pikkus)
        rt(144)
        i = i + 1
    end_fill()
 
täht(100, "yellow")
up()
lt(90)
fd(100)
down()
pencolor("yellow")
circle(100)
bgcolor("#000000")

exitonclick()