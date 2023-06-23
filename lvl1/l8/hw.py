import tkinter
def write():
    print(f"You wrote: {entry.get()}")

window = tkinter.Tk()
window.title("Calculator")
window.geometry("300x300")
entry = tkinter.Entry(window)
entry.place(x=90, y=50)

button_answer = tkinter.Button(window, text="+", command=write)
button_answer.place(x=150, y=150)
window.mainloop()