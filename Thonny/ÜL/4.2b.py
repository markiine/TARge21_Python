from tkinter import *

raam = Tk()
raam.title("Liiklusmärk")

tahvel = Canvas(raam, width=600, height=400, background="white")

tahvel.create_oval(10,10,100,100, fill="blue", outline="red", width= "8")

tahvel.create_line(25,25,85,85, width=6, fill="red")

tahvel.create_line(85,25,25,85, width=6, fill="red")

tahvel.pack()
raam.mainloop()
