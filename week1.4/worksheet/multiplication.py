
def multiplication(x, y):

    if y == 1:
        return x * 1

    return (x + (multiplication(x,y-1)))

print(multiplication(10,1))