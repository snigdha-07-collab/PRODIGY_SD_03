import tkinter as tk
from tkinter import ttk, messagebox

contacts = []

def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    contacts.append([name, phone, email])

    tree.insert("", "end", values=(name, phone, email))

    clear_fields()

def delete_contact():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a contact first!")
        return

    tree.delete(selected[0])

def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")

def search_contact():
    keyword = name_var.get().lower()

    for item in tree.get_children():
        tree.delete(item)

    for contact in contacts:
        if keyword in contact[0].lower():
            tree.insert("", "end", values=contact)

root = tk.Tk()
root.title("Contact Management System")
root.geometry("700x500")

title = tk.Label(root,
                 text="Contact Management System",
                 font=("Arial", 18, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()

tk.Label(frame, text="Name").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(frame, textvariable=name_var).grid(row=0, column=1)

tk.Label(frame, text="Phone").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(frame, textvariable=phone_var).grid(row=1, column=1)

tk.Label(frame, text="Email").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(frame, textvariable=email_var).grid(row=2, column=1)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Contact",
          command=add_contact).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Search",
          command=search_contact).grid(row=0, column=1, padx=10)

tk.Button(btn_frame, text="Delete",
          command=delete_contact).grid(row=0, column=2, padx=10)

tk.Button(btn_frame, text="Clear",
          command=clear_fields).grid(row=0, column=3, padx=10)

columns = ("Name", "Phone", "Email")

tree = ttk.Treeview(root,
                    columns=columns,
                    show="headings",
                    height=12)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200)

tree.pack(pady=20)

root.mainloop()