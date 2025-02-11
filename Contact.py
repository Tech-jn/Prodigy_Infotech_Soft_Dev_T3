import tkinter as tk

from tkinter import messagebox, simpledialog

import json



# Function to load contacts from a file

def load_contacts(filename):

    try:

        with open(filename, 'r') as file:

            contacts = json.load(file)

    except FileNotFoundError:

        contacts = []

    return contacts



# Function to save contacts to a file

def save_contacts(contacts, filename):

    with open(filename, 'w') as file:

        json.dump(contacts, file)



# Function to refresh the contact list display

def refresh_contacts_list():

    contacts_listbox.delete(0, tk.END)

    for contact in contacts:

        contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']} - {contact['email']}")



# Function to add a new contact

def add_contact():

    name = simpledialog.askstring("Input", "Enter name:")

    phone = simpledialog.askstring("Input", "Enter phone number:")

    email = simpledialog.askstring("Input", "Enter email address:")

    if name and phone and email:

        contacts.append({"name": name, "phone": phone, "email": email})

        save_contacts(contacts, filename)

        refresh_contacts_list()

        messagebox.showinfo("Info", "Contact added successfully!")

    else:

        messagebox.showwarning("Warning", "Please enter all details!")



# Function to edit a selected contact

def edit_contact():

    selected_index = contacts_listbox.curselection()

    if selected_index:

        index = selected_index[0]

        contact = contacts[index]

        name = simpledialog.askstring("Input", "Enter new name:", initialvalue=contact['name'])

        phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=contact['phone'])

        email = simpledialog.askstring("Input", "Enter new email address:", initialvalue=contact['email'])

        if name and phone and email:

            contacts[index] = {"name": name, "phone": phone, "email": email}

            save_contacts(contacts, filename)

            refresh_contacts_list()

            messagebox.showinfo("Info", "Contact edited successfully!")

        else:

            messagebox.showwarning("Warning", "Please enter all details!")

    else:

        messagebox.showwarning("Warning", "Please select a contact to edit!")



# Function to delete a selected contact

def delete_contact():

    selected_index = contacts_listbox.curselection()

    if selected_index:

        index = selected_index[0]

        contacts.pop(index)

        save_contacts(contacts, filename)

        refresh_contacts_list()

        messagebox.showinfo("Info", "Contact deleted successfully!")

    else:

        messagebox.showwarning("Warning", "Please select a contact to delete!")



# Main function to create the GUI

def main():

    global contacts_listbox, contacts

    global filename

    filename = "contacts.json"

    contacts = load_contacts(filename)



    root = tk.Tk()

    root.title("Contact Manager")

    root.config(bg="black")



    frame = tk.Frame(root, bg="black")

    frame.pack(pady=10)



    contacts_listbox = tk.Listbox(frame, width=50, height=15, bg="white", fg="#000000", selectbackground="#87cefa")

    contacts_listbox.pack()



    button_frame = tk.Frame(root, bg="#f0f0f0")

    button_frame.pack(pady=10)



    add_button = tk.Button(button_frame, text="Add Contact", command=add_contact, bg="#4caf50", fg="#ffffff")

    add_button.grid(row=0, column=0, padx=5)



    edit_button = tk.Button(button_frame, text="Edit Contact", command=edit_contact, bg="#2196f3", fg="#ffffff")

    edit_button.grid(row=0, column=1, padx=5)



    delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact, bg="#f44336", fg="#ffffff")

    delete_button.grid(row=0, column=2, padx=5)



    refresh_contacts_list()



    root.mainloop()



if __name__ == "__main__":

    main()
