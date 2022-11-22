# create_line(x0, y0, x1, y1, ..., xn, yn, option, ...)
from tkinter import *

raam = Tk()
raam.title("Joontega tahvel")

# loome tahvli laiusega 600px
tahvel = Canvas(raam, width=600, height=4000, background="red")

# üks horisontaalne sirglõik
tahvel.create_line(50,50,100,50)
 
# horisontaalne sirglõik ja vertikaalne sirglõik
tahvel.create_line(50,150,100,150,100,200)
 
# sirglõik paksusega 4px
tahvel.create_line(50,100,100,250, width=4)
 
# rohelist värvi nool paksusega 4px
tahvel.create_line(350,50,350,100, width=4, fill="green", arrow=LAST)

# paigutame tahvli raami ja teeme nähtavaks
tahvel.pack()
# siseneme põhitsüklisse
raam.mainloop()

print(Canvas.__init__.__doc__)