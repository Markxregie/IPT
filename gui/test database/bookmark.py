import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

connection = sqlite3.connect('bookmarks.db')
cursor = connection.cursor()


connection.commit()

# Function
def add(title, url):
    cursor.execute('INSERT INTO bookmarks (Title, URL) VALUES (?, ?)', (title, url))
    connection.commit()
    load_bookmarks()

def edit(bk_id, new_title, new_url):
    cursor.execute('UPDATE bookmarks SET Title = ?, URL = ? WHERE Bk_ID = ?', (new_title, new_url, bk_id))
    connection.commit()
    load_bookmarks()

def list_bookmarks():
    cursor.execute('SELECT * FROM bookmarks')
    return cursor.fetchall()

def remove(bk_id):
    cursor.execute('DELETE FROM bookmarks WHERE Bk_ID = ?', (bk_id,))
    connection.commit()
    load_bookmarks()

def load_bookmarks():
    for row in bookmarks_tree.get_children():
        bookmarks_tree.delete(row)
    for bk in list_bookmarks():
        bookmarks_tree.insert('', tk.END, values=bk)

def on_add():
    title = title_entry.get()
    url = url_entry.get()
    if title and url:
        add(title, url)
        title_entry.delete(0, tk.END)
        url_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Title and URL cannot be empty!")

def on_edit():
    selected_item = bookmarks_tree.selection()
    if selected_item:
        bk_id = bookmarks_tree.item(selected_item)['values'][0]
        title = title_entry.get()
        url = url_entry.get()
        if title and url:
            edit(bk_id, title, url)
            title_entry.delete(0, tk.END)
            url_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Title and URL cannot be empty!")
    else:
        messagebox.showwarning("Selection Error", "No bookmark selected!")

def on_remove():
    selected_item = bookmarks_tree.selection()
    if selected_item:
        bk_id = bookmarks_tree.item(selected_item)['values'][0]
        remove(bk_id)
    else:
        messagebox.showwarning("Selection Error", "No bookmark selected!")

def on_quit():
    connection.close()
    root.destroy()

# GUI
root = tk.Tk()
root.title("Bookmark Manager")
root.configure(bg='#603F83')

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#603F83", foreground="white")
style.configure("TButton", background="#C7D3D4", foreground="black", font=("Helvetica", 10))
style.configure("TFrame", background="#603F83")
style.configure("Treeview", background="white", foreground="black", fieldbackground="white")
style.configure("Treeview.Heading", background="#76528B", foreground="white", font=("Helvetica", 10, "bold"))
style.configure("Treeview", background="#C7D3D4", foreground="black", fieldbackground="#C7D3D4")
style.configure("Treeview.Heading", foreground="White", background="#603F83", font=("Helvetica", 10, "bold"))
style.map("Treeview.Heading",
          background=[("hover", "#76528B")],
          foreground=[("hover", "black")])

# Frames
title_frame = tk.Frame(root, bg='#603F83')
title_frame.pack(fill=tk.X)

input_frame = tk.Frame(root, padx=10, pady=10, bg='#603F83')
input_frame.pack(fill=tk.X, pady=10)

button_frame = tk.Frame(root, padx=10, pady=10, bg='#603F83')
button_frame.pack(fill=tk.X, pady=10)

tree_frame = tk.Frame(root, padx=10, pady=10, bg='#603F83')
tree_frame.pack(fill=tk.BOTH, expand=True)

# Title Label
title_label = tk.Label(title_frame, text="Bookmark Manager", bg='#603F83', fg='white', font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Input Fields
input_inner_frame = tk.Frame(input_frame, bg='#603F83')
input_inner_frame.pack(anchor=tk.CENTER)

label_title = tk.Label(input_inner_frame, text="Title", bg='#603F83', fg='white')
label_title.grid(row=0, column=0, padx=(10, 5))
title_entry = tk.Entry(input_inner_frame)
title_entry.grid(row=0, column=1, padx=5)

label_url = tk.Label(input_inner_frame, text="URL", bg='#603F83', fg='white')
label_url.grid(row=0, column=2, padx=(10, 5))
url_entry = tk.Entry(input_inner_frame)
url_entry.grid(row=0, column=3, padx=5)

# Buttons
button_inner_frame = tk.Frame(button_frame, bg='#603F83')
button_inner_frame.pack(anchor=tk.CENTER)

button_add = tk.Button(button_inner_frame, text="Add", command=on_add, bg='#C7D3D4', fg='black', font=("Helvetica", 10))
button_add.grid(row=0, column=0, padx=(10, 5))

button_edit = tk.Button(button_inner_frame, text="Edit", command=on_edit, bg='#C7D3D4', fg='black', font=("Helvetica", 10))
button_edit.grid(row=0, column=1, padx=5)

button_remove = tk.Button(button_inner_frame, text="Remove", command=on_remove, bg='#C7D3D4', fg='black', font=("Helvetica", 10))
button_remove.grid(row=0, column=2, padx=5)

button_quit = tk.Button(button_inner_frame, text="Quit", command=on_quit, bg='#C7D3D4', fg='black', font=("Helvetica", 10))
button_quit.grid(row=0, column=3, padx=5)

# Treeview
columns = ("ID", "Title", "URL")
bookmarks_tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
bookmarks_tree.heading("ID", text="ID", anchor=tk.CENTER)
bookmarks_tree.heading("Title", text="Title")
bookmarks_tree.heading("URL", text="URL")

bookmarks_tree.column("ID", anchor=tk.CENTER)

bookmarks_tree.pack(fill=tk.BOTH, expand=True)

load_bookmarks()

root.mainloop()
