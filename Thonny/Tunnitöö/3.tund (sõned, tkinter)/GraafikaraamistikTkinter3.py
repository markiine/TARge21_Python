from tkinter import *

raam = Tk()
raam.title("Tühi tahvel")

# loome tahvli laiusega 600px
tahvel = Canvas(raam, width=600, height=4000)

tahvel = Canvas(raam, background="red")
# paigutame tahvli raami ja teeme nähtavaks
tahvel.pack()
# siseneme põhitsüklisse
raam.mainloop()

print(Canvas.__init__.__doc__)
