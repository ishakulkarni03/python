import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()
    
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Info", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Length label and entry
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Uppercase checkbox
uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_checkbox.grid(row=1, column=0, columnspan=2)

# Numbers checkbox
numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_checkbox.grid(row=2, column=0, columnspan=2)

# Symbols checkbox
symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_checkbox.grid(row=3, column=0, columnspan=2)

# Generate password button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Password entry
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=6, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()

