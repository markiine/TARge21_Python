# create_text(x0, y0, option, ... )
from tkinter import *

raam = Tk()
raam.title("Teksti tahvel")

# loome tahvli laiusega 600px
tahvel = Canvas(raam, width=600, height=400, background="pink")

# musta värvi tekst "Tere!"
tahvel.create_text(50,50, text="Tere!")
# sinist värvi teksti "Tere!" alumine vasak punkt on (50, 50)
tahvel.create_text(150,150, text="Tere!", anchor=SW, fill="blue")

# paigutame tahvli raami ja teeme nähtavaks
tahvel.pack()
# siseneme põhitsüklisse
raam.mainloop()

print(Canvas.__init__.__doc__)