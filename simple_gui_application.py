import tkinter as tk
from tkinter import messagebox

win = tk.Tk()

# label = tk.Label(win, text = "Little label:")
# label.pack()
#
# frame = tk.Frame(win, height=30, width=100, bg="#000099")
# frame.pack()
#
# button = tk.Button(win, text="Button")
# button.pack(fill=tk.X)
#
# switch = tk.IntVar()
# switch.set(1)
#
# checkbutton = tk.Checkbutton(win, text="Check Button", variable=switch)
# checkbutton.pack()
#
# entry = tk.Entry(win, width=30)
# entry.pack()
#
# radiobutton_1 = tk.Radiobutton(win, text="Steak", variable=switch, value=0)
# radiobutton_1.pack()
# radiobutton_2 = tk.Radiobutton(win, text="Salad", variable=switch, value=1)
# radiobutton_2.pack()

# def clicked():
#     messagebox.showinfo("info", "some\ninfo")

# button_1 = tk.Button(win, text="Show info", command=clicked)
# button_1.pack()
# button_2 = tk.Button(win, text="Quit", command=win.destroy)
# button_2.pack()

def click(event=None):
    if event is None:
        tk.messagebox.showinfo("Click!", "I love clicks!")
    else:
        string = "x=" + str(event.x) + ",y=" + str(event.y) + \
                 ",num=" + str(event.num) + ",type=" + event.type
        tk.messagebox.showinfo("Click!", string)


# label = tk.Label(win, text="Label")
# label.pack()
#
# button = tk.Button(win, text="Button", command=click)
# button.pack(fill=tk.X)
#
# frame = tk.Frame(win, height=30, width=100, bg="#55BF40")
# frame.pack()

# label = tk.Label(win, text="Label")
# label.bind("<Button-1>", click)   # Line I
# label.pack()
#
# button = tk.Button(win, text="Button", command=click)
# button.pack(fill=tk.X)
#
# frame = tk.Frame(win, height=30, width=100, bg="#55BF40")
# frame.bind("<Button-1>", click)   # Line II

# def on_off():
#     global switch
#     if switch:
#         #button_2.config(command=lambda: None)
#         #button_2.config(text="Gee!")
#         label.unbind("<Button-1>")
#     else:
#         # button_2.config(command=peekaboo)
#         # button_2.config(text="Peekaboo!")
#         label.bind("<Button-1>", rhyme)
#     switch = not switch
#
#
# def rhyme(dummy):
#     global word_no, words
#     word_no += 1
#     label.config(text=words[word_no % len(words)])


# def peekaboo():
#     messagebox.showinfo("", "PEEKABOO!")
#
#
# def do_nothing():
#     pass

# switch = True
#
# words = ["Old", "McDonald", "Had", "A", "Farm"]
# word_no = 0
#
# button_1 = tk.Button(win, text="On/Off", command=on_off)
# button_1.pack()

# button_2 = tk.Button(win, text="Peekaboo!", command=peekaboo)
# button_2.pack()

# label = tk.Label(win, text=words[0])
# label.bind("<Button-1>", rhyme)
# label.pack()

# def hello(dummy):
#     messagebox.showinfo("", "Hello!")
#
# button = tk.Button(win, text="On/Off")
# button.pack()
# label = tk.Label(win, text="Label")
# label.pack()
# frame = tk.Frame(win, bg="yellow", width=100, height=20)
# frame.pack()
# win.bind_all("<Button-1>", hello)
# win.mainloop()


# def on_off():
#     global button
#     #state = button["text"]
#     state = button.cget("text")
#     if state == "ON":
#         state = "OFF"
#     else:
#         state = "ON"
#     #button["text"] = state
#     button.config(text=state)
#
#
# button = tk.Button(win, text="OFF", command=on_off)
# button.place(x=50, y=100, width=100)

# label_1 = tk.Label(win, text="Quick brown fox jumps over the lazy dog")
# label_1.grid(column=0, row=0)
# label_2 = tk.Label(win, text="Quick brown fox jumps over the lazy dog", font=("Times", "12"))
# label_2.grid(column=0, row=1)
# label_3 = tk.Label(win, text="Quick brown fox jumps over the lazy dog", font=("Arial", "16", "bold"))
# label_3.grid(column=0, row=2)

