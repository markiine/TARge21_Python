from turtle import *
 
# Defineerime funktsiooni täht, mis joonistab valitud värvi ja pikkusega tähe
def täht(pikkus, värv):   
    color(värv)
    begin_fill()                 
    i = 0
    while (i < 5):
        fd(pikkus)
        rt(144)
        i = i + 1
    end_fill()
 
täht(100, "yellow")        # Kilpkonn joonistab kollase tähe pikkusega 100 pikslit
 
exitonclick()