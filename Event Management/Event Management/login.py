import customtkinter as ctk
from tkinter import messagebox
from PIL import Image  

# Function to authenticate the user
def authenticate():
    username = name_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "admin123":
        messagebox.showinfo("Login Successful", "Welcome, admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Initialize the main window
app = ctk.CTk()
app.title("Transient Login")
app.geometry("1500x800")
app.configure(fg_color="#A3B18A")

# Create a central background frame (green color)
central_background_frame = ctk.CTkFrame(master=app, width=1400, height=700, corner_radius=10, fg_color="#B5C1A1")
central_background_frame.place(relx=0.5, rely=0.5, anchor='center')

# Create a frame for the login form on top of the central background frame
login_frame = ctk.CTkFrame(master=central_background_frame, width=360, height=500, corner_radius=10, fg_color="white")
login_frame.place_configure(width=400, height=450, relx=0.5, rely=0.5, anchor='center')

# Load and add the logo image
logo_image = ctk.CTkImage(Image.open("twitter.png"), size=(150, 150))
logo_label = ctk.CTkLabel(master=login_frame, image=logo_image, text="")
logo_label.grid(row=0, column=0, padx=125, pady=(20, 5))

# Add the title below the logo
title_label = ctk.CTkLabel(master=login_frame, text="TRANSIENT", font=("century gothic", 20, "bold"), text_color="black")
title_label.grid(row=1, column=0, padx=150, pady=(5, 5))

# Add input fields and labels
name_label = ctk.CTkLabel(master=login_frame, text="Name", font=("century gothic", 13, "bold"), text_color="black")
name_label.grid(row=2, column=0, padx=100, pady=(10, 5), sticky="w")

name_entry = ctk.CTkEntry(master=login_frame, width=200, fg_color="white")
name_entry.grid(row=3, column=0, padx=0, pady=5)

password_label = ctk.CTkLabel(master=login_frame, text="Password", font=("century gothic", 13, "bold"), text_color="black")
password_label.grid(row=4, column=0, padx=100, pady=(10, 5), sticky="w")

password_entry = ctk.CTkEntry(master=login_frame, width=200, fg_color="white", show="*")
password_entry.grid(row=5, column=0, padx=20, pady=5)

# Add a login button
login_button = ctk.CTkButton(master=login_frame, text="Log in", fg_color="#154734", hover_color="#588157", command=authenticate)
login_button.grid(row=6, column=0, padx=20, pady=(20, 10))

# Start the main loop
app.mainloop()
