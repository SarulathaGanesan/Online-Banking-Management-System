import tkinter as tk
from tkinter import ttk, messagebox
from database import connection
from excel import save_transaction

def open_deposit():

    window = tk.Toplevel()
    window.title("Deposit Money")
    window.geometry("400x250")

    tk.Label(window, text="Account Number").pack(pady=5)
    account_no = tk.Entry(window)
    account_no.pack()

    tk.Label(window, text="Deposit Amount").pack(pady=5)
    amount = tk.Entry(window)
    amount.pack()

    def deposit():

        account = account_no.get().strip()
        amount_text = amount.get().strip()

        if account == "":
            messagebox.showerror("Error", "Please enter Account Number")
            return

        if amount_text == "":
            messagebox.showerror("Error", "Please enter Deposit Amount")
            return

        try:
            deposit_amount = float(amount_text)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
            return

        if deposit_amount <= 0:
            messagebox.showerror("Error", "Amount must be greater than 0")
            return

        cursor = connection.cursor()

        cursor.execute(
            "SELECT balance FROM accounts WHERE account_no=%s",
            (account,)
        )

        result = cursor.fetchone()

        if result:

            current_balance = float(result[0])
            new_balance = current_balance + deposit_amount

            cursor.execute(
                "UPDATE accounts SET balance=%s WHERE account_no=%s",
                (new_balance, account)
            )

            cursor.execute("""
            INSERT INTO transactions
            (account_no, transaction_type, amount,
             balance_after_transaction, remarks)
            VALUES (%s,%s,%s,%s,%s)
            """, (
                account,
                "Deposit",
                deposit_amount,
                new_balance,
                "Cash Deposit"
            ))

            connection.commit()

            save_transaction(
                account,
                "Deposit",
                deposit_amount,
                new_balance,
                "Cash Deposit"
            )

            messagebox.showinfo(
                "Success",
                f"Deposit Successful!\nCurrent Balance: ₹{new_balance}"
            )

            window.destroy()

        else:

            messagebox.showerror(
                "Error",
                "Account Not Found!"
            )

        cursor.close()
    tk.Button(
        window,
        text="Deposit",
        command=deposit,
        bg="green",
        fg="white"
    ).pack(pady=20)

def open_create_account():

    window = tk.Toplevel()
    window.title("Create Account")
    window.geometry("400x300")

    tk.Label(window, text="Customer ID").pack(pady=5)
    customer_id = tk.Entry(window)
    customer_id.pack()

    tk.Label(window, text="Account Type").pack(pady=5)

    account_type = ttk.Combobox(
        window,
        values=["Savings", "Current"],
        state="readonly"
    )
    account_type.current(0)
    account_type.pack()

    tk.Label(window, text="Opening Balance").pack(pady=5)
    balance = tk.Entry(window)
    balance.pack()

    def create():

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM customers WHERE customer_id=%s",
            (customer_id.get(),)
        )

        customer = cursor.fetchone()

        if customer:

            query = """
            INSERT INTO accounts
            (customer_id, account_type, balance)
            VALUES (%s,%s,%s)
            """

            values = (
                customer_id.get(),
                account_type.get(),
                balance.get()
            )

            cursor.execute(query, values)
            connection.commit()

            messagebox.showinfo(
                "Success",
                "Account Created Successfully!"
            )

            window.destroy()

        else:
            messagebox.showerror(
                "Error",
                "Customer Not Found!"
            )

        cursor.close()

    tk.Button(
        window,
        text="Create Account",
        bg="green",
        fg="white",
        command=create
    ).pack(pady=20)

def open_withdraw():

    window = tk.Toplevel()
    window.title("Withdraw Money")
    window.geometry("400x250")

    tk.Label(window, text="Account Number").pack(pady=5)
    account_no = tk.Entry(window)
    account_no.pack()

    tk.Label(window, text="Withdraw Amount").pack(pady=5)
    amount = tk.Entry(window)
    amount.pack()

    def withdraw():

        cursor = connection.cursor()

        cursor.execute(
            "SELECT balance FROM accounts WHERE account_no=%s",
            (account_no.get(),)
        )

        result = cursor.fetchone()

        if result:

            current_balance = float(result[0])
            withdraw_amount = float(amount.get())

            if withdraw_amount > current_balance:

                messagebox.showerror(
                    "Error",
                    "Insufficient Balance!"
                )

            else:

                new_balance = current_balance - withdraw_amount

                cursor.execute(
                    "UPDATE accounts SET balance=%s WHERE account_no=%s",
                    (new_balance, account_no.get())
                )

                cursor.execute("""
                INSERT INTO transactions
                (account_no, transaction_type, amount,
                 balance_after_transaction, remarks)
                VALUES (%s,%s,%s,%s,%s)
                """, (
                    account_no.get(),
                    "Withdraw",
                    withdraw_amount,
                    new_balance,
                    "Cash Withdrawal"
                ))

                connection.commit()

                save_transaction(
                    account_no.get(),
                    "Withdraw",
                    withdraw_amount,
                    new_balance,
                    "Cash Withdrawal"
                )

                messagebox.showinfo(
                    "Success",
                    f"Withdrawal Successful!\nCurrent Balance: ₹{new_balance}"
                )

                window.destroy()

        else:

            messagebox.showerror(
                "Error",
                "Account Not Found!"
            )

        cursor.close()

    tk.Button(
        window,
        text="Withdraw",
        command=withdraw,
        bg="red",
        fg="white"
    ).pack(pady=20)

