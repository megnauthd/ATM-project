class Atm:
    def __init__(self):
        self.__pin = None  # Encapsulated attribute for PIN
        self.__balance = 0  # Encapsulated attribute for Balance
        self.__menu()  # Call the menu method to start the ATM interface

    def __menu(self):
        while True:
            print("\n---- ATM Menu ----")
            print("1. Generate PIN")
            print("2. Change PIN")
            print("3. Check Balance")
            print("4. Withdraw Money")
            print("5. Deposit Money")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.__generate_pin()
            elif choice == '2':
                self.__change_pin()
            elif choice == '3':
                self.__check_balance()
            elif choice == '4':
                self.__withdraw()
            elif choice == '5':
                self.__deposit()
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def __get_pin(self):
        """Prompt the user to enter a 4-digit PIN and validate it."""
        while True:
            pin = input("Enter a 4-digit PIN: ")
            if len(pin) == 4 and pin.isdigit():
                return pin
            else:
                print("Invalid PIN. Please enter exactly 4 digits.")

    def __verify_pin(self):
        """Prompt the user to enter the current PIN and validate it."""
        entered_pin = input("Enter your current PIN: ")
        if entered_pin == self.__pin:
            return True
        else:
            print("Incorrect PIN.")
            return False

    def __generate_pin(self):
        """Allow the user to generate a new 4-digit PIN if one is not already set."""
        if self.__pin is not None:
            print("PIN is already set. Please use the option to change your PIN.")
            return

        print("Generate a new PIN:")
        pin = self.__get_pin()
        confirm_pin = input("Confirm your PIN: ")

        if pin == confirm_pin:
            self.__pin = pin
            print("PIN successfully generated.")
        else:
            print("PINs do not match. Please try again.")

    def __change_pin(self):
        """Allow the user to change their PIN."""
        if self.__pin is None:
            print("No PIN set. Please generate a PIN first.")
            return

        if self.__verify_pin():
            print("Enter a new PIN:")
            new_pin = self.__get_pin()
            confirm_new_pin = input("Confirm your new PIN: ")

            if new_pin == confirm_new_pin:
                self.__pin = new_pin
                print("PIN successfully changed.")
            else:
                print("New PINs do not match. Please try again.")

    def __check_balance(self):
        """Allow the user to check their balance after verifying the PIN."""
        if self.__verify_pin():
            print(f"Your current balance is: ${self.__balance}")
        else:
            print("Unable to verify PIN. Access denied.")

    def __withdraw(self):
        """Allow the user to withdraw money after verifying the PIN."""
        if self.__verify_pin():
            amount = int(
                input("Enter amount to withdraw (multiple of 100): "))
            if amount % 100 != 0:
                print("Invalid amount. Please enter a multiple of 100.")
            elif amount > self.__balance:
                print("Insufficient balance.")
            else:
                self.__balance -= amount
                print(f"${amount} withdrawn successfully. Your new "
                      f"balance is: ${self.__balance}")
        else:
            print("Unable to verify PIN. Access denied.")

    def __deposit(self):
        """Allow the user to deposit money after verifying the PIN."""
        if self.__verify_pin():
            amount = int(input("Enter amount to deposit (multiple of 100): "))
            if amount <= 0 or amount % 100 != 0:
                print("Invalid amount. Please enter a positive multiple of 100.")
            else:
                self.__balance += amount
                print(f"${amount} deposited successfully. Your new "
                      f"balance is: ${self.__balance}")
        else:
            print("Unable to verify PIN. Access denied.")

# Example instantiation of the ATM class
atm = Atm()
