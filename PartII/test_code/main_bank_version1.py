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