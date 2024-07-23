# Non-OOP
# Bank Version 1
# Single account

accountName = "Joe"
accountBalance = 100
accountPassword = "soup"

while True:
    print()
    print("Press b to get the balance")
    print("Predd d to make a deposit")
    print("Press w to make a withdrawal")
    print("Press s to show the account")
    print("Press q to quit")
    print()

    action = input("What do you want to do?: ")
    action = action.lower()  # force to lowercase
    action = action[0]  # just use first letter
    print()

    if action == "b":
        print("Get Balance:")
        userPassword = input("Please enter the password: ")
        if userPassword != accountPassword:
            print("Incorrect password")
        else:
            print(f"Your balance is: {accountBalance}")
    elif action == "d":
        print("Deposit:")
        userDepositAmount = int(input("Please enter the amount to deposit: "))
        userPassword = input("Please enter the password: ")
        if userDepositAmount < 0:
            print("You cannot deposit a negative amount!")
        elif userPassword != accountPassword:
            print("Incorrect Password")
        else:  # OK
            accountBalance += userDepositAmount
            print(f"Your new balance is: {accountBalance}")
    elif action == "s":
        print("Show:")
        print(f"     Name: {accountName}")
        print(f"     Balance: {accountBalance}")
        print(f"     Password: {accountPassword}")
        print()
    elif action == "q":
        break
    elif action == "w":
        print("Withdraw:")

        userWithdrawAmount = int(input("Please enter the amount to withdraw: "))
        userPassword = input("Please enter the password: ")

        if userWithdrawAmount < 0:
            print("You cannot withdraw a negative amount")
        elif userPassword != accountPassword:
            print("Incorrect passwrod for this account")
        elif userWithdrawAmount > accountBalance:
            print("You cannot withdraw more than you have in your account")
        else:  # OK
            accountBalance -= userWithdrawAmount
            print(f"Your new balance is: {accountBalance}")

print("Done")
