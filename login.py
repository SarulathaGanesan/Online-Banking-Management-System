from database import connection

def login():

    cursor = connection.cursor()

    print("\n========== LOGIN ==========")

    username = input("Username : ")
    password = input("Password : ")

    query = """
    SELECT username, role
    FROM users
    WHERE username=%s AND password=%s
    """

    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    cursor.close()

    if user:
        print("\nLogin Successful!")
        print("Welcome", user[0])
        print("Role :", user[1])
        return True
    else:
        print("\nInvalid Username or Password!")
        return False