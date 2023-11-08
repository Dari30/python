import time
import tkinter as tk
import random

WIDTH = 500


def circled():
    d = random.randint(0, WIDTH)
    x = random.randint(0, WIDTH - d)
    y = random.randint(0, WIDTH - d)
    circle = canvas.create_oval(x, y, x + d, y + d, fill=random.choice(colors))
    return circle


def oval():
    h = random.randint(0, WIDTH)
    w = random.randint(0, WIDTH)
    x = random.randint(0, WIDTH - w)
    y = random.randint(0, WIDTH - h)
    canvas.create_oval(x, y, x + w, y + h, fill=random.choice(colors))


def square():
    a = random.randint(0, WIDTH)
    x = random.randint(0, WIDTH - a)
    y = random.randint(0, WIDTH - a)
    canvas.create_rectangle(x, y, x + a, y + a, fill=random.choice(colors), outline=random.choice(colors))
def u1circle():
    global stop1
    stop1=False
    while True:
        circled()
        window.update()
        time.sleep(1)
        if stop1:
            break
def stop():
    global stop1
    stop1=True
def mcircle():
    global stop1
    stop1=False
    circle = circled()
    dx=1
    dy=2
    while True:
        coords=canvas.coords(circle)
        left=coords[0]
        top=coords[1]
        right=coords[2]
        bot=coords[3]
        if right > WIDTH or left < 0:
            dx=-dx
        if bot > WIDTH or top < 0:
            dy=-dy
        canvas.move(circle,dx,dy)
        window.update()
        time.sleep(0.125)
        if stop1:break
colors = ['red', 'blue', 'green', 'pink', 'black', 'yellow', 'orange', 'purple', 'brown']
window = tk.Tk()
window.title("guess the number")
window.geometry("650x500")
canvas = tk.Canvas(window, width=WIDTH, height=WIDTH, bg="white")
canvas.place(x=0, y=0)
button1 = tk.Button(window, text="draw circle", command=circled)
button1.place(x=525, y=25)
button2 = tk.Button(window, text="draw oval", command=oval)
button2.place(x=525, y=65)
button3 = tk.Button(window, text="draw square", command=square)
button3.place(x=525, y=105)
buttonu1=tk.Button(window, text="start drawing circles endlessly", command=u1circle)
buttonu1.place(x=525, y=145)
buttonus=tk.Button(window, text="stop drawing circles endlessly", command=stop)
buttonus.place(x=525, y=185)
buttonmove=tk.Button(window, text="start drawing moving circle", command=mcircle)
buttonmove.place(x=525, y=225)
buttonusm=tk.Button(window, text="stop drawing moving circle", command=stop)
buttonusm.place(x=525, y=265)


window.mainloop()
