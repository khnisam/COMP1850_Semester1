# Week 1.7, Session 1: Task 2 - unit test for process_data() 

# Write test functions for the values you have chosen in the equivalence classes
# for testing the functions

# Hint: you should test for empty list, list with a single value, list with multiple values
# and for positive and negative integers


from process_data import process_data


def test_empty_list():
    int = []
    assert process_data(int) == None
    
    
def test_one_int_list():
    int = [-1]
    assert process_data(int) == -1
    


def test_multiple_int_list():
    int = [-1, 0, 1]
    assert process_data(int) == 0

    
    
