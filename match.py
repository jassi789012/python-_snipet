a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
m = input("Choose operation to be done on given a and b from (+, -, *, /): ")

match m:
    case '+':
        print("a + b : ", a + b)
    case '-':
        print("a - b : ", a - b)
    case '*':
        print("a * b : ", a * b)
    case '/':
        if b != 0:
            print("a / b : ", a / b)
        else:
            print("Cannot divide by zero.")
    case _:
        print("Wrong input")
