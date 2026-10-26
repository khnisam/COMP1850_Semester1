# Week 1.5, Session 1: Task 3

import math

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



# Finally, add code here to demonstrate use of Point

p1 = Point(1.5, 2.0)
p2 = Point(3.0, 5.0)
print(p1.x)
print(p1.y)
print(p1.distance())
print(p1.distance_to(p2))
