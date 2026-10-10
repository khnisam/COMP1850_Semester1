# Worksheet 1.2: Task 2 Solution
from util_extension import read_file
from statistics import median
from statistics import stdev
import sys


numbers = read_file()
print(numbers)
if len(numbers) == 0:
    print("Error: No numbers entered in file")
    sys.exit("Error!")
else:
    maximum = max(numbers)
    minimum = min(numbers)
    average = (sum(numbers))/(len(numbers))
    numbers.sort()
    mid = median(numbers)
    stdv = stdev(numbers)
    print(f"Minimum = {minimum:.2f}")
    print(f"Maximum = {maximum:.2f}")
    print(f"Mean = {average:.2f}")
    print(f"Median = {mid:.2f}")
    print(f"Standard Deviation = {stdv:.2f}")



        

    

    