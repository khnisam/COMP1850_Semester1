num1 = int(input("Enter number 1 "))
num2 = int(input("Enter number 2 "))

print("Please choose an arithmetic operation using the numbers relating to the operation.")
arithmeticOperation = int(input("1: + |2: - |3: * |4: /"))

if arithmeticOperation == 1:
    result = num1 + num2
    print(result)
elif arithmeticOperation == 2:
    result = num1 - num2
    print(result)
elif arithmeticOperation == 3:
    result = num1 * num2
    print(result)
elif arithmeticOperation == 4:
    result = num1 / num2
    print(result)
else:
    print("Invalid Choice")