def open_transfer():

    window = tk.Toplevel()
    window.title("Transfer Money")
    window.geometry("400x300")

    tk.Label(
        window,
        text="Sender Account Number"
    ).pack(pady=5)

    sender = tk.Entry(window)
    sender.pack()

    tk.Label(
        window,
        text="Receiver Account Number"
    ).pack(pady=5)

    receiver = tk.Entry(window)
    receiver.pack()

    tk.Label(
        window,
        text="Transfer Amount"
    ).pack(pady=5)

    amount = tk.Entry(window)
    amount.pack()

    def transfer():

        sender_account = sender.get().strip()
        receiver_account = receiver.get().strip()
        amount_text = amount.get().strip()

        # Check Sender Account
        if sender_account == "":
            messagebox.showerror(
                "Error",
                "Please enter Sender Account Number"
            )
            return

        # Check Receiver Account
        if receiver_account == "":
            messagebox.showerror(
                "Error",
                "Please enter Receiver Account Number"
            )
            return

        # Check Same Account
        if sender_account == receiver_account:
            messagebox.showerror(
                "Error",
                "Sender and Receiver accounts cannot be same"
            )
            return

        # Check Amount
        if amount_text == "":
            messagebox.showerror(
                "Error",
                "Please enter Transfer Amount"
            )
            return

        # Check Amount is a number
        try:
            transfer_amount = float(amount_text)

        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter a valid amount"
            )
            return

        # Check Amount is positive
        if transfer_amount <= 0:
            messagebox.showerror(
                "Error",
                "Amount must be greater than 0"
            )
            return

        cursor = connection.cursor()

        # Check Sender Account
        cursor.execute(
            "SELECT balance FROM accounts WHERE account_no=%s",
            (sender_account,)
        )

        sender_data = cursor.fetchone()

        if sender_data is None:

            messagebox.showerror(
                "Error",
                "Sender Account Not Found!"
            )

            cursor.close()
            return

        # Check Receiver Account
        cursor.execute(
            "SELECT balance FROM accounts WHERE account_no=%s",
            (receiver_account,)
        )

        receiver_data = cursor.fetchone()

        if receiver_data is None:

            messagebox.showerror(
                "Error",
                "Receiver Account Not Found!"
            )

            cursor.close()
            return

        sender_balance = float(sender_data[0])
        receiver_balance = float(receiver_data[0])

        # Check Sufficient Balance
        if transfer_amount > sender_balance:

            messagebox.showerror(
                "Error",
                "Insufficient Balance!"
            )

            cursor.close()
            return

        # Calculate New Balances
        new_sender_balance = sender_balance - transfer_amount
        new_receiver_balance = receiver_balance + transfer_amount

        # Update Sender
        cursor.execute(
            "UPDATE accounts SET balance=%s WHERE account_no=%s",
            (new_sender_balance, sender_account)
        )

        # Update Receiver
        cursor.execute(
            "UPDATE accounts SET balance=%s WHERE account_no=%s",
            (new_receiver_balance, receiver_account)
        )

        # Sender Transaction
        cursor.execute("""
            INSERT INTO transactions
            (account_no, transaction_type, amount,
             balance_after_transaction, remarks)
            VALUES(%s,%s,%s,%s,%s)
        """, (
            sender_account,
            "Transfer Out",
            transfer_amount,
            new_sender_balance,
            f"Transferred to {receiver_account}"
        ))

        # Receiver Transaction
        cursor.execute("""
            INSERT INTO transactions
            (account_no, transaction_type, amount,
             balance_after_transaction, remarks)
            VALUES(%s,%s,%s,%s,%s)
        """, (
            receiver_account,
            "Transfer In",
            transfer_amount,
            new_receiver_balance,
            f"Received from {sender_account}"
        ))

        connection.commit()

        # Save Sender Transaction to Excel
        save_transaction(
            sender_account,
            "Transfer Out",
            transfer_amount,
            new_sender_balance,
            f"Transferred to {receiver_account}"
        )

        # Save Receiver Transaction to Excel
        save_transaction(
            receiver_account,
            "Transfer In",
            transfer_amount,
            new_receiver_balance,
            f"Received from {sender_account}"
        )

        messagebox.showinfo(
            "Success",
            "Money Transferred Successfully!"
        )

        cursor.close()
        window.destroy()

    tk.Button(
        window,
        text="Transfer",
        command=transfer,
        bg="blue",
        fg="white"
    ).pack(pady=20)