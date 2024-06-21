from account import Account, AbortTransaction

class Bank:
    def __init__(self, hours, address, phone):
        self.accounts = {}
        self.next_account_number = 0
        self.hours = hours
        self.address = address
        self.phone = phone


    def create_account(self, name, balance, password):
        account = Account(name, balance, password)
        self.accounts[self.next_account_number] = account
        print(f"Account created successfully. Your account number is {self.next_account_number}.")
        self.next_account_number += 1

    def validate_account_number(self):
        account_number = input("Enter account number: ")
        try:
            account_number = int(account_number)
        except ValueError:
            raise AbortTransaction("Invalid account number.")

        if account_number not in self.accounts:
            raise AbortTransaction(f"Account number {account_number} not registered.")

        return account_number

    def get_info(self):
        print(f"We are open during the following hours: {self.hours}")
        print(f"We have {len(self.accounts)} accounts opened.")
        print(f"Our address is {self.address}")
        print(f"Please contact us at {self.phone}")

    def get_user_account(self):
        account_number = self.validate_account_number()
        account = self.accounts[account_number]
        self.validate_password(account)
        return account

    def validate_password(self, account):
        password = input("Enter password: ")
        account.check_password_match(password)


    def user_balance(self):
        account = self.get_user_account()
        balance = account.get_balance()
        print(f"The balance is {balance}")

    def deposit(self):
        account = self.get_user_account()
        deposit_amount = input("Enter amount to deposit: ")
        account.deposit(deposit_amount)

    def withdraw(self):
        account = self.get_user_account()
        withdraw_amount = input("Enter amount to withdraw: ")
        account.withdraw(withdraw_amount)

    def show_all_accounts(self):
        for account_number, account in self.accounts.items():
            print(f"Account Number: {account_number}")
            account.show()

