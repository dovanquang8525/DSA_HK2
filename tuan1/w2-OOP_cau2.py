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
    
# def main():
class Account:
    def __init__(self):
        self.bank_accounts = []
        
        # self.__account_number = account_number
        # self.__owner_name = owner_name
        # self.__balance = balance
        # self.__password = "1234"

    # create account
    def createAccount(self):
        account_number = input("Enter account number: ")
        owner_name = input("Enter name: ")
        balance = float(input("Enter balance: "))
        password = input("Password: ")
        
        account = {
            "account_number": account_number,
            "owner_name": owner_name,
            "balance": balance,
            "password": password
        }
        
        self.bank_accounts.append(account)
        print("Created successful!")
    # pass
    def getPassword(self):
        return 'jsdhfsdhfoidniep'
    # information
    def info(self):
        print("\n--- ACCOUNT INFO ---")
        print(f"Account number: {self.__account_number}")
        print(f"Owner name: {self.__owner_name}")
        print(f"Balance: {self.__balance}")
        print(f"Pass: {self.__password}")
    # display_info
    def display_info(self):
        account_number = input("Enter account number: ")
        for acc in self.bank_accounts:
            if acc.account_number != account_number:
                print("Nothing here")
            else:
                # print(acc)
                acc.info()
    # deposit
    def deposit(self):
        money = float(input("Enter money: "))
        if money > 0:   
            account_number_in = input("Enter account number: ")
            for account in self.bank_accounts:
                if account['account_number'] != account_number_in:
                    print("Nothing here")
                    break
                else:
                    account['balance'] += money
                    print("Done")
    # Withdraw
    def withdraw(self, money):
        if money > 0 and money < self.__balance:
            self.__balance -= money
            print(f"Balance: {self.__balance}")
    # get_balance
    def getBalance(self, acc):
        for acc in self.accounts:
            if acc.account_number == self.__account_number:
                print(f"Balance: {self.__balance}")
            else:
                print("Not found")
    # transfer
    def transfer():
        print("NONE")
    # list account
    def listAllAccount(self):
        if not self.bank_accounts:
            print("Khong co tai khoan ngan hang nao")
        for account in self.bank_accounts:
            print(f"Account Number: {account['account_number']}\nOwner Name: {account['owner_name']}\nBalance: {account['balance']}")
        
    def run(self):
        while True:
            display_banking_menu()
            choice = int(input("Your choice 1-8: "))
            if choice == 1:
                self.createAccount()
                # Account.getPassword(password)
            elif choice == 2:
                self.display_info()
            elif choice == 3:
                self.deposit()
            elif choice == 4:
                money = int(input("Enter money: "))
                Account.withdraw(money)
            elif choice == 5:
                account_number = input("Enter account number: ")
                Account.getBalance(account_number)
            elif choice == 6:
                Account.transfer()
            elif choice == 7:
                self.listAllAccount()
            elif choice == 8:
                break

if __name__ == '__main__':
    BankAccountManager = Account()
    BankAccountManager.run()