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
    def __init__(self, accountNumber, ownerName, balance):
        self.__accountNumber = accountNumber
        self.__ownerName = ownerName
        self.__balance = balance
        # self.__password = "1234"
    def accountInfo(self):
        print(f"Account Number: {self.__accountNumber}")
        print(f"Ower Name: {self.__ownerName}")
        print(f"Balance: {self.__balance}")

class Management:
    def __init__(self):
        self.accounts = []
    def createAccount(self, account):
        if account not in self.accounts:
            self.accounts.append(account)
            print("Created successful")
        else:
            print("FAIL")
    def displayAccountInfo():
        Account.accountInfo()

while True:
    display_banking_menu()
    choice = int(input("Your choice 1-8: "))
    if choice == 1:
        accountNumber = input("Enter account number: ")
        ownerName = input("Enter ower name: ")
        balance = float(input("Enter Balance: "))
        Management.createAccount(Account(accountNumber, ownerName, balance))
    elif choice == 2:
        Management.displayAccountInfo()
    