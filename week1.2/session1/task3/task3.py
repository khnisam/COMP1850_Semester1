# Week 1.2, Session 1: Task 3

fruit = ("apple", "banana", "cherry")
print(fruit)

# Find and display position of "banana"

position = fruit.index("banana")
print(fruit[position])
print(f"Position: {position}")

# Display how many times "cherry" occurs

counter = fruit.count("cherry")
print(f"Cherry appears: {counter} times.")

# Display how many times "strawberry" occurs

counter = fruit.count("strawberry")
print(f"Strawberry appears: {counter} times.")

# Unpack tuple into variables

(first, second, third) = fruit
print(first)
print(second)
print(third)
