import tkinter as tk
from tkinter import ttk
from database import connection

def open_view_customers():

    window = tk.Toplevel()
    window.title("View Customers")
    window.geometry("1000x500")

    columns = (
        "ID",
        "Name",
        "Gender",
        "DOB",
        "Phone",
        "Email",
        "Aadhaar",
        "Address"
    )

    tree = ttk.Treeview(window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM customers")

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)

    cursor.close()

    tree.pack(fill="both", expand=True)