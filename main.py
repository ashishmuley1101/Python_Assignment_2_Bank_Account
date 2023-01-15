
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

     # UC 2. Constructor with parameters: accountNumber, name and balance.
     def __init__(self, accountNumber, name, balance):
          self.accountNumber = accountNumber
          self.name = name
          self.balance = balance

     # UC 3. Deposit() method which manages the deposit actions.
     def Deposit(self, deposit):
          self.balance += deposit
          print("Amount Deposited :", deposit, "Rs.")
          print("Current Balance :", self.balance, "Rs.")


      # UC 4. Withdrawal() method  which manages withdrawal actions.
     def Withdrawal(self, withdrawal):

          if (self.balance < withdrawal):
               print("Insufficient balance to withdrawal...!")
          else:
               self.balance -= withdrawal
               print("Amount Withdrawal :", withdrawal, "Rs.")
               print("Current Balance :", self.balance, "Rs.")

     # UC 5. bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
     def bankFees(self):
          self.balance = self.balance - ((self.balance * 5 )/100)
          print("Current Balance :", self.balance, "Rs.")

     # UC 6. display() method to display account details.
     def display(self):
          print("Account Number : ", self.accountNumber)
          print("Account Holder Name : ", self.name)
          print("Account Balance : ", self.balance, "Rs.")





