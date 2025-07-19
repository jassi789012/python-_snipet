def apply(fn, val):
    return 6 + fn(val)


double = lambda x: x*2
square = lambda x: x*x
cube = lambda x: x*x*x

avg = lambda a, b, c: (a + b + c)/3

print(double(3))
print(square(3))
print(cube(3))
print(avg(3, 5, 10))

print(apply(cube, 2))

#       ^
#       |
# Both are same
#       |
#       v

print(apply(lambda x: x*x*x, 2))