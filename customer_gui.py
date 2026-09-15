import tkinter as tk
from tkinter import messagebox
from database import connection

def open_add_customer():

    window = tk.Toplevel()
    window.title("Add Customer")
    window.geometry("450x450")

    labels = [
        "Customer Name",
        "Gender",
        "Date of Birth (YYYY-MM-DD)",
        "Phone",
        "Email",
        "Aadhaar",
        "Address"
    ]

    entries = []

    for i, text in enumerate(labels):
        tk.Label(window, text=text).grid(row=i, column=0, padx=10, pady=8, sticky="w")

        entry = tk.Entry(window, width=30)
        entry.grid(row=i, column=1, padx=10, pady=8)

        entries.append(entry)

    def save_customer():

        cursor = connection.cursor()

        query = """
        INSERT INTO customers
        (customer_name, gender, date_of_birth, phone, email, aadhaar, address)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            entries[0].get(),
            entries[1].get(),
            entries[2].get(),
            entries[3].get(),
            entries[4].get(),
            entries[5].get(),
            entries[6].get()
        )

        cursor.execute(query, values)
        connection.commit()

        cursor.close()

        messagebox.showinfo("Success", "Customer Added Successfully!")

        window.destroy()

    tk.Button(
        window,
        text="Save Customer",
        command=save_customer,
        bg="green",
        fg="white"
    ).grid(row=8, column=0, columnspan=2, pady=20)