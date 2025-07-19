def factorial(n):
    '''takes an integer value and return its factorial through recursion'''
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)


fac = factorial(int(input("Enter any number : ")))
print(fac)
print(factorial.__doc__)