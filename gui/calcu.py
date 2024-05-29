import tkinter as tk
from tkinter import messagebox

def add():
    operand1 = entry1.get()
    operand2 = entry2.get()
    if is_valid_number(operand1) and is_valid_number(operand2):
        result = float(operand1) + float(operand2)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
    else:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def subtract():
    operand1 = entry1.get()
    operand2 = entry2.get()
    if is_valid_number(operand1) and is_valid_number(operand2):
        result = float(operand1) - float(operand2)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
    else:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def multiply():
    operand1 = entry1.get()
    operand2 = entry2.get()
    if is_valid_number(operand1) and is_valid_number(operand2):
        result = float(operand1) * float(operand2)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
    else:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def divide():
    operand1 = entry1.get()
    operand2 = entry2.get()
    if is_valid_number(operand1) and is_valid_number(operand2):
        if float(operand2) != 0:
            result = float(operand1) / float(operand2)
            entry_result.delete(0, tk.END)
            entry_result.insert(0, str(result))
        else:
            messagebox.showerror("Math Error", "Division by zero")
    else:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def mod():
    operand1 = entry1.get()
    operand2 = entry2.get()
    if is_valid_number(operand1) and is_valid_number(operand2):
        if float(operand2) != 0:
            result = float(operand1) % float(operand2)
            entry_result.delete(0, tk.END)
            entry_result.insert(0, str(result))
        else:
            messagebox.showerror("Math Error", "Division by zero")
    else:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry_result.delete(0, tk.END)

def exit_app():
    root.destroy()

def is_valid_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

root = tk.Tk()
root.title("Simple Calculator")

# Creating the layout
frame = tk.Frame(root)
frame.pack(pady=10)

# Title
title = tk.Label(frame, text="Simple Calculator", font=("Arial", 14))
title.grid(row=0, column=0, columnspan=3, pady=10)

# Operators
operators_frame = tk.LabelFrame(frame, text="Operators")
operators_frame.grid(row=1, column=0, padx=10, pady=10)

btn_add = tk.Button(operators_frame, text="+", width=5, command=add)
btn_add.grid(row=0, column=0, pady=2)

btn_subtract = tk.Button(operators_frame, text="-", width=5, command=subtract)
btn_subtract.grid(row=0, column=1, pady=2)

btn_multiply = tk.Button(operators_frame, text="*", width=5, command=multiply)
btn_multiply.grid(row=1, column=0, pady=2)

btn_divide = tk.Button(operators_frame, text="/", width=5, command=divide)
btn_divide.grid(row=1, column=1, pady=2)

btn_mod = tk.Button(operators_frame, text="Mod", width=11, command=mod)
btn_mod.grid(row=2, column=0, columnspan=2, pady=2)

# Operation details
details_frame = tk.LabelFrame(frame, text="Operation")
details_frame.grid(row=1, column=1, padx=10, pady=10)

tk.Label(details_frame, text="Operand 1:").grid(row=0, column=0, sticky=tk.W, pady=2)
entry1 = tk.Entry(details_frame)
entry1.grid(row=0, column=1, pady=2)

tk.Label(details_frame, text="Operand 2:").grid(row=1, column=0, sticky=tk.W, pady=2)
entry2 = tk.Entry(details_frame)
entry2.grid(row=1, column=1, pady=2)

tk.Label(details_frame, text="Result:").grid(row=2, column=0, sticky=tk.W, pady=2)
entry_result = tk.Entry(details_frame)
entry_result.grid(row=2, column=1, pady=2)

# Clear and Exit buttons
btn_clear = tk.Button(frame, text="Clear", width=10, command=clear)
btn_clear.grid(row=2, column=0, pady=10)

btn_exit = tk.Button(frame, text="Exit", width=10, command=exit_app)
btn_exit.grid(row=2, column=1, pady=10)

root.mainloop()
