# Non-OOP Bank
# Version 5
# Any number of accounts - with a list of dictionaries

accountList = []

def newAccount(aName, aBalance, aPassword):
    global accountList
    newAccountDict = {"name": aName, "balance": aBalance, "password": aPassword}
    accountList.append(newAccountDict)
    
def show(accountNumber):
    global accountList
    print(f"Account {accountNumber}")
    thisAccountDict = accountList[accountNumber]
    print(f"Name: {thisAccountDict['name']}")
    print(f"Balance: {thisAccountDict['balance']}")
    print(f"Password: {thisAccountDict['password']}")
    print()
    
def getBalance(accountNumber, password):
    global accountList
    thisAccountDict = accountList[accountNumber]
    if password != thisAccountDict['password']:
        print("Incorrect password")
        return None
    return thisAccountDict['balance']

###

###

# Create two sample accounts
print(f"Joe's account is account number: {len(accountList)}")
newAccount("Joe", 100, "soup")

print(f"Mary's account is account number: {len(accountList)}")
newAccount("Mary", 12345, "nuts")

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press n to create a new account")
    print("Press w to make a withdrawal")
    print("Press s to show all accounts")
    print("Press q to quit")
    print()
    
    action = input("What do you want to do?: ").lower()
    action = action[0]
    print()
    
    if action == "b":
        print("Get Balance:")
        userAccountNumber = int(input("Please enter your account number: "))
        userPassword = input("Please enter the password: ")
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print(f"Your balance is: {theBalance}")
    elif action == "d":
        print("Deposit:")
        userAccountNumber = int(input("Please enther the account number: "))
        userDepositAmount = int(input("Please enter amount to deposit: "))
        userPassword = input("Please enter the password: ")
        
###

###

print("Done")