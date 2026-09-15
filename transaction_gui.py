import tkinter as tk
from tkinter import ttk
from database import connection

def open_transaction_history():

    window = tk.Toplevel()
    window.title("Transaction History")
    window.geometry("1000x500")

    tk.Label(
        window,
        text="Account Number"
    ).pack(pady=5)

    account_entry = tk.Entry(window)
    account_entry.pack()

    tree = ttk.Treeview(
        window,
        columns=(
            "ID",
            "Type",
            "Amount",
            "Balance",
            "Date",
            "Remarks"
        ),
        show="headings"
    )

    headings = [
        "ID",
        "Type",
        "Amount",
        "Balance",
        "Date",
        "Remarks"
    ]

    for heading in headings:
        tree.heading(heading, text=heading)
        tree.column(heading, width=150)

    tree.pack(fill="both", expand=True)

    def load_transactions():

        for item in tree.get_children():
            tree.delete(item)

        cursor = connection.cursor()

        cursor.execute("""
        SELECT transaction_id,
               transaction_type,
               amount,
               balance_after_transaction,
               transaction_date,
               remarks
        FROM transactions
        WHERE account_no=%s
        ORDER BY transaction_date DESC
        """, (account_entry.get(),))

        rows = cursor.fetchall()

        for row in rows:
            tree.insert("", tk.END, values=row)

        cursor.close()

    tk.Button(
        window,
        text="Search",
        command=load_transactions,
        bg="green",
        fg="white"
    ).pack(pady=10)