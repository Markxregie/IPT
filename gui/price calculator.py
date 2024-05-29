import tkinter
import tkinter as tk
window = tkinter.Tk()

window.title("Price Calculator")
window.geometry("500x600")

label1 = tkinter.Label(window,text= "Brandi's Bagel House", font= ("Georgia", 20)).grid(padx = 130, pady= 10)

label2 = tkinter.Label(window,text= "Pick a Bagel", font= ("Georgia", 10)).grid(column = 0, row = 15, padx = 40, pady=5, sticky = "w" )


bagel = tkinter.IntVar()

tkinter.Radiobutton(window,text = "White ($1.50)",padx = 20, variable=bagel,value=1).grid(sticky="w")

tkinter.Radiobutton(window,text = "Whole Wheat ($1.25)",padx = 20, variable=bagel,value=2).grid(sticky="w")

label3 = tk.Label(window, text="Pick Your Toppings").grid(padx=37, pady=10, sticky = "w")

top1 = tkinter.IntVar()

toppings = tkinter.Checkbutton(window, text="Cream Cheese ($.50)",padx = 20, variable=top1).grid(sticky="w")
toppings = tkinter.Checkbutton(window, text="Butter ($.50)", padx = 20,variable=top1).grid(sticky="w")
toppings = tkinter.Checkbutton(window, text="Blueberry Jam ($.50)",padx = 20, variable=top1).grid(sticky="w")
toppings = tkinter.Checkbutton(window, text="Raspberry Jam ($.50)",padx = 20, variable=top1).grid(sticky="w")
toppings = tkinter.Checkbutton(window, text="Peach Jelly ($.50)",padx = 20, variable=top1).grid(sticky="w")


window.mainloop()