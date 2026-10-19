# Week 4, Session 1: 

# You are given an incomplete function isBond with a docstring. Your task
# is to complete the function based on the details in the docstring.

target = [0,0,7]

def isBond(intList,target):
    """
    This function accepts a list of integers and returns True if the
    sequence 0, 0, 7 appears in the list, in that order. Return False
    otherwise. The numbers do not need to be consecutive, but must appear
    in the specified order.
    """
    count = 0
    for num in intList:
        if (count < len(target)) and (num == target[count]):
            count = count + 1
        else:
            continue

    if count == 3:
        return True
    else:
        return False


    # pass is a Python keyword used as a placeholder for future code,
    # meaning you need to delete pass to write your code.
    # Nothing happens when pass is executed.

    

# Check if the following lines of code produce the correct output
print(isBond([1, 2, 4, 0, 0, 7, 5], target))   # True
print(isBond([1, 0, 2, 4, 0, 5, 7], target))   # True
print(isBond([1, 7, 2, 0, 4, 5, 0], target))   # False
