import random
import tkinter as tk

def compchoice():
    n = random.randint(1, 3)
    if n == 1:
        return 'rock'
    elif n == 2:
        return 'paper'
    else:
        return 'scissors'

def gamelogic(cc, uc):
    if cc == uc:
        return "Draw"
    if cc == 'rock' and uc == 'paper':
        return "User win!!"
    elif cc == 'paper' and uc == 'scissors':
        return "User win!!"
    elif cc == 'scissors' and uc == 'rock':
        return "User win!!"
    else:
        return "Computer win!"

def play_game(choice):
    cmpChoice = compchoice()
    computer_choice.set("Computer choice: " + cmpChoice)
    result = gamelogic(cmpChoice, choice)
    game_result.set(result)

root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Set the window size to 500x500 and make it unscalable
root.geometry("300x200")
root.resizable(False, False)

computer_choice = tk.StringVar()
game_result = tk.StringVar()

label = tk.Label(root, text="Enter your choice:")
rock_button = tk.Button(root, text="Rock", command=lambda: play_game('rock'))
paper_button = tk.Button(root, text="Paper", command=lambda: play_game('paper'))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game('scissors'))
result_label = tk.Label(root, textvariable=game_result)
computer_label = tk.Label(root, textvariable=computer_choice)

label.pack()
rock_button.pack()
paper_button.pack()
scissors_button.pack()
result_label.pack()
computer_label.pack()

root.mainloop()
