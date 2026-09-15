from account_gui import (
    open_create_account,
    open_deposit,
    open_withdraw,
    open_transfer
)
from account_gui import open_create_account
from view_customer_gui import open_view_customers
from customer_gui import open_add_customer
from transaction_gui import open_transaction_history
from balance_gui import open_check_balance
import tkinter as tk

def open_dashboard():

    dashboard = tk.Toplevel(root)
    dashboard.title("Dashboard")
    dashboard.geometry("500x600")
    dashboard.configure(bg="white")

    tk.Label(
        dashboard,
        text="BANK DASHBOARD",
        font=("Arial",18,"bold"),
        bg="white"
    ).pack(pady=20)

    tk.Button(
    dashboard,
    text="Add Customer",
    width=25,
    command=open_add_customer
    ).pack(pady=5)
    tk.Button(
    dashboard,
    text="View Customers",
    width=25,
    command=open_view_customers
    ).pack(pady=5)
    tk.Button(
    dashboard,
    text="Create Account",
    width=25,
    command=open_create_account
    ).pack(pady=5)

    tk.Button(
    dashboard,
    text="Deposit Money",
    width=25,
    command=open_deposit
    ).pack(pady=5)

    tk.Button(
    dashboard,
    text="Withdraw Money",
    width=25,
    command=open_withdraw
    ).pack(pady=5)

    tk.Button(
    dashboard,
    text="Transfer Money",
    width=25,
    command=open_transfer
    ).pack(pady=5)

    tk.Button(
    dashboard,
    text="Transaction History",
    width=25,
    command=open_transaction_history
    ).pack(pady=5)
    
    tk.Button(
    dashboard,
    text="Check Balance",
    width=25,
    command=open_check_balance
    ).pack(pady=5)

    tk.Button(
        dashboard,
        text="Exit",
        width=25,
        command=dashboard.destroy
    ).pack(pady=20)


# Main Window
root = tk.Tk()
root.title("Online Banking Management System")
root.geometry("600x500")
root.configure(bg="lightblue")

title = tk.Label(
    root,
    text="ONLINE BANKING MANAGEMENT SYSTEM",
    font=("Arial",18,"bold"),
    bg="lightblue"
)
title.pack(pady=30)

tk.Button(
    root,
    text="Open Dashboard",
    width=25,
    height=2,
    command=open_dashboard
).pack(pady=20)

root.mainloop()