from Account import *

class Bank():
    def __init__(self, hours, address, phone):
        self.accounts_dict = {}
        self.next_account_number = 0
        self.hours = hours
        self.address = address
        self.phone = phone
        
    def ask_for_valid_account_number(self):
        account_number = input("What is your account number?: ")
        
        try:
            account_number = int(account_number)
        except ValueError:
            raise AbortTransaction("The account number must be an integer")
        if account_number not in self.accounts_dict:
            raise AbortTransaction(f"There is no account {account_number}")
        return account_number
    
    def get_users_account(self):
        account_number = self.ask_for_valid_account_number()
        account = self.accounts_dict[account_number]
        self.ask_for_valid_password(account)
        return account
            
            
    def ask_for_valid_password(self, account):
         password = input("Please enter your password: ")
         account.check_password_match(password)
         
    def create_account(self, the_name, the_starting_amount, the_password):
        account = Account(the_name, the_starting_amount, the_password)
        new_account_number = self.next_account_number
        self.accounts_dict[new_account_number] = account
        # Increment to prepare for the next account to be created
        self.next_account_number += 1
        return new_account_number
    
    def open_account(self):
        print("*** Open Account ***")
        user_name = input("Whats your name?: ")
        user_starting_amount = input("How much money to start your account?: ")
        user_password = input("What password would you like to use for this account?: ")
        user_account_number = self.create_account(user_name, user_starting_amount, user_password)
        print(f"Your new account number is: {user_account_number}")
        
    def close_account(self):
        print("*** Close Account ***")
        user_account_number = self.ask_for_valid_account_number()
        account = self.accounts_dict[user_account_number]
        self.ask_for_valid_password(account)
        the_balance = account.get_balance()
        print(f"You had {the_balance} in your account, which is being returned to you.")
        del self.accounts_dict[user_account_number]
        print("Your account is closed.")
    
    def balance(self):
        print("*** Get Balance ***")
        account = self.get_users_account()
        the_balance = account.get_balance()
        print(f"Your balance is: {the_balance}")
            
    def deposit(self):
        print("*** Deposit ***")
        account = self.get_users_account()
        deposit_amount = input("Please enter amount to deposit: ")
        the_balance = account.deposit(deposit_amount)
        print(f"Deposited {deposit_amount}")
        print(f"Your new balance is {the_balance}")
            
            
    def withdraw(self):
        print("*** Withdraw ***")
        account = self.get_users_account()
        user_amount = input("Please enter the amount to withdraw: ")
        the_balance = account.withdraw(user_amount)
        print(f"Withdrew {user_amount}")
        print(f"Your new balance is {the_balance}")
        
    def get_info(self):
        print('Hours:', self.hours)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print('We currently have', len(self.accounts_dict), 'account(s) open.')
        
    # Special method for Bank administrator only
    def show(self):
        print("*** Show ***")
        print('(This would typically require an admin password)')
        for userAccountNumber in self.accounts_dict:
            oAccount = self.accounts_dict[userAccountNumber]
            print('Account:', userAccountNumber)
            oAccount.show()
            print()