from tkinter import *

raam = Tk()
raam.title("Tühi tahvel")

# loome tahvli laiusega 600px
tahvel = Canvas(raam, width=600)
# paigutame tahvli raami ja teeme nähtavaks
tahvel.pack()
# siseneme põhitsüklisse
raam.mainloop()

print(Canvas.__init__.__doc__)
