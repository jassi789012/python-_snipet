a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
op = input("Enter operation you want to do on given numbers from(+,-,*,/)")

match op:
    case '+':
        print("Sum of given two numbers:",a+b)
    case '-':
        print("Subtraction of given two numbers:",a-b)
    case '*':
        print("Multiplication of given two numbers:",a*b)
    case '/':
        print("Dividation of given two numbers:",a/b)
    case _:
        print("Invalid Input..")
