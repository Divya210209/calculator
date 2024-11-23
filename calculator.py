num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
operation=input("Choose the operation(+,-,*,/,^):")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
elif operation == '^':
    result = num1 ** num2
else:
    print("Invalid Input")
print(f"The result is {result}")