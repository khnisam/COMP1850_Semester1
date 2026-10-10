# Worksheet 1.2: Task 2 Solution
from util import read_numbers
from statistics import median
import sys

numbers = read_numbers() 
if len(numbers) == 0:
    sys.exit("Error: no numbers provided")
else:
    maximum = max(numbers)
    minimum = min(numbers)
    average = (sum(numbers))/(len(numbers))
    numbers.sort()
    mid = median(numbers)
    print(f"Minimum = {minimum:.2f}")
    print(f"Maximum = {maximum:.2f}")
    print(f"Mean = {average:.2f}")
    print(f"Median = {mid:.2f}")
        

    

    