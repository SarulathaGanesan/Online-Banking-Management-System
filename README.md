# 🏦 Online Banking Management System

## 📌 Project Overview

The **Online Banking Management System** is a Python-based desktop application developed to simplify and manage basic banking operations. It provides a user-friendly graphical interface using Tkinter and stores customer, account, and transaction details in a MySQL database.

The system also maintains individual Excel transaction records for each bank account using OpenPyXL, making transaction tracking and record management easier.

## 🚀 Features

- **Customer Management:** Add, view, search, update, and delete customer details.
- **Account Management:** Create and manage bank accounts.
- **Deposit Money:** Deposit money into customer accounts.
- **Withdraw Money:** Withdraw money while checking available balance.
- **Fund Transfer:** Transfer money between bank accounts.
- **Balance Enquiry:** Check the current account balance.
- **Transaction History:** View account transaction details.
- **MySQL Integration:** Store and manage banking data using MySQL.
- **Excel Transaction Records:** Maintain separate Excel files for individual accounts.
- **Input Validation:** Validate user inputs and handle errors.
- **Graphical User Interface:** Interactive desktop application developed using Tkinter.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| MySQL | Database management |
| Tkinter | Graphical User Interface |
| OpenPyXL | Excel file management |
| MySQL Connector | Python-MySQL connectivity |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
ONLINE_BANKING_SYSTEM/
│
├── gui.py
├── main.py
├── database.py
├── config.py
├── excel.py
│
├── customer.py
├── customer_gui.py
├── view_customer_gui.py
│
├── account.py
├── account_gui.py
├── balance_gui.py
│
├── transaction.py
├── transaction_gui.py
├── reports.py
├── dashboard.py
├── login.py
│
├── transactions/
│
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/SarulathaGanesan/Online-Banking-Management-System.git
```

### 2. Navigate to the Project Folder

```bash
cd Online-Banking-Management-System
```

### 3. Install Required Libraries

```bash
pip install mysql-connector-python openpyxl
```

### 4. Configure MySQL Database

- Install and open MySQL Workbench.
- Create the required banking database.
- Create the necessary tables for customers, accounts, and transactions.
- Configure your MySQL host, username, password, and database name in `config.py`.

**Note:** Keep your database credentials private. Do not upload `config.py` or expose your MySQL password on GitHub.

### 5. Run the Application

```bash
python gui.py
```

## 💾 Data Storage

- Customer and account information are stored in the MySQL database.
- Deposit, withdrawal, and transfer details are recorded in the transactions table.
- Individual Excel workbooks are maintained for each account to store transaction records.

## 🎯 Project Objective

The main objective of this project is to develop a simple and user-friendly banking application that automates basic banking operations, maintains accurate transaction records, and demonstrates database connectivity, Python GUI development, and Excel integration.

## 🔮 Future Enhancements

- Online banking support
- OTP-based authentication
- Improved security and password encryption
- Monthly transaction statements
- PDF statement generation

## 👩‍💻 Developer

**Sarulatha Ganesan**

GitHub: [SarulathaGanesan](https://github.com/SarulathaGanesan)

---

⭐ If you find this project useful, feel free to explore the repository!
