# create_rectangle (x0, y0, x1, y1, option, ... )
from tkinter import *

raam = Tk()
raam.title("Ristküliku tahvel")

# loome tahvli laiusega 600px
tahvel = Canvas(raam, width=600, height=4000, background="red")

# seest tühi ristkülik (ruut) mustade servadega
tahvel.create_rectangle(150,50,200,100)
 
# seest tühi ristkülik kollaste servadega, mille paksus on 2px
tahvel.create_rectangle(150,150,200,200, width=2, outline="yellow")
 
# mustade servadega roheline ristkülik
tahvel.create_rectangle(150,250,200,300, fill="green")

# paigutame tahvli raami ja teeme nähtavaks
tahvel.pack()
# siseneme põhitsüklisse
raam.mainloop()

print(Canvas.__init__.__doc__)