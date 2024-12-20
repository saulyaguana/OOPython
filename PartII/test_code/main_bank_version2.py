# Test program using accounts
# Version 2, using a list of accounts

# Bring in all the code from the Account class file
from Account import *

# Start off with an empty list of accounts
accounts_list = []

# Create two accounts
account = Account("Joe", 100, "JoesPassword")
accounts_list.append(account)
print("Joe's account number is 0")

account = Account("Mary", 12345, "MarysPassword")
accounts_list.append(account)
print("Mary's account number is 1")

accounts_list[0].show()
accounts_list[1].show()

# Call some methods on the different accounts
print("Calling methods of the two accounts...")
accounts_list[0].deposit(100, "JoesPassword")
accounts_list[1].withdraw(345, "MarysPassword")
accounts_list[1].deposit(100, "MarysPassword")

# Show the accounts
accounts_list[0].show()
accounts_list[1].show()

# Create another account with information from the user
print()
user_name = input("What is the name for the new user account?: ")
user_balance = int(input("What is the starting balance for this account?: "))
user_password = input("What is the password you want to use for this account?: ")

account = Account(user_name, user_balance, user_password)
accounts_list.append(account)

# Show the newly created user account
print("Created new account, account number is 2")
accounts_list[2].show()

# Let's deposit 100 into the new account
accounts_list[2].deposit(100, user_password)
users_balance = accounts_list[2].get_balance(user_password)
print()
print(f"After depositing 100, the user's balance is: {users_balance}")

# Show the new account
accounts_list[2].show()