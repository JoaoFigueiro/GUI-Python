from tkinter import Tk, Button, Canvas


def change_phase():
    global canvas, light

    phases = ((True, False, False),
              (True, True, False),
              (False, False, True),
              (False, True, False))

    r, o, g = phases[light % 4]
    canvas.itemconfigure(canvas.find_withtag("red")[0], fill="red" if r else "light gray")
    canvas.itemconfigure(canvas.find_withtag("orange")[0], fill="orange" if o else "light gray")
    canvas.itemconfigure(canvas.find_withtag("green")[0], fill="green" if g else "light gray")

    light += 1


win = Tk()
win.title('Traffic Lights')
win.geometry('300x975')
win.resizable(0, 0)

light = 0

canvas = Canvas(win, width=300, height=900, bg='grey', borderwidth=2)

canvas.create_oval(10, 10, 290, 290, fill="light gray", tags="red")
canvas.create_oval(10, 300, 290, 590, fill="light gray", tags="orange")
canvas.create_oval(10, 600, 290, 890, fill="light gray", tags="green")

canvas.pack()

quit = Button(win, text='Quit', command=win.quit)
quit.pack(side='left', fill='both', expand='yes')

next = Button(win, text='Next', command=change_phase)
next.pack(side='right', fill='both', expand='yes')

win.mainloop()