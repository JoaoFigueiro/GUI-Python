import tkinter as tk


window = tk.Tk()
canvas = tk.Canvas(window, width=200, height=200, bg='white')
# canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380, arrow=tk.BOTH, fill='red', smooth=True, width=3)
# canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380)
#canvas.create_rectangle(200, 100, 300, 300, outline='white', width=5, fill='red')
#canvas.create_polygon(20, 380, 200, 68, 380, 380, outline='red', width=5, fill='yellow')
# canvas.create_oval(100, 100, 300, 200, outline='red', width=20, fill='white')

# canvas.create_arc(10, 100, 380, 300, outline='red', width=5)
# canvas.create_arc(10, 100, 380, 300, outline='blue', width=5,
#                   style=tk.CHORD, start=90, fill='white')
# canvas.create_arc(10, 100, 380, 300, outline='green', width=5,
#                   style=tk.ARC, start=180, extent=180)
#
# canvas.create_text(200, 200, text="Mary\nhad\na\nlittle\nlamb",
#                    font=("Arial","40","bold"),
#                    justify=tk.CENTER,
#                    fill='white')

image = tk.PhotoImage(file='logo.png')
canvas.create_image(50, 50, image=image)

button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()

window.mainloop()
