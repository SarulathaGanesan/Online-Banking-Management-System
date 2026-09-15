from database import connection

def dashboard():

    cursor = connection.cursor()

    # Total Customers
    cursor.execute("SELECT COUNT(*) FROM customers")
    total_customers = cursor.fetchone()[0]

    # Total Accounts
    cursor.execute("SELECT COUNT(*) FROM accounts")
    total_accounts = cursor.fetchone()[0]

    # Total Deposits
    cursor.execute("""
    SELECT IFNULL(SUM(amount),0)
    FROM transactions
    WHERE transaction_type='Deposit'
    """)
    total_deposit = cursor.fetchone()[0]

    # Total Withdrawals
    cursor.execute("""
    SELECT IFNULL(SUM(amount),0)
    FROM transactions
    WHERE transaction_type='Withdraw'
    """)
    total_withdraw = cursor.fetchone()[0]

    # Total Transfers
    cursor.execute("""
    SELECT IFNULL(SUM(amount),0)
    FROM transactions
    WHERE transaction_type='Transfer Out'
    """)
    total_transfer = cursor.fetchone()[0]

    print("\n========== BANK DASHBOARD ==========")

    print(f"Total Customers   : {total_customers}")
    print(f"Total Accounts    : {total_accounts}")
    print(f"Total Deposits    : ₹{total_deposit}")
    print(f"Total Withdrawals : ₹{total_withdraw}")
    print(f"Total Transfers   : ₹{total_transfer}")

    cursor.close()