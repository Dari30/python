import tkinter as tk
import random
import tkinter.messagebox as tkm

def enter(e):
    global correct, incorrect
    if time == 0:
        if score_correct > score_incorrect:
            tkm.showinfo("Good result", "you are good at this game")
        else:
            tkm.showinfo("Bad result", "you are bad at this game")
        return
    if label_word["fg"] == entry.get():
        correct += 1
    else:
        incorrect += 1
    label_word["fg"] = random.choice(colors)
    label_word["text"] = random.choice(colors)
    score_correct["text"] = f"correct: {correct}"
    score_incorrect["text"] = f"incorrect: {incorrect}"



def time_t():
    global time
    if time == 0:
        tkm.showinfo("Game over", "You’ve run out of time")
        return
    time -= 1
    label_t["text"] = f"time left: {time}"
    label_t.after(1000, time_t)


window = tk.Tk()
window.title("write the color")
window.geometry("300x200")
correct = 0
incorrect = 0
colors = ["red", "blue", "green", "pink", "black", "yellow", "orange", "purple", "brown"]
time = 30

label = tk.Label(master=window, text="enter the color of the word not a word")
label.place(x=10, y=15)
score_correct = tk.Label(master=window, text=f"correct: {correct}")
score_correct.place(x=10, y=50)
score_incorrect = tk.Label(master=window, text=f"incorrect: {incorrect}")
score_incorrect.place(x=10, y=70)
label_word = tk.Label(master=window, text=random.choice(colors), font=("Calibri", 40))
label_word.place(x=10, y=85)
entry = tk.Entry(window)
entry.place(x=10, y=150)
label_t = tk.Label(window, text=f"time left: {time}")
label_t.after(1000, time_t)
label_t.place(x=10, y=175)
window.bind("<Return>", enter)
window.mainloop()
