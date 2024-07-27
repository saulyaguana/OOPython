# Non-OOP
# Bank 2
# Single account

accountName = ""
accountBalance = 0
accountPassword = ""


def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password


def show():
    global accountName, accountBalance, accountPassword
    print(f"Name: {accountName}")
    print(f"Balance: {accountBalance}")
    print(f"Password: {accountPassword}")
    print()


def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print("Incorrect Password")
        return None
    return accountBalance


def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print(f"You cannot deposit a negative amount!")
        return None
    if password != accountPassword:
        print("Incorrect Password")
        return None
    accountBalance += amountToDeposit
    return accountBalance


def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print("You cannot withdraw a negative amount")
        return None
    if password != accountPassword:
        print("Incorrect Password for this account")
        return None
    if amountToWithdraw > accountBalance:
        print("You cannot withdraw more than you have in your account")
        return None
    accountBalance -= amountToWithdraw
    return accountBalance


#################

newAccount("Alan", 200, "advancedW")  # create an account

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press w to make a withdraw")
    print("Press s to show the account")
    print("Press q to quit")
    print()

    action = input("What do you want to do?: ").lower()
    action = action[0]
    print()

    if action == "b":
        print("Get balance:")
        userPassword = input("Please enter the password: ")
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print(f"Your balance is: {theBalance}")
    elif action == "d":
        print("Deposit:")
        userDepositAmount = int(input("Please enter amount to deposit: "))
        userPassword = input("Please enter the password: ")

        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print(f"Your new balance is: {newBalance}")
    elif action == "w":
        amountToWithdraw = int(input("Write the amount you want to withdraw: "))
        userPassword = input("Write your password: ")
        newWithdraw = withdraw(amountToWithdraw, userPassword)
        if newWithdraw is not None:
            print(f"Your new balance is: {newWithdraw}")
    elif action == "s":
        show()
    elif action == "q":
        break

print("Done")
