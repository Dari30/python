import tkinter


def set_answer(v):
    entry_answer.delete(0, "end")
    entry_answer.insert(0, str(v))


def add():
    set_answer(get_n1() + get_n2())


def get_n2():
    return int(entry2.get())


def get_n1():
    return int(entry.get())


def minus():
    n1 = int(entry.get())
    n2 = int(entry2.get())
    set_answer(n1 - n2)


def divide():
    n1 = int(entry.get())
    n2 = int(entry2.get())
    set_answer(n1/n2)


def mult():
    n1 = int(entry.get())
    n2 = int(entry2.get())
    set_answer(n1*n2)

window = tkinter.Tk()
window.configure(bg="blue")
window.title("Calculator")
window.geometry("300x300")
label = tkinter.Label(master=window, text="1st number", bg="black", fg="white")
label.place(x=90, y=30)
label2 = tkinter.Label(master=window, text="2nd number", bg="black", fg="white")
label2.place(x=90, y=70)
label3 = tkinter.Label(master=window, text="3rd number", bg="black", fg="white")
label3.place(x=90, y=200)
entry = tkinter.Entry(window, width=3, bg="black", fg="white")
entry.place(x=90, y=50)
entry2 = tkinter.Entry(window, bg="black", fg="white")
entry2.place(x=90, y=90,width=100)
entry_answer = tkinter.Entry(window, bg="black", fg="white")
entry_answer.place(x=90, y=220)
button_plus = tkinter.Button(window, text="+", command=add, bg="black", fg="white")
button_plus.place(x=90, y=150)
button_times = tkinter.Button(window, text="*", command=mult, bg="black", fg="white")
button_times.place(x=180, y=150)
button_minus = tkinter.Button(window, text="-", command=minus, bg="black", fg="white")
button_minus.place(x=180, y=180)
button_divide = tkinter.Button(window, text="/", command=divide, bg="black", fg="white")
button_divide.place(x=90, y=180)
window.mainloop()
print("Hello")
