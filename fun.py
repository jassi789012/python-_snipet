def table(n):
    for i in range(1,11):
        print(n," X ",i," = ",n*i)


def gmean(a, b):
    print((a*b)/(a+b))

def chek(a, b):
    if(a>b):
        print("a is greater")
    elif(a<b):
        print("b is greater")
    else:
        print("both are equal")

def emp():
    pass

n = int(input("Enter any number: "))
table(n)

a = int(input("Enter a for gmean: "))
b = int(input("Enter b for gmean: "))
gmean(a, b)

a = int(input("Enter a to chek: "))
b = int(input("Enter b to chek: "))
chek(a, b)