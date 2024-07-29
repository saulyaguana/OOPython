# Non-OOP
# Bank 3
# Two accounts

account0Name = ''
account0Balance = ''
account0Password = ''
account1Name = ''
account1Balance = ''
account1Password = ''
nAccounts = 0

def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    
    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password
    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password
        
def show():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    
    if account0Name != '':
        print("Account 0")
        print(f"Name: {account0Name}")
        print(f"Balance: {account0Balance}")
        print(f"Password: {account0Password}")
        print()
    if account1Name != '':
        print("Account 1")
        print(f"Name: {account1Name}")
        print(f"Balance: {account1Balance}")
        print(f"Password: {account1Password}")
        print()
        
def getBalance(accountNumber, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    
    if accountNumber == 0:
        if password != account0Password:
            print("Incorrect password")
            return None
        return account0Balance
    if accountNumber == 1:
        if password != account1Password:
            print("Incorrect password")
            return None
        return account1Balance
    
def deposit(accountNumber, amountToDeposit, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    
    if accountNumber == 0:
        if amountToDeposit < 0:
            print(f"You cannot deposit a negative amount!")
            return None
        if password != account0Password:
            print("Incorrect Password")
            return None
        account0Balance += amountToDeposit
        return account0Balance
    elif accountNumber == 1:
        if amountToDeposit < 0:
            print(f"You cannot deposit a negative amount!")
            return None
        if password != account1Password:
            print("Incorrect Password")
            return None
        account1Balance += amountToDeposit
        return account1Balance
    
def withdraw(accountNumber, amountToWithdraw, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    
    if accountNumber == 0:
        if amountToWithdraw < 0:
            print("You cannot withdraw a negative amount")
            return None
        if password != account0Password:
            print("Incorrect password for this account")
            return None
        if amountToWithdraw > account0Balance:
            print("You cannot withdraw more than you have in your account")
            return None
        account0Balance -= amountToWithdraw
        return account0Balance
    elif accountNumber == 1:
        if amountToWithdraw < 0:
            print("You cannot withdraw a negative amount")
            return None
        if password != account1Password:
            print("Incorrect password for this account")
            return None
        if amountToWithdraw > account1Balance:
            print("You cannot withdraw more than you have in your account")
            return None
        account1Balance -= amountToWithdraw
        return account1Balance
        