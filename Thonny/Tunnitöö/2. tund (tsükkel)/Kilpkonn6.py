from turtle import *
speed(0)

summa = 0
i = 1               
while i <= 200:        
   nihe = (10 + 3 * i)
   forward(nihe)
   left(90)
   i = i + 1
   summa += 1
   print("Summa: ", summa)
exitonclick()