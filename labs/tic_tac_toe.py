import tkinter as tk
from tkinter import messagebox
from random import randrange


def close_window(_event):
    win.destroy()


def check_result(player):
    for row in range(3):
        if all(button.cget("text") == player for button in board[row]):
            messagebox.showinfo("", f"Player {player} win")
            win.destroy()

        if all(button.cget("text") == player for button in [board[col][row] for col in range(3)]):
            messagebox.showinfo("", f"Player {player} win")
            win.destroy()

        if all(button.cget("text") == player for button in [board[index][index] for index in range(3)]):
            messagebox.showinfo("", f"Player {player} win")
            win.destroy()

        if all(button.cget("text") == player for button in [board[index][2-index] for index in range(3)]):
            messagebox.showinfo("", f"Player {player} win")
            win.destroy()


def click(self):
    global win

    self.widget.config(text='O', fg='green', activeforeground='green')

    check_result('X')
    check_result('O')

    valid_options = [
        button
        for button, content in win.children.items()
        if content.cget('text') not in ['O', 'X']
    ]

    choice = randrange(0, len(valid_options))
    chosen_button = valid_options[choice]

    win.children.get(chosen_button).config(
        text='X', fg='red', activeforeground='red'
    )


win = tk.Tk()
win.title("TicTacToe")
win.bind('<Control-w>', close_window)

board = [[None for c in range(3)] for r in range(3)]

for col in range(3):
    for row in range(3):
        btn = tk.Button(win, width=4, height=1, font=("Arial", 30, "bold"), text="")
        btn.bind("<Button-1>", click)
        btn.grid(column=col, row=row)
        board[row][col] = btn

win.mainloop()

# the computer (i.e., your program) plays 'X', and Xes are always red,
# the user (e.g., you) plays 'O', and Os are always green,
# the board consists of 9 tiles, and the tile role is played by a button,
# the first move belongs to the computer - it always puts its first 'X' in the middle of the board,
# the user enters her/his move by clicking the chosen tile (clicking the tiles which are not free is ineffective)
# the program checks if the game over conditions are met, and if the game is over, a message box is displayed announcing the winner,
# otherwise the computer responds with its move and the check is repeated,
# use random to generate the computer's moves.