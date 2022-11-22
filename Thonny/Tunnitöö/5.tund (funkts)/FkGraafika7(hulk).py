from turtle import *
 
# Defineerime funktsiooni nimega hulknurk. Argumendid on nurkade arv ja külje pikkus
def hulknurk(n, külg):    
    i = 0
    nurk = 360 / n         # Arvutatakse kilpkonna pööramise nurga suurus
    while (i < n):
        forward(külg)
        left(nurk)
        i = i + 1
 
fillcolor("green")
begin_fill()
hulknurk(6, 150)           # Kilpkonn joonistab rohelise korrapärase kuusnurga küljega 150 pikslit
end_fill()
 
fillcolor("red")
begin_fill()
hulknurk(7, 50)            # Kilpkonn joonistab punase korrapärase seitsenurga küljega 50 pikslit
end_fill()
 
exitonclick()