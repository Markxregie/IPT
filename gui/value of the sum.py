import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Value of the Sum")


label1 = tkinter.Label(window, text = "SUM OF N")
label1.pack()

ttk.Label(window, text = "Enter an Integer",).grid( column = 0, row = 15, padx = 10, pady =25)

textbox1 = tkinter.Entry(window)
textbox1.pack()



window.mainloop()