# Worksheet 1.2: Task 2 Solution
from util import read_numbers
from statistics import median
import sys

numbers = read_numbers() 
if len(numbers) == 0:
    print("Error: no numbers provided")
    sys.exit("Error!")
else:
    maximum = max(numbers)
    minimum = min(numbers)
    average = (sum(numbers))/(len(numbers))
    numbers.sort()
    mid = median(numbers)
    print(f"Minimum = {minimum:.1f}")
    print(f"Maximum = {maximum:.1f}")
    print(f"Mean = {average:.1f}")
    print(f"Median = {mid:.1f}")
        

    

    