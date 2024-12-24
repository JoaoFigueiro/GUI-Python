import tkinter as tk


def on_off():
    global accessible
    if accessible == tk.DISABLED:
        accessible = tk.ACTIVE
    else:
        accessible = tk.DISABLED
    sub_menu.entryconfigure(1, state=accessible)


window = tk.Tk()

accessible = tk.DISABLED

menu = tk.Menu(window)
sub_menu = tk.Menu(menu, tearoff=0)

window.config(menu=menu)
menu.add_cascade(label="Menu", menu=sub_menu)

sub_menu.add_command(label="On/Off", command=on_off)
sub_menu.add_command(label="Switch", state=tk.DISABLED)

window.mainloop()
