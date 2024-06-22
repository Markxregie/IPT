import tkinter as tk
from tkinter import PhotoImage, messagebox

# Function to draw a rounded rectangle
def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1 + radius, y1,
        x1 + radius, y1,
        x2 - radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# Initialize the main window
window = tk.Tk()
window.title("Login")
window.geometry('1300x700')
window.configure(bg='#A9B498')  # Set outer background color
window.resizable(False, False)  # Disable window resizing


def login():
    username = "admin"
    password = "admin123"
    if name_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title='Login Success' , message =  'You successfuly logged in.')
    else:
        messagebox.showerror(title = 'Error', message = 'Invalid.')

# Create a canvas for the inner background with rounded corners
canvas = tk.Canvas(window, bg='#A9B498', highlightthickness=0)
canvas.place(x=25, y=25, width=1250, height=650)  # Fixed position and size
round_rectangle(canvas, 0, 0, 1250, 650, radius=50, fill='#CAD1B8')

# Create a frame for the login form on top of the canvas
login_frame = tk.Frame(window, bg='white', bd=2)
login_frame.place(x=450, y=150, width=400, height=400)  # Fixed position and size



# Title
title_label = tk.Label(login_frame, text="TRANSIENT", font=("Century Gothic", 16, 'bold'), bg='white', fg='#7B8C68')
title_label.place(relx=0.5, rely=0.20, anchor='center')

# Load the image for the rounded entry backgrounds
rounded_entry_bg = PhotoImage(file='Rectangle 1.png')

# Create and place the Name label and entry
name_label = tk.Label(login_frame, text="Name", bg='white', font=("Century Gothic", 10), fg='#7B8C68')
name_label.place(relx=0.34, rely=0.33, anchor='e')
name_entry_image = tk.Label(login_frame, image=rounded_entry_bg, border=0, bg='white')
name_entry_image.place(relx=0.5, rely=0.4, anchor='center')
name_entry = tk.Entry(login_frame, width=27, border=0, font=('bold', 11))
name_entry.place(relx=0.5, rely=0.4, anchor='center')

# Create and place the Password label and entry
password_label = tk.Label(login_frame, text="Password", font=("Century Gothic", 10), bg='white', fg='#7B8C68')
password_label.place(relx=0.31, rely=0.53, anchor='center')
password_entry_image = tk.Label(login_frame, image=rounded_entry_bg, border=0, bg='white')
password_entry_image.place(relx=0.5, rely=0.6, anchor='center')
password_entry = tk.Entry(login_frame, font=("Century Gothic", 12), width=24, border=0, show='*')
password_entry.place(relx=0.5, rely=0.6, anchor='center')

# Create and place the login button
round = PhotoImage(file='loh.png')
round_button = tk.Button(login_frame, image=round, border=0, command=login)
round_button.place(relx=0.5, rely=0.8, anchor='center')

# Run the main loop
window.mainloop()
