import tkinter as tk

window = tk.Tk()

# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")

# button_1.place(x=10, y=10, width=150)
# button_2.place(x=20, y=40)
# button_3.place(x=30, y=70, height=50)

#button_1.grid(row=0, column=0)
#button_2.grid(row=1, column=1)
#button_3.grid(row=2, column=2)

#button_3.grid(row=2, column=0, columnspan=2)

#button_1.pack()
#button_1.pack(side=tk.RIGHT)

# button_1.pack(side=tk.RIGHT, fill=tk.Y)
# button_2.pack()
# button_3.pack()

#button = tk.Button(window, text="Button #1", bg="red", fg="yellow")

# button = tk.Button(window, text="Button #1",
#                    bg="MediumPurple",
#                    fg="LightSalmon",
#                    activeforeground="LavenderBlush",
#                    activebackground="HotPink")

button = tk.Button(window, text="Button #1",
                   bg="#9370DB",
                   fg="#FFA07A",
                   activeforeground="#FFF0F5",
                   activebackground="#FF69B4")

button.pack()

window.mainloop()
