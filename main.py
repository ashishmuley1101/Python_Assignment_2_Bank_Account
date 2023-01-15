
# Exercise 1.  Bank Account class :-
# UC1. Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# UC2. Create a constructor with parameters: accountNumber, name, balance.
# UC3. Create a Deposit() method which manages the deposit actions.
# UC4. Create a Withdrawal() method  which manages withdrawals actions.
# UC5. Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# UC6. Create a display() method to display account details.
# UC7. Give the complete code for the  BankAccount class.


# UC 1. BankAccount class which represents a bank account, having as attributes: accountNumber, name and balance.
class BankAccount:
     # attributes
     accountNumber = 0
     name = ""
     balance = 0