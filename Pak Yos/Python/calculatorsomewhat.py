#PYTHON CALCULATOR (WITH GUI OMGG YYOURE SO GOOS AT THINGS WIJNDKFNDJKFNJKDNFJ)

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import numexpr
import re

root = tk.Tk()
root.title("somewhat of a calculator")
root.geometry("300x200")

def convert_percent(expression):
    expression = re.sub(r"(\d+(\.\d+)?)%", r"(\1/100)", expression)
    expression = re.sub(r"(\d+(\.\d+)?)\s*([\+\-])\s*(\(\d+(\.\d+)?/100\))", 
                        r"\1 \3 (\4 * \1)", expression)
    return expression

def fix_log_base(expression):
    print("done")
    expression = expression.replace("log(", "log10(")
    return expression

def backspace():
    current_text = calcentry.get()
    calcentry.delete(len(current_text) - 1)

def clearentry():
    calcentry.delete(0, END)

def calculate(variable):
    safevar = fix_log_base(variable)
    safevar = convert_percent(safevar)
    equation = numexpr.evaluate(safevar)
    write(equation)

def write(entry):
    clearentry()
    calcentry.insert(tk.END, entry)

def update(event):
    variable = input_variable.get()
    calculate(variable)

def update_button():
    if input_variable.get().strip():  # Check if entry is not empty
        acbtn.config(command=backspace, text="CE")
    else:
        acbtn.config(command=clearentry, text="AC")

input_variable = StringVar()
input_variable.trace_add("write", lambda *args: update_button())
calcentry = tk.Entry(root,textvariable=input_variable,width=15, font=("Arial", 16), justify="right")
calcentry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
calcentry.bind("<Return>", update)

buttons = [
    "(", ")", "%", "AC",
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

def add_to_entry(value):
    calcentry.insert(tk.END, value)

for index, label in enumerate(buttons):
    row = (index + 4) // 4 
    col = index % 4
    if buttons[index] == "=":
        btn = tk.Button(root, text=label, width=5, height=2,
                    command=lambda: update(None))
        btn.grid(row=row, column=col, padx=5, pady=5)
    elif buttons[index] == "AC":
        acbtn = tk.Button(root, text=label, width=5, height=2,
                    command=clearentry)
        acbtn.grid(row=row, column=col, padx=5, pady=5)
    else:
        btn = tk.Button(root, text=label, width=5, height=2,
                        command=lambda v=label: add_to_entry(v))
        btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()