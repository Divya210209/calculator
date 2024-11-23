import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def sq(a,b):
    return a**b
operations_dict={
    "+" :add,
    "-" :sub,
    "*" :mul,
    "/" :div,
    "^" :sq
}
def calculator():
    number1=float(input("Enter first number: "))
    for symbol in operations_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        op_symbol=input("pick an operation: ")
        number2=float(input("Enter second number: "))
        cal_fn=operations_dict[op_symbol]
        output=cal_fn(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")

        should_con=input(f"enter 'y' to continue calculation with {output} or 'n' to exit").lower()
        if should_con=='y':
            number1=output
        elif should_con=='n':
            continue_flag=False
            os.system('cls')
            calculator()
        else:
            continue_flag=False
            print("Bye")

calculator()

