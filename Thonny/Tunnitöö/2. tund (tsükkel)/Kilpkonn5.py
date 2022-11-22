from turtle import *
speed(0)
i = 0               # Muutuja i väärtus on esialgu 0
while i <= 80:        # Tsükli keha läbitakse neli korda.
   forward(100 + 3 * i)
   left(90)
   i = i + 1        # Muutuja i väärtust suurendatakse ühe võrra
exitonclick()