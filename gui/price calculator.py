import tkinter as tk

def calculate_total():
    subtotal = 0
    tax_rate = 0.07

    # Bagel prices
    if bagel.get() == 1:
        subtotal += 1.25
    elif bagel.get() == 2:
        subtotal += 1.50

    # Topping prices
    if top1.get():
        subtotal += 0.50
    if top2.get():
        subtotal += 0.25
    if top3.get():
        subtotal += 0.75
    if top4.get():
        subtotal += 0.75
    if top5.get():
        subtotal += 0.75

    # Coffee prices
    if coffee.get() == 2:
        subtotal += 1.25
    elif coffee.get() == 3:
        subtotal += 2.00
    elif coffee.get() == 4:
        subtotal += 1.75

    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount

    subtotal_var.set(f"${subtotal:.2f}")
    tax_var.set(f"${tax_amount:.2f}")
    total_var.set(f"${total:.2f}")

def reset_form():
    bagel.set(0)
    top1.set(0)
    top2.set(0)
    top3.set(0)
    top4.set(0)
    top5.set(0)
    coffee.set(1)
    subtotal_var.set("")
    tax_var.set("")
    total_var.set("")

# Create main window
window = tk.Tk()
window.title("Bagel and Coffee Price Calculator")
window.geometry("500x600")

# Title
tk.Label(window, text="Brandi's Bagel House", font=("Georgia bold", 20)).pack(pady=10)

# Frame for the left side (Bagels and Toppings)
left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT, padx=20, pady=20, anchor="n")

# Bagel options
tk.Label(left_frame, text="Pick a Bagel", font=("Georgia bold", 10)).grid(row=0, column=0, sticky="w")
bagel = tk.IntVar()
tk.Radiobutton(left_frame, text="White ($1.25)", variable=bagel, value=1).grid(row=1, column=0, sticky="w")
tk.Radiobutton(left_frame, text="Whole Wheat ($1.50)", variable=bagel, value=2).grid(row=2, column=0, sticky="w")

# Toppings options
tk.Label(left_frame, text="Pick Your Toppings", font=("Georgia bold", 10)).grid(row=3, column=0, sticky="w", pady=(10,0))
top1 = tk.IntVar()
top2 = tk.IntVar()
top3 = tk.IntVar()
top4 = tk.IntVar()
top5 = tk.IntVar()
tk.Checkbutton(left_frame, text="Cream Cheese ($0.50)", variable=top1).grid(row=4, column=0, sticky="w")
tk.Checkbutton(left_frame, text="Butter ($0.25)", variable=top2).grid(row=5, column=0, sticky="w")
tk.Checkbutton(left_frame, text="Blueberry Jam ($0.75)", variable=top3).grid(row=6, column=0, sticky="w")
tk.Checkbutton(left_frame, text="Raspberry Jam ($0.75)", variable=top4).grid(row=7, column=0, sticky="w")
tk.Checkbutton(left_frame, text="Peach Jelly ($0.75)", variable=top5).grid(row=8, column=0, sticky="w")

# Frame for the right side (Coffee and Prices)
right_frame = tk.Frame(window)
right_frame.pack(side=tk.LEFT, padx=15, pady=15 ,anchor="n")

# Coffee options
tk.Label(right_frame, text="Want Coffee with That?", font=("Georgia bold", 10)).grid(row=0, column=0, sticky="w")
coffee = tk.IntVar(value=1)
tk.Radiobutton(right_frame, text="None", variable=coffee, value=1).grid(row=1, column=0, sticky="w")
tk.Radiobutton(right_frame, text="Regular Coffee ($1.25)", variable=coffee, value=2).grid(row=2, column=0, sticky="w")
tk.Radiobutton(right_frame, text="Cappuccino ($2.00)", variable=coffee, value=3).grid(row=3, column=0, sticky="w")
tk.Radiobutton(right_frame, text="Cafe au Lait ($1.75)", variable=coffee, value=4).grid(row=4, column=0, sticky="w")

# Price display
# Price display
tk.Label(right_frame, text="Prices", font=("Georgia bold", 10)).grid(row=5, column=0, sticky="w", pady=(20, 0))

# Subtotal
tk.Label(right_frame, text="Subtotal:").grid(row=6, column=0, sticky="w", pady=2)
subtotal_var = tk.StringVar()
tk.Entry(right_frame, textvariable=subtotal_var, state='readonly').grid(row=6, column=1, sticky="w", pady=2)

# Tax
tk.Label(right_frame, text="Tax:").grid(row=7, column=0, sticky="w", pady=2)
tax_var = tk.StringVar()
tk.Entry(right_frame, textvariable=tax_var, state='readonly').grid(row=7, column=1, sticky="w", pady=2)

# Total
tk.Label(right_frame, text="Total:").grid(row=8, column=0, sticky="w", pady=2)
total_var = tk.StringVar()
tk.Entry(right_frame, textvariable=total_var, state='readonly').grid(row=8, column=1, sticky="w", pady=2)

# Buttons
button_frame = tk.Frame(right_frame)
button_frame.grid(row=9, column=0, columnspan=2, pady=20)
tk.Button(button_frame, text="Calculate Total", command=calculate_total).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Reset Form", command=reset_form).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Exit", command=window.quit).pack(side=tk.LEFT, padx=5)

window.mainloop()