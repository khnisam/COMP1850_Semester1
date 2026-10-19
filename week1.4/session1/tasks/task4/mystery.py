# Week 4, Session 1

# You are given the function mystery_func. 
# Inspect the code in the function
# Your task is to write a corresponding docstring
# - what the function does 
# - what is the input data and type
# - what is the return value and type


# function implementation

def mystery_func(string): #input data type is a sentence and string
    upper = 0 #defines the number of uppercase characters in string
    lower = 0 #defines the number of lowercase characters in string

    for ch in string:
        if ch.isupper(): #checks if index in string is either uppercase or lowercase, if upper then increment upper
            upper += 1
        if ch.islower(): #checks if index in string is lower, if lower then increment lower
            lower += 1
    return (upper, lower) #returns the number of lowercase and uppercase characters. This will be integer




# testing

print(mystery_func("abc"))
print(mystery_func("The quick Brown Fox!"))
print(mystery_func("012345"))
print(mystery_func("ABC"))


# Can you predict the output of the following lines of code?
# Uncomment the lines of code one by one and run the program
# to see if you are right?

# print(mystery_func("X"))
print(mystery_func("[2, 3]"))
