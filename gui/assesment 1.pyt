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
        label1.config(text="Please enter a positive integer")

window = tk.Tk()
window.title("Summation")

label = ttk.Label(window, text="Enter an integer: ", font=("Helvetica", 10))
label.pack(pady=(50, 10))

entry = tk.Entry(window, width=20)
entry.pack()

button = tk.Button(window, text="Validate", command=calculate)
button.pack(pady=10)

label1 = tk.Label(window, text="")
label1.pack()

window.geometry("300x200")
window.mainloop()
