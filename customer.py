from database import connection
def add_customer():
    cursor=connection.cursor()
    print("\n===== ADD NEW CUSTOMER =====")
    customer_name=input("Enter Customer Name: ")
    gender=input("Enter Gender(Male/Female/Other): ")
    date_of_birth=input("Enter Date of Birth(YYYY-MM-DD): ")
    phone=input("Enter Phone Number: ")
    email=input("Enter Email: ")
    aadhaar=input("Enter Aadhaar Number: ")
    address=input("Enter Address: ")

    query="""
    INSERT INTO customers
    (customer_name,gender,date_of_birth,phone,email,aadhaar,address)
    VALUES(%s,%s,%s,%s,%s,%s,%s)
    """
    values=(
        customer_name,
        gender,
        date_of_birth,
        phone,
        email,
        aadhaar,
        address
    )
    cursor.execute(query,values)
    connection.commit()

    print("\nCustomer Added Successfully!")
    cursor.close()

def view_customers():
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM customers")

    customers = cursor.fetchall()

    print("\n========== CUSTOMER LIST ==========")

    for customer in customers:
        print(customer)

    cursor.close()

def search_customer():
    cursor = connection.cursor()

    customer_id = input("Enter Customer ID: ")

    query = "SELECT * FROM customers WHERE customer_id = %s"

    cursor.execute(query, (customer_id,))

    customer = cursor.fetchone()

    if customer:
        print("\n========== CUSTOMER DETAILS ==========")
        print("Customer ID :", customer[0])
        print("Name        :", customer[1])
        print("Gender      :", customer[2])
        print("DOB         :", customer[3])
        print("Phone       :", customer[4])
        print("Email       :", customer[5])
        print("Aadhaar     :", customer[6])
        print("Address     :", customer[7])
        print("Created At  :", customer[8])
    else:
        print("Customer Not Found!")

    cursor.close()

def update_customer():
    cursor = connection.cursor()

    customer_id = input("Enter Customer ID to Update: ")

    query = "SELECT * FROM customers WHERE customer_id = %s"
    cursor.execute(query, (customer_id,))
    customer = cursor.fetchone()

    if customer:

        phone = input("Enter New Phone Number: ")
        email = input("Enter New Email: ")
        address = input("Enter New Address: ")

        update_query = """
        UPDATE customers
        SET phone=%s, email=%s, address=%s
        WHERE customer_id=%s
        """

        values = (phone, email, address, customer_id)

        cursor.execute(update_query, values)
        connection.commit()

        print("\nCustomer Updated Successfully!")

    else:
        print("\nCustomer Not Found!")

    cursor.close()

def delete_customer():
    cursor = connection.cursor()

    customer_id = input("Enter Customer ID to Delete: ")

    query = "SELECT * FROM customers WHERE customer_id = %s"
    cursor.execute(query, (customer_id,))
    customer = cursor.fetchone()

    if customer:

        confirm = input("Are you sure you want to delete this customer? (Y/N): ")

        if confirm.upper() == "Y":
            delete_query = "DELETE FROM customers WHERE customer_id = %s"
            cursor.execute(delete_query, (customer_id,))
            connection.commit()

            print("\nCustomer Deleted Successfully!")

        else:
            print("\nDelete Operation Cancelled.")

    else:
        print("\nCustomer Not Found!")

    cursor.close()