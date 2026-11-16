import random

# Read names from a file

with open("names.txt", "r") as infile:
    names = [ line.strip() for line in infile ]

number = int(input("Please enter a number ")) #This prompts the user to enter the number of random numbers generated.

random_list = [] # Creates a random number list, which will store the random numbers.
for num in range(number):
    random_Number = random.randint(0, len(names))
    random_list.append(random_Number)

    
duplicates = []   #Creates a duplicate list
seen = set() #Creates a dictionary for all the seen elements in list.
for i in random_list: #iterating over each element in the list. 
    if i in seen:
        duplicates.append(i) 
    else:
        seen.add(i)

if len(duplicates) == 0:
    for item in random_list:
        print(f"{names[item]}\n")


    
    


# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

# Display the chosen names, one per line
