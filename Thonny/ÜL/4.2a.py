from tkinter import *
 
raam = Tk()
raam.title("Kuressaare valla lipp")

tahvel = Canvas(raam, width=600, height=300)
kõrgus = 100
i = 0

while i < 3:
    if i == 0 or i == 2:
        tahvel.create_rectangle(0, i * kõrgus, 600, (i + 1) * kõrgus, fill="blue", outline="black")
    else:
        tahvel.create_rectangle(0, i * kõrgus, 600, (i + 1) * kõrgus, fill="white", outline="black")
    i += 1
    
tahvel.create_oval(230,190,370,110, fill="yellow", outline="black")

tahvel.pack()
raam.mainloop()
