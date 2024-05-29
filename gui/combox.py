import tkinter as tk
from tkinter import ttk

def buttonclicked():
    strSelected = "You have selected " + cbolang.get()
    lbloutput.config(text=strSelected)

window = tk.Tk()
window.geometry("400x150")

ttk.Label(window, text="Jollibee Menu: ", font=("Helvetica", 10)).grid(column=0, row=0, padx=10, pady=25)

n = tk.StringVar()

cbolang = ttk.Combobox(window, width=30, textvariable=n)
cbolang['value'] = ("burger", "fries", "chimken")

cbolang.grid(column=1, row=0)

cbolang.current(0)

button1 = tk.Button(window, text="click", command=buttonclicked)
button1.grid(column=1, row=1)

lbloutput = tk.Label(window, text="")
lbloutput.grid(column=1, row=2)

window.mainloop()
