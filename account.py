class AbortTransaction(Exception):
    '''Raise this exception to abort a bank transaction'''
    pass

class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def check_password_match(self, password):
        if password != self.password:
            raise AbortTransaction("Password incorrect")

    def get_balance(self):
        return self.balance

    def edit_account(self, new_name, new_password):
        self.show()
        self.name = new_name
        self.password = new_password

    def validate_amount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction("Invalid amount. Please enter a positive integer.")
        if amount <= 0:
            raise AbortTransaction("Amount must be positive.")
        return amount

    def deposit(self, amount_to_deposit):
        validated_amount = self.validate_amount(amount_to_deposit)
        self.balance += validated_amount
        print(f"{validated_amount} has been deposited to your account.")
        self.print_updated_balance()

    def print_updated_balance(self):
        print(f"Your updated balance is: {self.balance}")

    def withdraw(self, amount_to_withdraw):
        validated_amount = self.validate_amount(amount_to_withdraw)
        if self.balance < validated_amount:
            raise AbortTransaction("Insufficient funds.")
        self.balance -= validated_amount
        self.print_updated_balance()

    def show(self):
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")
