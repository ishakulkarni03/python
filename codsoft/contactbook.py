import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
        messagebox.showinfo("Success", "Contact added successfully!")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Name and phone number are required!")

def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contacts():
    query = search_entry.get()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def update_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        index = selected_index[0]
        contact = contacts[index]
        new_name = simpledialog.askstring("Update Name", "Enter new name:", initialvalue=contact['name'])
        new_phone = simpledialog.askstring("Update Phone", "Enter new phone number:", initialvalue=contact['phone'])
        new_email = simpledialog.askstring("Update Email", "Enter new email:", initialvalue=contact['email'])
        new_address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=contact['address'])
        
        contacts[index] = {'name': new_name, 'phone': new_phone, 'email': new_email, 'address': new_address}
        messagebox.showinfo("Success", "Contact updated successfully!")
        view_contacts()
    else:
        messagebox.showwarning("Warning", "No contact selected!")

def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        index = selected_index[0]
        contacts.pop(index)
        messagebox.showinfo("Success", "Contact deleted successfully!")
        view_contacts()
    else:
        messagebox.showwarning("Warning", "No contact selected!")

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Add contact form
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, columnspan=2, pady=10)

# Contact list and operations
contact_list = tk.Listbox(root, width=50, height=15)
contact_list.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

tk.Button(root, text="View Contacts", command=view_contacts).grid(row=6, column=0, columnspan=2, pady=10)

tk.Label(root, text="Search:").grid(row=7, column=0, padx=10, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=7, column=1, padx=10, pady=5)

tk.Button(root, text="Search", command=search_contacts).grid(row=8, column=0, columnspan=2, pady=10)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=9, column=0, columnspan=2, pady=10)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=10, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
