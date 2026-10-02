"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Isam
"""

name = input("What is your name? ")
try:
    userName = int(name)
    print("That is not a valid name")
except ValueError:
    print(f"Welcome to LeedsBank's savings calculator {name}!")

    moneySaving = input("Enter how much money you would like to save every month. ")
    try:
        number = int(moneySaving)
        if number >= 0:
            yearlySaving = number * 12
            interestSaving = yearlySaving + (yearlySaving * 0.008)
            round(interestSaving, 2)
            print(f"You have chosen to save £{number} per month!")
            print(f"You will save £{yearlySaving} per annum!")
            print(f"Your total amount of money saved including interest will be £{interestSaving:.2f} per year")
        else:
            print("Invalid amount")
    except ValueError:
        print("Invalid amount")






