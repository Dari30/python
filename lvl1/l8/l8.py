import tkinter
def add():
    print("hello+")
    n1 = int(entry.get())
    n2 = int(entry2.get())
    entry_answer.delete(0, "end")
    entry_answer.insert(0,str(n1+n2))
def minus():
    print("hello+")
    n1 = int(entry.get())
    n2 = int(entry2.get())
    entry_answer.delete(0, "end")
    entry_answer.insert(0,str(n1-n2))
def divide():
    print("hello+")
    n1 = int(entry.get())
    n2 = int(entry2.get())
    entry_answer.delete(0, "end")
    entry_answer.insert(0,str(n1/n2))
def mult():
    print("hello*")
    n1 = int(entry.get())
    n2 = int(entry2.get())
    entry_answer.delete(0, "end")
    entry_answer.insert(0,str(n1*n2))
window = tkinter.Tk()
window.title("Calculator")
window.geometry("300x300")
entry = tkinter.Entry(window)
entry.place(x=90,y=50)
entry2 = tkinter.Entry(window)
entry2.place(x=90,y=90)
entry_answer = tkinter.Entry(window)
entry_answer.place(x=90,y=220)
button_plus = tkinter.Button(window, text="+", command=add)
button_plus.place(x=90,y=150)
button_times = tkinter.Button(window, text="*", command=mult)
button_times.place(x=180,y=150)
button_minus = tkinter.Button(window, text="-", command=minus)
button_minus.place(x=180,y=180)
button_divide = tkinter.Button(window, text="/", command=divide)
button_divide.place(x=90,y=180)
window.mainloop()
print("Hello")