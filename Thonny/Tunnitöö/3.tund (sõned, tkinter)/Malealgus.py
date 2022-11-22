from tkinter import *

raam = Tk()
raam.title("Malelaud")

tahvel = Canvas(raam, width=800, height=800, background="white")

tahvel.create_rectangle(0,0,100,100, fill="red", outline="black")
tahvel.create_rectangle(100,100,200,0, fill="black", outline="black")
tahvel.create_rectangle(0, 400, 880, 560, fill="blue", outline="blue")


tahvel.pack()
raam.mainloop()