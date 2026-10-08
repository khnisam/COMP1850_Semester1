# Week 1.2, Session 2: Task 3
# Simple Voting Eligibility Checker

# Prompt the user to enter their age

age = input("Enter your age: ")
try:
    userAge = int(age)
    if userAge >= 18: 
        print("You are eligible to vote.")
    elif userAge < 0:
        print("That is not a valid age.")
    else:
        print("You are not eligible to vote yet.")
except ValueError:
    print("That is not a number.")

    


