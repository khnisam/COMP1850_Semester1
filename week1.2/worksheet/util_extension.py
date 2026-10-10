"""
Utility functions for Worksheet 1.2.
"""
import sys

def read_numbers():
    """
    Prompts the user to enter a series of numbers on a single line,
    separated from each other by spaces.

    Returns a list of float values corresponding to the numbers that were
    input by the user.
    """
    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    return numbers

def read_file():
    with open("/workspaces/COMP1850_Semester1/week1.2/worksheet/numbers.txt", "r") as file:
        numbers = []
        for line in file:
            number = line
            try:
                value = float(number)
                numbers.append(value)
            except ValueError:
                print("numbers.txt contains value(s) that aren't of the same type.")
                sys.exit("Error!")
    return numbers





            
