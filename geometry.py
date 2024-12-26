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

def question_2():
    answer = messagebox.askokcancel("?", "I'm going to format your hard drive")
    print(answer)

def question_3():
    answer = messagebox.askretrycancel("?", "I'm going to format your hard drive")
    print(answer)

def question_4():
    answer = messagebox.askquestion("?", "I'm going to format your hard drive")
    print(answer)

def question_5():
    answer = messagebox.showerror("!", "Your code does nothing!")
    print(answer)

def question_6():
    answer = messagebox.showwarning("Be careful!", "Big Brother is watching you!")
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
button.pack()

button2 = tk.Button(window, text="Ask to Cancel!", command=question_2)
button2.pack()

button3 = tk.Button(window, text="Ask to Retry!", command=question_3)
button3.pack()

button4 = tk.Button(window, text="What are your plans?", command=question_4)
button4.pack()

button5 = tk.Button(window, text="Alarming message", command=question_5)
button5.pack()

button6 = tk.Button(window, text="What's going on?", command=question_6)
button6.pack()


window.mainloop()
