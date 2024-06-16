
from bank import Bank ,AbortTransaction

class Main:
    @staticmethod
    def run():
        bank = Bank("9 AM - 5 PM", "123 Bank St.", "555-555-5555")

        while True:
            print("\nWelcome to the bank. Choose an option:")
            print("1: Create an account")
            print("2: Check balance")
            print("3: Deposit")
            print("4: Withdraw")
            print("5: Show all accounts")
            print("6: Bank information")
            print("7: Exit")

            option = input("Enter option: ").strip()

            if option == "1":
                name = input("Enter your name: ")
                while True:
                  balance = input("Enter initial balance: ")
                  try:
                       balance = int(balance)
                       break
                  except ValueError:
                       print("Wrong type amount")
                while True:
                    password = input("Set a password: ")
                    if Main.set_strong_password(password):
                        break
                    else:
                        print("Password should be strong with including at least 5 characters having letters and numbers")
                bank.create_account(name, int(balance), password)
            elif option == "2":
                try:
                    bank.user_balance()
                except AbortTransaction as e:
                    print(e)
            elif option == "3":
                try:
                    bank.deposit()
                except AbortTransaction as e:
                    print(e)
            elif option == "4":
                try:
                    bank.withdraw()
                except AbortTransaction as e:
                    print(e)
            elif option == "5":
                bank.show_all_accounts()
            elif option == "6":
                bank.get_info()
            elif option == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    @staticmethod
    def set_strong_password(password):
        if len(password)<5:
            return False
        if not re.search("[a-zA-Z]", password):
            return False
        if not re.search("[0-9]",password):
            return False
        return True


# Run the main interface
if __name__ == "__main__":
    Main.run()


