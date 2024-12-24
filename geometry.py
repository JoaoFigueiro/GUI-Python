import tkinter as tk
from tkinter import messagebox

def click(*args):
    global size, grows
    if grows:
        size += 50
        if size >= 500:
            grows = False
    else:
        size -= 50
        if size <= 100:
            grows = True
    window.geometry(str(size) + "x" + str(size))


def really():
    if messagebox.askyesno("?", "Wilt thou be gone?"):
        window.destroy()


def question():
    answer = messagebox.askyesno("?", "To be or not to be?")
    print(answer)

size = 100
grows = True
window = tk.Tk()
window.maxsize(width=400, height=400)
window.minsize(width=250, height=200)
window.resizable(width=True, height=False)

window.geometry("300x300")
window.bind("<Button-1>", click)
window.protocol("WM_DELETE_WINDOW", really)

button = tk.Button(window, text="Ask the question!", command=question)


window.mainloop()
