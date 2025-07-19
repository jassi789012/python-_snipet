# DocString should be defined before the function body
# Changes in DocString can change the output of programe

def square(n):
    '''Takes a number n and return its square'''
    print(f"square of {n} : {n**2}")

square(5)
print(square.__doc__)
