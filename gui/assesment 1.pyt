import tkinter as tk
from tkinter import ttk

def calculate():
    n = entry.get()
    if n.isdigit():
        n = int(n)
        numbers_str = ""
        sum_value = 0
        for i in range(1, n + 1):
            if i == 1:
                numbers_str += str(i)
            else:
                numbers_str += " + " + str(i)
            sum_value += i
        label1.config(text=f"The sum is {numbers_str} = {sum_value}")
    else:
        label1.config(text="Please enter a Positive integer")

window = tk.Tk()
window.geometry("400x150")
window.title("Summation")

ttk.Label(window, text="Enter an integer: ", font=("Helvetica", 10)).grid(column=0, row=0, padx=10, pady=10)

entry = tk.Entry(window, width=20)
entry.grid(column=1, row=0)

button1 = tk.Button(window, text="Summation", command= calculate)
button1.grid(column=1, row=1, pady=10)

label1 = tk.Label(window, text="")
label1.grid(column=1, row=2)

window.mainloop()
