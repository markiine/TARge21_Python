from tkinter import *
 
raam = Tk()
raam.title("Maja")

tahvel = Canvas(raam, width=600, height=600, background="white")
#sein
tahvel.create_rectangle(100,500,500,300, fill="brown", outline="black")
#uks
tahvel.create_rectangle(275,500,325,425, fill="black", outline="black")
#aken1
tahvel.create_rectangle(150,450,250,350, fill="light blue", outline="black")
#aken2
tahvel.create_rectangle(350,450,450,350, fill="light blue", outline="black")
#katus
tahvel.create_polygon(100,300,500,300,300,250, fill="black", outline="black")
#korsten
tahvel.create_rectangle(225,290,250,225, fill="grey", outline="black")

tahvel.pack()
raam.mainloop()

