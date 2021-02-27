import tkinter
from tkinter import DISABLED, ACTIVE

player1 = True


def new_game():
    """Start a new game - enable all buttons, set all values to whitespace"""
    button0.config(state=ACTIVE, text="")
    button1.config(state=ACTIVE, text="")
    button2.config(state=ACTIVE, text="")
    button3.config(state=ACTIVE, text="")
    button4.config(state=ACTIVE, text="")
    button5.config(state=ACTIVE, text="")
    button6.config(state=ACTIVE, text="")
    button7.config(state=ACTIVE, text="")
    button8.config(state=ACTIVE, text="")


def button_work(button):
    """Use the global variable player1 in order to decide on whether it's a circle or X, 
    then disable the button so it cannot be pressed again."""
    
    global player1

    if player1:
        button.config(text="O")
        player1 = False
        button.config(state=DISABLED)

    else:
        button.config(text="X")
        player1 = True
        button.config(state=DISABLED)


def game_logic(button):
    """Use the button number to determine winning logic for the game."""
    if button0["text"] == "X" and button1["text"] == "X" and button2["text"] == "X" or button3["text"] == "X" and button4["text"] == "X" and button5["text"] == "X" or button6["text"] == "X" and button7["text"] == "X" and button8["text"] == "X" or \
            button0["text"] == "X" and button3["text"] == "X" and button6["text"] == "X" or button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or \
                button0["text"] == "X" and button4["text"] == "X" and button8["text"] == "X" or button2["text"] == "X" and button4["text"] == "X" and button6["text"] == "X":
        result_label.config(text="P2 Wins!")

    if button0["text"] == "O" and button1["text"] == "O" and button2["text"] == "O" or button3["text"] == "O" and button4["text"] == "O" and button5["text"] == "O" or button6["text"] == "O" and button7["text"] == "O" and button8["text"] == "O" or \
            button0["text"] == "O" and button3["text"] == "O" and button6["text"] == "O" or button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or \
            button0["text"] == "O" and button4["text"] == "O" and button8["text"] == "O" or button2["text"] == "O" and button4["text"] == "O" and button6["text"] == "O":
        result_label.config(text="P1 Wins!")


root = tkinter.Tk()
root.title("TicTacToe")
root.geometry("300x300")
root.resizable(0, 0)

root.config(bg="black")

# Create and pack frames
title_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
options_frame = tkinter.Frame(root)
title_frame.pack(padx=3, pady=3)
button_frame.pack(padx=3, pady=3)
options_frame.pack(padx=3, pady=3)

# Create title
tkinter.Label(title_frame, text="Tic Tac Toe", font=("Arial", 20)).pack()

# Create buttons
button0 = tkinter.Button(button_frame, font=("Arial", 25), width=3, command=lambda:[button_work(button0), game_logic(button0)])
button1 = tkinter.Button(button_frame, font=("Arial", 25), width=3, command=lambda:[button_work(button1), game_logic(button1)])
button2 = tkinter.Button(button_frame, font=("Arial", 25), width=3, command=lambda:[button_work(button2), game_logic(button2)])
button3 = tkinter.Button(button_frame, font=("Arial", 25), width=3, command=lambda:[button_work(button3), game_logic(button3)])
button4 = tkinter.Button(button_frame, font=("Arial", 25), width=3, command=lambda:[button_work(button4), game_logic(button4)])
button5 = tkinter.Button(button_frame, font=("Arial", 25), width=3, command=lambda:[button_work(button5), game_logic(button5)])
button6 = tkinter.Button(button_frame, font=("Arial", 25), width=3, command=lambda:[button_work(button6), game_logic(button6)])
button7 = tkinter.Button(button_frame, font=("Arial", 25), width=3, command=lambda:[button_work(button7), game_logic(button7)])
button8 = tkinter.Button(button_frame, font=("Arial", 25), width=3, command=lambda:[button_work(button8), game_logic(button8)])

# Grid buttons
button0.grid(row=0, column=0)
button1.grid(row=0, column=1)
button2.grid(row=0, column=2)
button3.grid(row=1, column=0)
button4.grid(row=1, column=1)
button5.grid(row=1, column=2)
button6.grid(row=2, column=0)
button7.grid(row=2, column=1)
button8.grid(row=2, column=2)

result_label = tkinter.Label(options_frame, text="Game in Progress!", width=15)
result_label.grid(row=0, column=0, padx=2, pady=2)

new_game_button = tkinter.Button(options_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=1, padx=2, pady=2)

root.mainloop()
