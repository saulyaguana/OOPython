# Non-OOP Bank
# Version 4
# Any number of accounts - with lists

accountNamesList = []
accountBalancesList = []
accountPasswordsList = []


def newAccount(name, balance, password):
    global accountNamesList, accountBalancesList, accountPasswordsList

    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)


def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsList
    print(f"Account: {accountNumber}")
    print(f"Name: {accountNamesList[accountNumber]}")
    print(f"Balance: {accountBalancesList[accountNumber]}")
    print(f"Password: {accountPasswordsList[accountNumber]}")
    print()


def getBalance(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList

    if password != accountPasswordsList[accountNumber]:
        print("Incorrect password")
        return None
    return accountBalancesList[accountNumber]


#######


######

# Create two sample accounts
print(f"Joe's account is account number: {len(accountNamesList)}")
newAccount("Joe", 100, "soup")

print(f"Mary's account is account number: {len(accountNamesList)}")
newAccount("Mary", 12345, "nuts")

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press n to create a new account")
    print("Press w to make a withdraw")
    print("press s to show all ccounts")
    print("Press q to quit")
    print()

    action = input("What do you want to do?: ").lower()
    action = action[0]
    print()

    if action == "b":
        print("Get Balance:")
        userAccountNumber = int(input("Please enter your account number: "))
        userPassword = input("Please enter the password: ")
        theBlance = getBalance(userAccountNumber, userPassword)
        if theBlance is not None:
            print(f"The balance is: {theBlance}")

######

######
