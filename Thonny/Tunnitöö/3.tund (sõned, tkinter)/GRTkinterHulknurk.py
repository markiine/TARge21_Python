# create_polygon(x0, y0, x1, y1, ..., option, ...)
from tkinter import *

raam = Tk()
raam.title("Hulknurk tahvel")

tahvel = Canvas(raam, width=600)
tahvel = Canvas(raam, height=600)
# mustade servadega punane kolmnurk
tahvel.create_polygon(150,350,150,400,200,375, fill="red",
outline="black")

# paigutame tahvli raami ja teeme nähtavaks
tahvel.pack()
# siseneme põhitsüklisse
raam.mainloop()

print(Canvas.__init__.__doc__)