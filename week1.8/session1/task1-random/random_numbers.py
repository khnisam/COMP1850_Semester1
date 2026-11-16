import random

# Get user to input how many random numbers they want

random_numbers = int(input("How many random numbers would you like ? "))
list = []
for number in range(random_numbers): #Generates numbers based on provided user input, via a for loop, then appends to a list.
    num = random.randint(1,100)
    list.append(num)

# Generate this many random numbers

# Write the random numbers to a file named random.txt, one number per line

with open("random.txt", "w") as outfile: #this will then write the randomly generated numbers, through a for loop that iterates through the list.
    for num in list:
        outfile.write(f"{num}\n")

