import tkinter as tk
from tkinter import messagebox
from database import connection


def open_check_balance():

    window = tk.Toplevel()
    window.title("Check Balance")
    window.geometry("400x300")

    tk.Label(
        window,
        text="CHECK ACCOUNT BALANCE",
        font=("Arial", 16, "bold")
    ).pack(pady=20)

    tk.Label(
        window,
        text="Account Number"
    ).pack(pady=5)

    account_no = tk.Entry(window, width=30)
    account_no.pack()

    result_label = tk.Label(
        window,
        text="",
        font=("Arial", 12)
    )
    result_label.pack(pady=20)

    def check_balance():

        cursor = connection.cursor()

        cursor.execute("""
        SELECT account_no, account_type, balance, status
        FROM accounts
        WHERE account_no=%s
        """, (account_no.get(),))

        result = cursor.fetchone()

        cursor.close()

        if result:

            result_label.config(
                text=f"""
Account Number: {result[0]}
Account Type: {result[1]}
Balance: ₹{result[2]}
Status: {result[3]}
"""
            )

        else:

            messagebox.showerror(
                "Error",
                "Account Not Found!"
            )

    tk.Button(
        window,
        text="Check Balance",
        width=20,
        command=check_balance
    ).pack(pady=10)