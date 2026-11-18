
import matplotlib.pyplot as plt  # import library

x = [ k for k in range(15) ]  # create a range for the data
y = [ pow(k,3) for k in x ]      # create a simple function y=x^3

plt.plot(x,y)  # create a 2d plot

plt.xlabel('x')
plt.ylabel('y=x^3')  # annotate

plt.show()  # display

# Test the example as is on the slides
# - Modify the data and the range
# - Plot in different ways
# Read matplotlib documentation
# - Test some other plotting functions
