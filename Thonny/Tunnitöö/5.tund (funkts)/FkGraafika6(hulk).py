from turtle import *
def hulknurk(n):    
    i = 0
    nurk = 360 / n         # Arvutatakse kilpkonna pööramise nurga suurus
    while (i < n):
        forward(100)
        left(nurk)
        i = i + 1
 
hulknurk(5)
exitonclick()