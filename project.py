import tkinter
from tkinter import *

root = Tk()
root.title("TO DO LIST")
root.geometry("400x600+400+100")
root.resizable(False, False)


def on_hover(event):
    event.widget.configure(bg="#32405b")


def on_default(event):
    event.widget.configure(bg="#5a95ff")


task_list = []


def open_txt_file():
    try:
        global task_list
        with open("taskList.txt", "r") as textFile:
            tasks = textFile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listBox.insert(END, task)
    except:
        file = open("taskList.txt", "w")
        file.close()


def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("taskList.txt", 'a') as taskFile:
            taskFile.write(f"\n{task}")
        task_list.append(task)
        listBox.insert(END, task)


def deleteFile():
    global task_list
    task = str(listBox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("taskList.txt", 'w') as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")
        listBox.delete(ANCHOR)


# icon
image_icon = PhotoImage(file="to-do-list.png")
root.iconphoto(False, image_icon)
# topBar
label = Label(root, bg="#32405b", width=100, height=4)
label.pack()
dockImage = PhotoImage(file="dots.png")
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)
noteImage = PhotoImage(file="to-do-list.png")
Label(root, image=noteImage, bg="#32405b").place(x=340, y=25)

heading = Label(root, text="ALL TASK", bg="#32405b",
                font="arial 20 bold", fg="white")
heading.place(x=130, y=20)

# main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=150)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold",
                bg="#5a95ff", width=6, fg="#fff", bd=0, cursor="hand2", command=addTask)
button.bind('<Enter>', on_hover)
button.bind('<Leave>', on_default)
button.place(x=300, y=0)

# List Box
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(150, 0))
listBox = Listbox(frame1, font='arial 12', width=40, height=16,
                  bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listBox.pack(side="left", fill="both", padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)
listBox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listBox.yview)
open_txt_file()
# delete
Delete_button = PhotoImage(file="trash-bin.png")
Button(root, image=Delete_button, bd=0,
       command=deleteFile).pack(side=BOTTOM, pady=13)
root.mainloop()
