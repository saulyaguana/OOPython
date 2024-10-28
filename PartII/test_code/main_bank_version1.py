# Test program using accounts
# Version 1, using explicit variables for each Account object

# Bring all the code from the Account class file
from Account import *

# Create two accounts
o_joes_account = Account("Joe", 100, "JoesPassword")
print("Created an account for Joe")

o_marys_account = Account("Mary", 12345, "MarysPassword")
print("Created an account for Mary")

o_joes_account.show()
o_marys_account.show()
print()

# Call some methods on the different accounts
print("Calling methods of the two accounts...")
o_joes_account.deposit(50, "JoesPassword")
o_marys_account.withdraw(345, "MarysPassword")
o_marys_account.deposit(100, "MarysPassword")

# Show the accounts
o_joes_account.show()
o_marys_account.show()

# Create another account with information from the user
print()
user_name = input("What is the name for the new user account?: ")
user_balance = int(input("What is the starting balance for this account?: "))
user_password = input("What is the password you want to use for this account?: ")

o_new_account = Account(user_name, user_balance, user_password)

# Show the newly created account
o_new_account.show()

# Let's deposit 100 into the new account
o_new_account.deposit(100, user_password)
users_balance = o_new_account.get_balance(user_password)
print()
print(f"After depositing 100, the user's balance is: {users_balance} - {o_new_account.balance}")