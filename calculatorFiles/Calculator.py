num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Choise an operation")
print("1 = sum ")
print("2 = subtraction ")
print("3 = division ")
print("4 = multiplication ")

operation = int((input("Enter the operation: ")))

if operation == 1:
    sum = int(num1 + num2)
    print("The result is:", sum)

if operation == 2:
    sub = int(num1 - num2)
    print("The result is:", sub)

if operation == 3:
    div = int(num1 / num2)
    print("The result is:", div)

if operation == 4:
    mult = int(num1 * num2)
    print("The result is:", mult)

