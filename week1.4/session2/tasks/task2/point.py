# Week 4, Session 2: Task 2

# We can specify a 2d coordinate point with a tuple p=(x,y)
# Complete two functions to compute the mid-point and distance between 2 points.
# The formula to find the mid point of two points = (x1+x2)/2, y = (y1+y2)/2. Return the midpoint as a point tuple.
# The formula to find the distance between the two points = √((x2 – x1)² + (y2 – y1)²). 
# You can use math.sqrt() to find the square root of a number. 

import math

def midpoint(p1,p2):
    # complete your code here to return a point tuple
    (x1, y1) = p1
    (x2, y2) = p2
    x_1 = x1
    x_2 = x2
    y_1 = y1
    y_2 = y2
    midX = (x_1 + x_2)/2
    midY = (y_1 + y_2)/2
    mid_point = (midX, midY)
    return mid_point

def length(p1,p2):
    # complete your code here to return a value
    (x1, y1) = p1
    (x2, y2) = p2
    x_1 = x1
    x_2 = x2
    y_1 = y1
    y_2 = y2
    distance = math.sqrt(pow(x_2 - x_1,2) + pow(y_2 - y_1,2))
    return distance
    

# Check if correct output is produced
m = midpoint( (0,0), (4,3) )    # mid = (2.0, 1.5)
d = length( (0,0), (4,3) )    # dist=5.0

print(f"Distance {d} Midpoint {m}")