# button_1 = tk.Button(win, text="Ordinary button")
# button_1.pack()
# button_2 = tk.Button(win, text="Exceptional button")
# button_2.pack()
# button_2["borderwidth"] = 10
# button_2["highlightthickness"] = 10
# button_2["padx"] = 10
# button_2["pady"] = 5
# button_2["underline"] = 1
#
# button_2.config(bg ="#000000")
# button_2.config(fg ="yellow")
# button_2.config(activeforeground ="#FF0000")
# button_2.config(activebackground ="green")

# button_1 = tk.Button(win, text="Regular button")
# button_1["anchor"] = 'e'
# button_1["width"] = 20  # pixels!
# button_1.pack()
#
# button_2 = tk.Button(win, text="Another button")
# button_2["anchor"] = 'sw'
# button_2["width"] = 20
# button_2["height"] = 3  # rows
# button_2.pack()

# label_1 = tk.Label(win, height=3, text="arrow", cursor="arrow")
# label_1.pack()
# label_2 = tk.Label(win, height=3, text="clock", cursor="clock")
# label_2.pack()
# label_3 = tk.Label(win, height=3, text="heart", cursor="heart")
# label_3.pack()

# cursor_types = ['X_cursor','arrow','based_arrow_down','based_arrow_up','boat','bogosity','bottom_left_corner','bottom_right_corner','bottom_side','bottom_tee','box_spiral','center_ptr','circle','clock','coffee_mug','cross']
# cursor_types = ['cross_reverse','crosshair','diamond_cross','dot','dotbox','double_arrow','draft_large','draft_small','draped_box','exchange','fleur','gobbler','gumby','hand1','hand2','heart','icon','iron_cross','left_ptr']
#cursor_types = ['left_side','left_tee','leftbutton','ll_angle','lr_angle','man','middlebutton','mouse','pencil','pirate','plus','question_arrow','right_ptr','right_side','right_tee','rightbutton','rtl_logo','sailboat']
#cursor_types = ['sb_down_arrow','sb_h_double_arrow','sb_left_arrow','sb_right_arrow','sb_up_arrow','sb_v_double_arrow','shuttle','sizing','spider','spraycan','star','target','tcross','top_left_arrow','top_left_corner']
#cursor_types = ['top_right_corner','top_side','top_tee','trek','ul_angle','umbrella','ur_angle','watch','xterm']
#
# for cursor in cursor_types:
#     var = tk.Label(win, height=3, text=cursor, cursor=cursor)
#     var.pack()
#

# def blink():
#     global is_white
#     if is_white:
#         color = 'black'
#     else:
#         color = 'white'
#     is_white = not is_white
#     frame.config(bg=color)
#     frame.after(100, blink)
#
#
# is_white = True
# frame = tk.Frame(win, width=200, height=100, bg='white')
# frame.after(100, blink)
# frame.pack()


# def suicide():
#     frame.destroy()
#
#
# frame = tk.Frame(win, width=200, height=100, bg='green')
# button = tk.Button(frame, text="I'm a frame's child")
# button.place(x=10, y=10)
# frame.after(5000, suicide)
# frame.pack()

# def flip_focus():
#     if win.focus_get() is button_1:
#         button_2.focus_set()
#     else:
#         button_1.focus_set()
#     win.after(1000, flip_focus)
#
# button_1 = tk.Button(win, text="First")
# button_1.pack()
# button_2 = tk.Button(win, text="Second")
# button_2.pack()
# win.after(1000, flip_focus)

def r_observer(*args):
    print("Reading")


def w_observer(*args):
    print("Writing")


variable = tk.StringVar()
variable.set("abc")

r_obsid = variable.trace("r", r_observer)
w_obsid = variable.trace("w", w_observer)

variable.set(variable.get() + 'd')  # read followed by write
variable.trace_vdelete("r", r_obsid)

variable.set(variable.get() + 'e')
variable.trace_vdelete("w", w_obsid)

variable.set(variable.get() + 'f')

print(variable.get())

win.mainloop()
