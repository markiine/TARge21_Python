from tkinter import *

raam = Tk()
raam.title("Malelaud")

tahvel = Canvas(raam, width=800, height=800, background="white")

kõrgus = 100
laius = 100
i = 0
while i < 8:
    if i % 2 == 0:
        tahvel.create_rectangle(0, i * kõrgus , 100,(i + 1) * laius, fill="white", outline="black")
        tahvel.create_rectangle(100, i * kõrgus, 200, (i + 1) * laius, fill="black", outline="black")
        tahvel.create_rectangle(200, i * kõrgus, 300,(i + 1) * laius, fill="white", outline="black")
        tahvel.create_rectangle(300, i * kõrgus, 400, (i + 1) * laius, fill="black", outline="black")
        tahvel.create_rectangle(400, i * kõrgus, 500,(i + 1) * laius, fill="white", outline="black")
        tahvel.create_rectangle(500, i * kõrgus, 600, (i + 1) * laius, fill="black", outline="black")
        tahvel.create_rectangle(600, i * kõrgus, 700,(i + 1) * laius, fill="white", outline="black")
        tahvel.create_rectangle(700, i * kõrgus, 800, (i + 1) * laius, fill="black", outline="black")
    else:
        tahvel.create_rectangle(0, i * kõrgus , 100,(i + 1) * laius, fill="black", outline="black")
        tahvel.create_rectangle(100, i * kõrgus, 200, (i + 1) * laius, fill="white", outline="black")
        tahvel.create_rectangle(200, i * kõrgus, 300,(i + 1) * laius, fill="black", outline="black")
        tahvel.create_rectangle(300, i * kõrgus, 400, (i + 1) * laius, fill="white", outline="black")
        tahvel.create_rectangle(400, i * kõrgus, 500,(i + 1) * laius, fill="black", outline="black")
        tahvel.create_rectangle(500, i * kõrgus, 600, (i + 1) * laius, fill="white", outline="black")
        tahvel.create_rectangle(600, i * kõrgus, 700,(i + 1) * laius, fill="black", outline="black")
        tahvel.create_rectangle(700, i * kõrgus, 800, (i + 1) * laius, fill="white", outline="black")
    i += 1
    
tahvel.pack()
raam.mainloop()