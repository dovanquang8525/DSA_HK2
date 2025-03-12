# Câu 2  
# Xây dựng hệ thống tài khoản ngân hàng với các yêu cầu: 
# • Tạo class Account với các thuộc tính: account_number, owner_name, balance 
# • Tạo các phương thức:  
# o deposit(): Nạp tiền 
# o withdraw(): Rút tiền (có kiểm tra số dư) 
# o get_balance(): Xem số dư 
# o transfer(): Chuyển tiền sang tài khoản khác 
# • Áp dụng tính đóng gói để bảo vệ các thuộc tính 
# • Tạo phương thức để in thông tin tài khoản 
def display_banking_menu():
    print("\n=== BANKING SYSTEM ===")
    print("1. Create new account")
    print("2. Display account info")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check balance")
    print("6. Transfer money")
    print("7. List all accounts")
    print("8. Exit\n")
    # return input("Enter your choice 1-7")

class Account:
    def __init__(this, accountNumber, ownerName, balance):
        this.__accountNumber = accountNumber
        this.__ownerName = ownerName
        this.__balance = balance
        this.__password = '1234'
    def __init__(this):
        this.bank_accounts = []
    def createAccount(this):
        accountNumber = input("Enter account number: ")
        ownerName = input("Enter owner name: ")
        balance = float(input("Enter balance: "))
        password = input("Enter password: ")
        
        account = [{
            "accountNumber" : accountNumber,
            "ownerName": ownerName,
            "balance" : balance,
            "password" : password
        }]
        
        this.bank_accounts.append(account)
        print("Done")
    def getPassword(this):
        return this.__password + "fdsfouefbwej"
    def displayAccountInfo(this):
        account = input("Enter Account number: ")
        for acc in this.bank_accounts:
            if acc["accountNumber"] == account:
                print(f"Account Number: {acc['account_number']}\nOwner Name: {acc['owner_name']}\nBalance: {acc['balance']}")
            else:
                print("None")
    def deposit(this):
        money = float(input("Enter the money: "))
        if money > 0:
            account_number = input("Enter Account number: ")
            for acc in this.bank_accounts:
                if acc["accountNumber"] == account_number:
                    acc["balance"] += money
                else:
                    print("Not Found !!")
    def withdraw(this):
        money = float(input("Enter the money: "))
        if money > 0:
            account_number = input("Enter Account number: ")
            for acc in this.bank_accounts:
                if acc["accountNumber"] == account_number:
                    acc["balance"] -= money
                else:
                    print("Not found !!")
    def getBalance(this):
        account = input("Enter Account number: ")
        for acc in this.bank_accounts:
            if acc["accountNumber"] == account:
                print(f"Account number: {acc["accountNumber"]}")
                print(f"Owner name: {acc["ownerName"]}")
                print(f"Balance: {acc["balance"]}")
            else:
                print("Not Found")
    def listAllAccount(this):
        if not this.bank_accounts:
            print("Notthing here")
        for acc in this.bank_accounts:
            print(f"Account number: {acc["accountNumber"]}")
            print(f"Owner name: {acc["ownerName"]}")
            print(f"Balance: {acc["balance"]}")
            print(f"pass: {acc["password"]}")
    def run(this):
        while True:
                display_banking_menu()
                choice = int(input("Your choice 1-8: "))
                if choice == 1:
                    this.createAccount()
                    # Account.getPassword(password)
                elif choice == 2:
                    this.displayAccountInfo()
                elif choice == 3:
                    this.deposit()
                elif choice == 4:
                    this.withdraw()
                elif choice == 5:
                    this.getBalance()
                elif choice == 6:
                    this.transfer()
                elif choice == 7:
                    this.listAllAccount()
                elif choice == 8:
                    break
account = Account()
account.run()