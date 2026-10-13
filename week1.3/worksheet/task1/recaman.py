# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input

i = 1
sequence = [0]
for i in range(L):
    trial = sequence[i] - i+1
    if trial > 0:
        a = sequence[i] - i+1
        sequence.append(a)
    elif trial < 0:
        a = sequence[i] + i+1
        sequence.append(a)


print(sequence)



# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'


# You may wish to use further output for testing purposes while you develop your code

#[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence