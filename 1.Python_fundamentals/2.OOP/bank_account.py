class BankAccount:
    # Constructor to initialize the balance
    def __init__(self):
        self.balance = 0.0  # Initialize the balance to 0.0

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Add the deposit amount to the balance
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= (
                    amount  # Subtract the withdrawal amount from the balance
                )
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    # Method to get the current balance
    def get_balance(self):
        return self.balance  # Return the current balance


# Main method to interact with the BankAccount class
def main():
    # Create a BankAccount object
    account = BankAccount()

    # Deposit money into the account
    account.deposit(1000)  # Deposit $1000
    account.deposit(500)  # Deposit $500

    # Withdraw money from the account
    account.withdraw(300)  # Withdraw $300
    account.withdraw(2000)  # Try to withdraw more than the balance

    # Check the current balance
    print(f"Current balance: ${account.get_balance()}")


# Call the main method to run the program
if __name__ == "__main__":
    main()
