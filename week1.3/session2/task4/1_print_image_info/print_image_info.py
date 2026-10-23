# Week 1.3, Session 2: Print PGM image info

validWidth = True
validGrey = True
validHeight = True


with open("../images/feep.pgm", "r") as infile:
    next(infile) #skip ln1
    next(infile) #skip ln2
    next(infile) #skip ln3
    height = 0
    zeroCount = 0
    oneCount = 0
    for line in infile:
        data = line.strip().split()
        height = height + 1
        width = len(data)

        for i in data:
            try:
                element = int(i)
                if (element >= 0) and (element <= 15):
                    validGrey = True
                    continue
                else:
                    validGrey = False
                    break
            except ValueError:
                print("File Error")
                break

with open("../images/feep.pgm", "r") as infile:
    next(infile) #skip ln1
    next(infile) #skip ln2
    for line in infile:
        max_gray_value = line
        break

with open("../images/feep.pgm", "r") as infile:
    next(infile) #skip ln1
    for line in infile:
        pixels = line.strip().split()
        break

if width == int(pixels[0]):
    validWidth = True
else:
    validWidth = False

if height == int(pixels[1]):
    validHeight = True
else:
    validHeight = False

if validGrey == True and validWidth == True and validHeight == True:
    print("Valid Image")
elif validGrey == True and validWidth == True and validHeight == False:
    print("Invalid Height")
elif validGrey == True and validWidth == False and validHeight == True:
    print("Invalid Width")
elif validGrey == False and validWidth == True and validHeight == True:
    print("Invalid Pixel Values")

                

print(f"The Dimensions: {width} x {height}")
print(f"The Max Gray Value: {max_gray_value}")

    
        
        
            


# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)