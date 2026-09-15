from excel import save_transaction
from database import connection

from database import connection
import random

def generate_account_number():
    cursor = connection.cursor()

    while True:
        account_no = random.randint(1000000000, 9999999999)

        cursor.execute(
            "SELECT account_no FROM accounts WHERE account_no=%s",
            (account_no,)
        )

        if cursor.fetchone() is None:
            cursor.close()
            return account_no


def create_account():
    cursor = connection.cursor()

    customer_id = input("Enter Customer ID: ")

    cursor.execute(
        "SELECT * FROM customers WHERE customer_id=%s",
        (customer_id,)
    )

    customer = cursor.fetchone()

    if customer:

        account_type = input("Enter Account Type (Savings/Current): ")
        balance = float(input("Enter Opening Balance: "))

        account_no = generate_account_number()

        cursor.execute("""
        INSERT INTO accounts
        (account_no, customer_id, account_type, balance)
        VALUES(%s,%s,%s,%s)
        """,
        (
            account_no,
            customer_id,
            account_type,
            balance
        ))

        connection.commit()

        print("\nAccount Created Successfully!")
        print("Generated Account Number:", account_no)

    else:
        print("Customer Not Found!")

    cursor.close()

def deposit_money():
    cursor = connection.cursor()

    account_no = input("Enter Account Number: ")
    amount = float(input("Enter Deposit Amount: "))

    # Check account
    cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (account_no,))
    result = cursor.fetchone()

    if result:

        current_balance = float(result[0])
        new_balance = current_balance + amount

        # Update balance
        cursor.execute(
            "UPDATE accounts SET balance=%s WHERE account_no=%s",
            (new_balance, account_no)
        )

        # Store transaction
        cursor.execute("""
        INSERT INTO transactions
        (account_no, transaction_type, amount, balance_after_transaction, remarks)
        VALUES (%s,%s,%s,%s,%s)
        """, (
            account_no,
            "Deposit",
            amount,
            new_balance,
            "Cash Deposit"
        ))

        connection.commit()

        save_transaction(
            account_no,
            "Deposit",
            amount,
            new_balance,
            "Cash Deposit"
        )

        print("\nDeposit Successful!")
        print("Current Balance:", new_balance)

    else:
        print("\nAccount Not Found!")

    cursor.close()   

def withdraw_money():
    cursor = connection.cursor()

    account_no = input("Enter Account Number: ")
    amount = float(input("Enter Withdraw Amount: "))

    cursor.execute(
        "SELECT balance FROM accounts WHERE account_no=%s",
        (account_no,)
    )

    result = cursor.fetchone()

    if result:

        current_balance = float(result[0])

        if amount > current_balance:
            print("\nInsufficient Balance!")

        else:

            new_balance = current_balance - amount

            cursor.execute(
                "UPDATE accounts SET balance=%s WHERE account_no=%s",
                (new_balance, account_no)
            )

            cursor.execute("""
            INSERT INTO transactions
            (account_no, transaction_type, amount, balance_after_transaction, remarks)
            VALUES (%s,%s,%s,%s,%s)
            """, (
                account_no,
                "Withdraw",
                amount,
                new_balance,
                "Cash Withdrawal"
            ))

            connection.commit()

            save_transaction(
                account_no,
                "Withdraw",
                amount,
                new_balance,
                "Cash Withdrawal"
            )

            print("\nWithdrawal Successful!")
            print("Current Balance:", new_balance)

    else:
        print("\nAccount Not Found!")

    cursor.close()

def transfer_money():
    cursor = connection.cursor()

    from_account = input("Enter Sender Account Number: ")
    to_account = input("Enter Receiver Account Number: ")
    amount = float(input("Enter Transfer Amount: "))

    # Check sender balance
    cursor.execute(
        "SELECT balance FROM accounts WHERE account_no=%s",
        (from_account,)
    )
    sender = cursor.fetchone()

    if not sender:
        print("Sender Account Not Found!")
        cursor.close()
        return

    # Check receiver account
    cursor.execute(
        "SELECT balance FROM accounts WHERE account_no=%s",
        (to_account,)
    )
    receiver = cursor.fetchone()

    if not receiver:
        print("Receiver Account Not Found!")
        cursor.close()
        return

    sender_balance = float(sender[0])

    if sender_balance < amount:
        print("Insufficient Balance!")
        cursor.close()
        return

    receiver_balance = float(receiver[0])

    new_sender_balance = sender_balance - amount
    new_receiver_balance = receiver_balance + amount

    # Update balances
    cursor.execute(
        "UPDATE accounts SET balance=%s WHERE account_no=%s",
        (new_sender_balance, from_account)
    )

    cursor.execute(
        "UPDATE accounts SET balance=%s WHERE account_no=%s",
        (new_receiver_balance, to_account)
    )

    # Sender transaction
    cursor.execute("""
    INSERT INTO transactions
    (account_no, transaction_type, amount, balance_after_transaction, remarks)
    VALUES (%s,%s,%s,%s,%s)
    """, (
        from_account,
        "Transfer Out",
        amount,
        new_sender_balance,
        f"Transferred to {to_account}"
    ))

    # Receiver transaction
    cursor.execute("""
    INSERT INTO transactions
    (account_no, transaction_type, amount, balance_after_transaction, remarks)
    VALUES (%s,%s,%s,%s,%s)
    """, (
        to_account,
        "Transfer In",
        amount,
        new_receiver_balance,
        f"Received from {from_account}"
    ))

    connection.commit()

    # Update Excel files
    save_transaction(
        from_account,
        "Transfer Out",
        amount,
        new_sender_balance,
        f"Transferred to {to_account}"
    )

    save_transaction(
        to_account,
        "Transfer In",
        amount,
        new_receiver_balance,
        f"Received from {from_account}"
    )

    print("\nTransfer Successful!")
    print("Sender Balance:", new_sender_balance)
    print("Receiver Balance:", new_receiver_balance)

    cursor.close()

def view_transactions():
    cursor = connection.cursor()

    account_no = input("Enter Account Number: ")

    query = """
    SELECT transaction_id,
           transaction_type,
           amount,
           balance_after_transaction,
           transaction_date,
           remarks
    FROM transactions
    WHERE account_no=%s
    ORDER BY transaction_date
    """

    cursor.execute(query, (account_no,))
    records = cursor.fetchall()

    if records:

        print("\n========== TRANSACTION HISTORY ==========")

        for row in records:
            print("---------------------------------------")
            print("Transaction ID :", row[0])
            print("Type           :", row[1])
            print("Amount         :", row[2])
            print("Balance        :", row[3])
            print("Date           :", row[4])
            print("Remarks        :", row[5])

    else:
        print("\nNo Transactions Found!")

    cursor.close()

def check_balance():
    cursor = connection.cursor()

    account_no = input("Enter Account Number: ")

    query = """
    SELECT account_no, account_type, balance
    FROM accounts
    WHERE account_no = %s
    """

    cursor.execute(query, (account_no,))
    account = cursor.fetchone()

    if account:
        print("\n========== ACCOUNT DETAILS ==========")
        print("Account Number :", account[0])
        print("Account Type   :", account[1])
        print("Balance        :", account[2])
    else:
        print("\nAccount Not Found!")

    cursor.close()