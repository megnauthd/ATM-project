# ATM System in Python
Link to replit project https://replit.com/@megnauthdhanra1/ATM-project#main.py

## Project Overview

This project is an implementation of an ATM (Automated Teller Machine) system using Object-Oriented Programming (OOP) principles in Python. The purpose of this project is to simulate the core functionalities of an ATM, such as generating a PIN, changing a PIN, checking balance, withdrawing money, and depositing money, all through a command-line interface. This project is designed to reinforce understanding of key OOP concepts, including classes, objects, and method handling.

## Features

- **Generate PIN**: Allows users to create a 4-digit PIN for securing their account.
- **Change PIN**: Permits users to change their existing PIN after verifying their current one.
- **Check Balance**: Enables users to check their account balance after entering their PIN.
- **Withdraw Money**: Lets users withdraw money from their account after providing a pin, provided they have sufficient funds.
- **Deposit Money**: Allows users to deposit money into their account after they enter a pin, with the requirement that the amount is a multiple of 100.

## How It Works

### 1. Initialization

When the ATM system starts, it initializes with:
- `__pin`: A private attribute to store the user's PIN, initially set to `None`.
- `__balance`: A private attribute to store the user's balance, initially set to `0`.

The system then automatically calls the `__menu()` method, which presents the user with various options to interact with the ATM.

### 2. Menu Options

The `__menu()` method displays the following options:
- Generate PIN
- Change PIN
- Check Balance
- Withdraw Money
- Deposit Money
- Exit

The user selects an option by entering the corresponding number, and the system executes the appropriate method based on the user's choice.

### 3. Generate PIN

- The `__generate_pin()` method allows the user to create a new 4-digit PIN.
- If the user has already set a PIN, the system prevents them from generating a new one and directs them to the `Change PIN` option instead.

### 4. Change PIN

- The `__change_pin()` method allows the user to change their existing PIN.
- The user must first verify their current PIN before entering and confirming a new PIN.

### 5. Check Balance

- The `__check_balance()` method allows the user to view their current balance after successfully entering their PIN.

### 6. Withdraw Money

- The `__withdraw()` method lets the user withdraw money from their account.
- The withdrawal amount must be a multiple of 100 and not exceed the current balance.

### 7. Deposit Money

- The `__deposit()` method allows the user to deposit money into their account.
- The deposit amount must be a positive multiple of 100.

### 8. Exit

- The user can exit the ATM system by selecting the `Exit` option from the menu.

