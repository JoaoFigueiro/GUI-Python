import tkinter as tk
from tkinter import PhotoImage


window = tk.Tk()
window.title('Icon?')
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='logo.png'))
window.bind("&lt;Button-1&gt;", lambda e: window.destroy())
window.mainloop()
