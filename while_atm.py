#While loop example base on if_else_atm.py
balance = 500
repeat = "yes"

while repeat.lower() == "yes":
    action = input("Would you like to deposit or withdraw? ")
    amount = int(input("Please enter an amount: "))


    if action.lower() == "withdraw":
        if amount > balance:
            print("Insuffcient funds")
        else:
            balance = balance - amount
            print("Your remaining balance is: ", balance)
    elif action.lower() == "deposit":
        balance = balance + amount
        print("Your remaining balance is: ", balance)
    else:
        print("Please enter 'deposit' or 'withdraw'")

    repeat = input("Would you like to continue? yes or no: ")

print("Goodbye!")
