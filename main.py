import database
from customer import (
    add_customer,
    view_customers,
    search_customer,
    update_customer,
    delete_customer
)
from account import (
    create_account,
    deposit_money,
    withdraw_money,
    transfer_money,
    view_transactions,
    check_balance
    
)
from dashboard import dashboard
from login import login
if not login():
    exit()
while True:
    print("\n========== ONLINE BANKING MANAGEMENT SYSTEM ==========")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Search Customer")
    print("4. Update Customer")
    print("5. Delete Customer")
    print("6. Create Account")
    print("7. Deposit Money")
    print("8. Withdraw Money")
    print("9. Transfer Money")
    print("10. View Transaction History")
    print("11. Check Balance")
    print("12. Dashboard")
    print("13. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_customer()

    elif choice == "2":
        view_customers()

    elif choice == "3":
        search_customer()

    elif choice == "4":
        update_customer()
    
    elif choice == "5":
        delete_customer()

    elif choice == "6":
        create_account()

    elif choice == "7":
        deposit_money()

    elif choice == "8":
        withdraw_money()

    elif choice == "9":
        transfer_money()

    elif choice == "10":
        view_transactions()

    elif choice == "11":
        check_balance()

    elif choice == "12":
        dashboard()

    elif choice == "13":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")


