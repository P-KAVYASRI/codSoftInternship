import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

# Initialize the main application window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("600x400")

# Contact list
contacts = []

# Functions to handle contact management
def add_contact():
    name = simpledialog.askstring("Input", "Enter Name:")
    phone = simpledialog.askstring("Input", "Enter Phone Number:")
    email = simpledialog.askstring("Input", "Enter Email:")
    address = simpledialog.askstring("Input", "Enter Address:")
    
    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        update_contact_list()
    else:
        messagebox.showerror("Input Error", "Name and Phone number are required!")

def update_contact_list():
    for i in contact_tree.get_children():
        contact_tree.delete(i)
    for contact in contacts:
        contact_tree.insert("", "end", values=(contact["name"], contact["phone"]))

def view_contacts():
    update_contact_list()

def search_contact():
    search_term = simpledialog.askstring("Input", "Enter Name or Phone Number to search:")
    if search_term:
        for contact in contacts:
            if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]:
                messagebox.showinfo("Search Result", f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
                return
        messagebox.showinfo("Search Result", "Contact not found!")

def update_contact():
    search_term = simpledialog.askstring("Input", "Enter Name or Phone Number of the contact to update:")
    if search_term:
        for contact in contacts:
            if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]:
                new_name = simpledialog.askstring("Input", f"Enter new name (current: {contact['name']}):")
                new_phone = simpledialog.askstring("Input", f"Enter new phone number (current: {contact['phone']}):")
                new_email = simpledialog.askstring("Input", f"Enter new email (current: {contact['email']}):")
                new_address = simpledialog.askstring("Input", f"Enter new address (current: {contact['address']}):")
                
                contact["name"] = new_name if new_name else contact["name"]
                contact["phone"] = new_phone if new_phone else contact["phone"]
                contact["email"] = new_email if new_email else contact["email"]
                contact["address"] = new_address if new_address else contact["address"]
                
                update_contact_list()
                return
        messagebox.showinfo("Update Result", "Contact not found!")

def delete_contact():
    search_term = simpledialog.askstring("Input", "Enter Name or Phone Number of the contact to delete:")
    if search_term:
        for contact in contacts:
            if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]:
                contacts.remove(contact)
                update_contact_list()
                messagebox.showinfo("Delete Result", "Contact deleted successfully!")
                return
        messagebox.showinfo("Delete Result", "Contact not found!")

# Creating buttons for different functionalities
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact)
add_button.grid(row=0, column=0, padx=5)

view_button = tk.Button(button_frame, text="View Contacts", command=view_contacts)
view_button.grid(row=0, column=1, padx=5)

search_button = tk.Button(button_frame, text="Search Contact", command=search_contact)
search_button.grid(row=0, column=2, padx=5)

update_button = tk.Button(button_frame, text="Update Contact", command=update_contact)
update_button.grid(row=0, column=3, padx=5)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact)
delete_button.grid(row=0, column=4, padx=5)

# Contact list display
contact_tree = ttk.Treeview(root, columns=("Name", "Phone"), show="headings")
contact_tree.heading("Name", text="Name")
contact_tree.heading("Phone", text="Phone")
contact_tree.pack(fill=tk.BOTH, expand=True)

# Run the main event loop
root.mainloop()
