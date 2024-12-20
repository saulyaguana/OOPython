class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password
        
    def deposit(self, amount_to_deposit, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None
        if amount_to_deposit < 0:
            print("You cannot deposit a negative amount")
            return None
        self.balance += amount_to_deposit
        return self.balance
    
    def withdraw(self, amount_to_withdraw, password):
        if password != self.password:
            print("Incorrect password for this account")
            return None
        
        if amount_to_withdraw < 0:
            print("You cannot withdraw a negatice amount")
            return None
        
        if amount_to_withdraw > self.balance:
            print("You cannot withdraw more than you have in your account")
            return None
        
        self.balance -= amount_to_withdraw
        return self.balance
    
    def get_balance(self, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None
        return self.balance
    
    # Added for debugging
    def show(self):
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")
        print(f"Password: {self.password}")
        print()