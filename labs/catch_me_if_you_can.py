from tkinter import *
import random


def newxy(xy):
    nw = random.randint(1, 440)
    while abs(xy - nw) < 50:
        nw = random.randint(1, 440)
    return nw


def domove(ev):
    global x, y
    x = newxy(x)
    y = newxy(y)
    bt.place(x=x, y=y)

wn = Tk()
wn.geometry("500x500")
wn.title("Catch me!")
bt = Button(wn, text="Catch me!")
bt.bind("<Enter>", domove)
x = y = 10
bt.place(x=x, y=y)
random.seed()
wn.mainloop()
