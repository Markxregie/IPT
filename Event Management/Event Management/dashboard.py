import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()

app.title("Dashboard")
app.geometry("1555x800")
app.configure(bg_color="white")

def homepage():
    homepage_fm = ctk.CTkFrame(main_frame, fg_color='white')  # Set background color of homepage_fm to white
    homepage_lb = ctk.CTkLabel(homepage_fm, text='DASHBOARD', font=('Century Gothic bold', 25), text_color='black')
    homepage_lb.pack(pady=30, padx=20, anchor='w')
    homepage_fm.pack(fill=ctk.BOTH, expand=True)


    # Create the upcoming event frame with specific dimensions
    upcoming_event_frame = ctk.CTkFrame(homepage_fm, fg_color='#A3B18A', width=700, height=300, corner_radius=20)
    upcoming_event_frame.pack(pady=10, padx=20, anchor='w')

    upcoming_event_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
    # Add a label inside the green frame
    green_label = ctk.CTkLabel(upcoming_event_frame, text='Upcoming Events',fg_color='#A3B18A', font=('Century Gothic bold', 30), text_color='white')
    green_label.pack(pady=5, padx=20, anchor='w')

    # Create a frame to hold the labels and entries side by side
    event_info_frame = ctk.CTkFrame(upcoming_event_frame, fg_color='#A3B18A')
    event_info_frame.pack(pady=10, padx=20, anchor='w', fill=ctk.X)

    # Total Events Section
    total_events_label = ctk.CTkLabel(event_info_frame, text='Total Number of Events', font=('Century Gothic bold', 15), text_color='white')
    total_events_label.grid(row=0, column=0, pady=0, padx=0, sticky='w')

    total_events_entry = ctk.CTkEntry(event_info_frame, state='readonly', font=('Century Gothic bold', 15), text_color='white', height=30, width=100, fg_color='#A3B18A', border_width=1)
    total_events_entry.grid(row=1, column=0, pady=0, padx=0, sticky='w')

    # Events Today Section
    events_today_label = ctk.CTkLabel(event_info_frame, text='Events Today', font=('Century Gothic bold', 15), text_color='white')
    events_today_label.grid(row=3, column=0, pady=5, padx=0, sticky='w')

    events_today_entry = ctk.CTkEntry(event_info_frame, state='readonly', font=('Century Gothic bold', 15), text_color='white', height=30, width=100, fg_color='#A3B18A', border_width=1)
    events_today_entry.grid(row=4, column=0, pady=0, padx=0, sticky='w')

    # Pending event Section
    pending_events_label = ctk.CTkLabel(event_info_frame, text='Pending Event', font=('Century Gothic bold', 15), text_color='white')
    pending_events_label.grid(row=5, column=0, pady=5, padx=0, sticky='w')

    pending_events_entry = ctk.CTkEntry(event_info_frame, state='readonly', font=('Century Gothic bold', 15), text_color='white', height=30, width=100, fg_color='#A3B18A', border_width=1)
    pending_events_entry.grid(row=6, column=0, pady=0, padx=0, sticky='w')

    homepage_fm.pack(fill=ctk.BOTH, expand=True)

    
    
def schedule():
    schedule_fm = ctk.CTkFrame(main_frame)
    schedule_lb = ctk.CTkLabel(schedule_fm, text='Scheduled Events', font=('Century Gothic', 25), text_color='black')
    schedule_lb.pack(pady=50, padx=20, anchor='w')
    schedule_fm.pack(fill=ctk.BOTH, expand=True)

def coordinators():
    coordinators_fm = ctk.CTkFrame(main_frame)
    coordinators_lb = ctk.CTkLabel(coordinators_fm, text='Coordinators', font=('Century Gothic', 25), text_color='black')
    coordinators_lb.pack(pady=50, padx=20, anchor='w')
    coordinators_fm.pack(fill=ctk.BOTH, expand=True)

def report():
    report_fm = ctk.CTkFrame(main_frame)
    report_lb = ctk.CTkLabel(report_fm, text='Report', font=('Century Gothic', 25), text_color='black')
    report_lb.pack(pady=50, padx=20, anchor='w')
    report_fm.pack(fill=ctk.BOTH, expand=True)

def staff():
    staff_fm = ctk.CTkFrame(main_frame)
    staff_lb = ctk.CTkLabel(staff_fm, text='Staff', font=('Century Gothic', 25), text_color='black')
    staff_lb.pack(pady=50, padx=20, anchor='w')
    staff_fm.pack(fill=ctk.BOTH, expand=True)

def switch(page_function):
    for fm in main_frame.winfo_children():
        fm.destroy()
    page_function()

# Load the images
image_path = "testinglogo.png"
image = Image.open(image_path)
image = image.resize((80, 80), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)

image_path = "home3.png"
image_home = ctk.CTkImage(dark_image=Image.open(image_path), size=(40, 40))

image_path = "bookmark.png"
image_schedule = ctk.CTkImage(dark_image=Image.open(image_path), size=(40, 40))

image_path = "cal2.png"
image_coordinators = ctk.CTkImage(dark_image=Image.open(image_path), size=(40, 40))

image_path = "report.png"
image_report = ctk.CTkImage(dark_image=Image.open(image_path), size=(40, 40))

image_path = "staff3.png"
image_staff = ctk.CTkImage(dark_image=Image.open(image_path), size=(45, 45))

image_path = "logut.png"
image_logout = ctk.CTkImage(dark_image=Image.open(image_path), size=(45, 45))

# Create the option frame
option_frame = ctk.CTkFrame(app, border_color='#D9D9D9', fg_color='white', corner_radius=0)
option_frame.pack(side=ctk.LEFT, fill=ctk.Y)

# Option button
image_label = ctk.CTkLabel(option_frame, image=photo, text="")
image_label.place(x=13, y=30)

home_btn = ctk.CTkButton(option_frame, image=image_home, text="", fg_color="white", border_width=0, hover_color="#A3B18A", width=95, command=lambda: switch(homepage))
home_btn.place(x=2, y=165)

schedule_btn = ctk.CTkButton(option_frame, image=image_schedule, text="", fg_color="white", border_width=0, hover_color="#A3B18A", width=95, command=lambda: switch(schedule))
schedule_btn.place(x=2, y=227)

coordinators_btn = ctk.CTkButton(option_frame, image=image_coordinators, text="", fg_color="white", border_width=0, hover_color="#A3B18A", width=95, command=lambda: switch(coordinators))
coordinators_btn.place(x=2, y=295)

report_btn = ctk.CTkButton(option_frame, image=image_report, text="", fg_color="white", border_width=0, hover_color="#A3B18A", width=95, command=lambda: switch(report))
report_btn.place(x=2, y=359)

staff_btn = ctk.CTkButton(option_frame, image=image_staff, text="", fg_color="white", border_width=0, hover_color="#A3B18A", width=95, command=lambda: switch(staff))
staff_btn.place(x=2, y=428)

logut_btn = ctk.CTkButton(option_frame, image=image_logout, text="", fg_color="white", border_width=0, hover_color="#A3B18A", width=95)
logut_btn.place(x=2, y=700)

option_frame.pack_propagate(False)
option_frame.configure(width=100, height=800)

# Create the main frame
main_frame = ctk.CTkFrame(app, bg_color="white")
main_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)
main_frame.pack_propagate(False)
main_frame.configure(height=800, width=1490)

homepage()

app.mainloop()