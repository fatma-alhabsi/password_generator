import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # For copying password to clipboard

def generate_password():
    length = int(length_entry.get())
    chars = ""
    if use_upper.get():
        chars += string.ascii_uppercase
    if use_lower.get():
        chars += string.ascii_lowercase
    if use_numbers.get():
        chars += string.digits
    if use_symbols.get():
        chars += string.punctuation
    
    if not chars:
        messagebox.showerror("Error", "Please select at least one character type")
        return
    
    password = "".join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    pyperclip.copy(password_entry.get())

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")

# Checkbuttons for character options
use_upper = tk.BooleanVar()
use_lower = tk.BooleanVar()
use_numbers = tk.BooleanVar()
use_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Uppercase Letters", variable=use_upper).pack()
tk.Checkbutton(root, text="Lowercase Letters", variable=use_lower).pack()
tk.Checkbutton(root, text="Numbers", variable=use_numbers).pack()
tk.Checkbutton(root, text="Symbols", variable=use_symbols).pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Password display
password_entry = tk.Entry(root, width=30)
password_entry.pack()

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

# Run the application
root.mainloop()
