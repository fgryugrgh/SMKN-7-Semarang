import tkinter as tk
from tkinter import *
from tkinter.ttk import *


test = tk.Tk()
test.title('test')
test.geometry("300x200")

def hello_world(event):
    label = tk.Label(test, text="hello world")
    label.pack()

button = tk.Button(test, text="click", command=hello_world)
button.pack()

def new_window(event):
    new = tk.Tk()
    new.title("new")
    new.geometry("300x200")
    newtext = tk.Label(new, text="hello")
    newtext.pack()
    frame2 = Frame(new, height = 100, width = 200)
    frame2.pack()
    frame2.bind("<Enter>", hello_world)


newwindow = tk.Button(test, text="new window", command=new_window)
newwindow.pack()


frame1 = Frame(test, height = 100, width = 200)
frame1.pack()
#frame1.bind("<Leave>", hello_world)

def entrytest(entry):
    label1 = tk.Label(test, text=str(entry))
    label1.pack()

def update(event):
    variable = input_variable.get()
    print(variable)
    entrytest(variable)

input_variable = StringVar()
entry = Entry(test, textvariable=input_variable)
entry.pack()
entry.bind("<Return>", update)
test.mainloop()