class UPI:
    def __init__(self):# to initialize 
        self.balance = 0  # Initialize balance to 0 when ATM object is created
        self.pin = "1234"  # Set default PIN
        self.transactions = []  # List to store transactions

    def check_balance(self):# Function for checking the balance
        """Check account balance"""
        print(f"Your balance is: INR{self.balance}")  # Display current balance

    def deposit(self, amount):# To deposit amount in the account
        """Deposit money into account"""
        self.balance += amount  # Increase balance by deposited amount
        self.transactions.append(f"Deposit: INR{amount}")  # Add deposit transaction to list
        print(f"INR{amount} deposited successfully.")
        self.check_balance()  # Show updated balance after deposit

    def withdraw(self, amount):# To withdraw amount from account
        """Withdraw money from account"""
        if amount > self.balance:  # Check if withdrawal amount exceeds balance
            print("Insufficient funds.")  # Print message if insufficient funds
        else:
            self.balance -= amount  # Deduct withdrawal amount from balance
            self.transactions.append(f"Withdrawal: INR{amount}")  # Add withdrawal transaction to list
            print(f"INR{amount} withdrawn successfully.")
            self.check_balance()  # Show updated balance after withdrawal

    def check_pin(self, pin):# For checking weather the pin is correct or not
        """Check PIN entered by user"""
        return pin == self.pin  # Return True if PIN is correct, False otherwise

    def reset_pin(self, new_pin):# For resetting the PIN
        """Reset PIN"""
        self.pin = new_pin
        print("PIN successfully reset.")

    def display_transactions(self):# To display past three transactions
        """Display past three transactions"""
        print("\nPast three transactions:")
        if len(self.transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in self.transactions[-3:]:
                print(transaction)

def main():
    atm = UPI()  # Initialize UPI object

    while True:
        print("\nWelcome to the UPI!")  # Display ATM menu
        pin = input("Enter your PIN: ")  # Prompt user to enter PIN
        if atm.check_pin(pin):  # Check if entered PIN is correct
            while True:  # Inner loop for ATM operations
                print("\nUPI Menu:")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Reset PIN")
                print("5. Display Past 3 Transactions")
                print("6. Exit")
                choice = input("Enter your choice (1-6): ")  # Get user input for choice

                if choice == '1':
                    atm.check_balance()  # Call check_balance method
                elif choice == '2':
                    amount = float(input("Enter deposit amount: INR"))  # Get deposit amount from user
                    atm.deposit(amount)  # Call deposit method with the given amount
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: INR"))  # Get withdrawal amount from user
                    atm.withdraw(amount)  # Call withdraw method with the given amount
                elif choice == '4':
                    new_pin = input("Enter new PIN: ")  # Get new PIN from user
                    atm.reset_pin(new_pin)  # Call reset_pin method with the new PIN
                elif choice == '5':
                    atm.display_transactions()  # Call display_transactions method to display past three transactions
                elif choice == '6':
                    print("Thank you for using the UPI. Goodbye!")  # Exit message
                    break  # Exit inner loop
                else:
                    print("Invalid choice. Please enter a number from 1 to 6.")  # Print error message for invalid input
            break  # Exit outer loop
        else:
            print("Incorrect PIN. Please try again.")  # Print message for incorrect PIN

if __name__ == "__main__":
    main()
