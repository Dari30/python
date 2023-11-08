import tkinter as tk
import tkinter.messagebox as tkm
import random


def check(e):
    global attempts, won

    if attempts == 0 or won:
        button_game["state"]=tk.NORMAL
        return
    if number > int(entry.get()):
        attempts -= 1
        label_text["text"] = "the nuber is greater"
        entry["text"] = " "
    if number < int(entry.get()):
        label_text["text"] = "the nuber is less"
        attempts -= 1
        entry["text"] = " "
    if number == int(entry.get()):
        label_text["text"] = "the nuber is correct"
        won = True
    label_attempts["text"] = f"attempts {attempts}"


window = tk.Tk()
window.title("guess the number")
window.geometry("300x300")
attempts = 7
won = False
number = random.randint(1, 100)
label_text = tk.Label(window, text=f"guess the number from 0 to 100")
label_text.place(x=80, y=15)
label_attempts = tk.Label(window, text=f"attempts {attempts}")
label_attempts.place(x=110, y=30)
entry = tk.Entry(window)
entry.place(x=80, y=50)
button_check = tk.Button(window, command=lambda: check("press"), text="check")
button_check.place(x=110, y=70)
button_game = tk.Button(window, text="new game")
button_game.place(x=110, y=90)
button_game["state"]=tk.DISABLED
window.bind("<Return>", check)

window.mainloop()
