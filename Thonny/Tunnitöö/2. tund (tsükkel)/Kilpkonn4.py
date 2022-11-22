from turtle import *
i = 0               # Muutuja i väärtus on esialgu 0
while i < 8:        # Tsükli keha läbitakse neli korda.
   forward(70 * i)
   left(90)
   i = i + 1        # Muutuja i väärtust suurendatakse ühe võrra
exitonclick()