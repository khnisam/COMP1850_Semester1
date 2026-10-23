# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except

with open("../images/feep.pgm", "r") as infile:
    data1 = infile.readline().strip()
    data2 = infile.readline().strip()
    max_gray = int(infile.readline().strip())

    with open("../images/feep_inverted.pgm", "w") as outfile:
        outfile.write(f"{data1}\n")
        outfile.write(f"{data2}\n")
        outfile.write(f"{max_gray}\n")

        for line in infile:
            string = line.strip().split()
            for i in range(len(string)):
                original_pixel_value = int(string[i])
                invert_pixel_value = max_gray - original_pixel_value
                string[i] = invert_pixel_value
        
            string_line = " ".join(str(item) for item in string)
            outfile.write(string_line + "\n")
        
        
        
    
    







# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value


# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"