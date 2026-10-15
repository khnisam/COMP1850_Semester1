# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input

sequence = [0]
for i in range(1,L):
    trial = sequence[i-1] - (L - (L-i))
    if (trial > 0) and (trial not in sequence):
        a = sequence[i-1] - (L - (L-i))
        sequence.append(a)
    else:
        a = sequence[i-1] + (L - (L-i))
        sequence.append(a)

print(sequence)



# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'


# You may wish to use further output for testing purposes while you develop your code

#[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

 # The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence