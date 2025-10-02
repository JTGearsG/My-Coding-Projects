#Simple Atm
print("\n === Welcome To Simple ATM ===")
balance = 0

while True:

    print("\n1. Check Balance ")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    option = input("\nChoose an Option (1-4): ")
    if option == "4":
        print("Goodbye")
        break

    elif option == "1":
        print(f"Balance: {balance:.2f}")

    elif option == "2":
        try:
            amount_being_withdrawn = float(input("How much money do you want to withdraw?: "))
            if amount_being_withdrawn > balance:
                print("You cant withdraw more than your balance!")
            else:
                balance -= amount_being_withdrawn
                print(f"You Withdrew {balance:.2f}")
                print(f"Your balance is know: {balance:.2f}")
        except ValueError:
            print("Please enter a number.")

    elif option == "3":
        try:
            amount_being_deposited = float(input("How much money do you want to deposit?: "))
            if amount_being_deposited == 0:
                print("You cant deposit 0 dollars!")
            else:
                balance += amount_being_deposited
                print("Money Successfully Deposited!")
                print(f"Your balance is know: {balance:.2f}")
        except ValueError:
            print("Please enter a number.")
    else:
        print("Please choose a valid option! (1-4)")















