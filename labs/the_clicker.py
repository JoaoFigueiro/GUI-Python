import tkinter as tk
from random import randint


def tick():
    global clock_time, after_id, clock
    if clock_started:
        clock_time += 1
        clock["text"] = str(clock_time)
        after_id = clock.after(1000, tick)


def disable_button(self):
    global win, values, clock_started, clock

    if not clock_started:
        clock_started = True
        clock.after(1000, tick)

    if int(self.widget.cget('text')) <= int(min(values)):
        self.widget.config(state=tk.DISABLED)
        values.remove(int(self.widget.cget('text')))

    if not values:
        clock_started = False
        clock.after_cancel(after_id)

win = tk.Tk()
win.title("Clicker")

values = []
buttons = []

for row in range(5):
    for col in range(5):
        value = randint(1, 999)

        while value in values:
            value = randint(1, 999)

        values.append(value)

        button = tk.Button(
            win,
            text=str(value),
        )

        button.grid(row=row, column=col)
        button.bind("<Button-1>", disable_button)

        buttons.append(button)

clock_time = 0
clock_started = False

clock = tk.Label(win, text=str(clock_time))
clock.grid(row=5, column=2)

win.mainloop()