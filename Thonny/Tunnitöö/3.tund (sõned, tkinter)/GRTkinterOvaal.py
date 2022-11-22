#create_oval(x0, y0, x1, y1, option, ... )
from tkinter import *

raam = Tk()
raam.title("Ovaal tahvel")

# loome tahvli laiusega 600px
tahvel = Canvas(raam, width=600, height=400, background="black")

# roheliste servadega punane ovaal(ring)
tahvel.create_oval(10,10,100,100, fill="red", outline="green", width= "4")
# paigutame tahvli raami ja teeme nähtavaks
tahvel.pack()
# siseneme põhitsüklisse
raam.mainloop()

print(Canvas.__init__.__doc__)