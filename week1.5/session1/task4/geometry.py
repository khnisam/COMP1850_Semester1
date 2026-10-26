# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here

    def __init__(self, x_value, y_value):
        self.x = x_value
        self.y = y_value
    """
    Constructs an object
    """

    # Add distance() method here

    def distance(self):
        return math.hypot(self.x,self.y)
    """
    Returns distance from this point to the origin
    """

    # Add distance_to() method here
    # (This will need a parameter representing another point)

    def distance_to(self, p2):
        return math.hypot(p2.x - self.x, p2.y - self.y)


    # circle class 

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = math.pi * (self.radius ** 2) 
        return round(result,2)

    def perimeter(self):
        result = 2 * math.pi * self.radius
        return round(result,2)
    

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
