import os
from openpyxl import Workbook, load_workbook
from datetime import datetime

def save_transaction(account_no, transaction_type, amount, balance, remarks):

    folder = "transactions"

    if not os.path.exists(folder):
        os.makedirs(folder)

    file_name = os.path.join(folder, f"{account_no}.xlsx")

    if os.path.exists(file_name):
        workbook = load_workbook(file_name)
        sheet = workbook.active
    else:
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Transactions"

        sheet.append([
            "Date & Time",
            "Transaction Type",
            "Amount",
            "Balance",
            "Remarks"
        ])

    sheet.append([
        datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        transaction_type,
        amount,
        balance,
        remarks
    ])

    workbook.save(file_name)