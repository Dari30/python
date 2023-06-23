import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tkm


def new_file():
    global file_name
    if tkm.askokcancel("","your text will be deleted, because it's not saved, are you sure?"):
        text.delete(1.0, "end")
        file_name = ""
        window.title(f"{file_name}Notepad")


def open_file():
    global file_name
    file_name = tfd.askopenfilename()
    with open(file_name, encoding="utf-8") as file:
        text.insert(1.0, file.read())
        window.title(f"{file_name}Notepad")

def save_as_file():
    global file_name
    file_name = tfd.asksaveasfilename()
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(text.get(1.0, "end"))
        window.title(f"{file_name}Notepad")


def save_file():
    if file_name == "":
        save_as_file()
    else:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(text.get(1.0, "end"))



window = tk.Tk()
file_name = ""
window.geometry("400x400")
window.title(f"{file_name}Notepad")
text = tk.Text(window, wrap="word")
text.place(x=0, y=0, relwidth=1, relheight=1)
main_menu = tk.Menu(window, )
window.configure(menu=main_menu)
file_menu = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="file", menu=file_menu, )
new_file_icon = tk.PhotoImage(file="new_file.gif")
file_menu.add_command(label="new", image=new_file_icon, compound="left", command=new_file)
open_file_icon = tk.PhotoImage(file="open_file.gif")
file_menu.add_command(label="open", image=open_file_icon, compound="left", command=open_file)
save_file_icon = tk.PhotoImage(file="save_file.gif")
file_menu.add_command(label="save", image=save_file_icon, compound="left", command=new_file)
file_menu.add_command(label="save as", image=save_file_icon, compound="left", command=save_as_file)
window.mainloop()
