l = [1,2,3,4,5]

# cube = lambda x: x*x*x

# newl = []
# for list in l:
#     newl.append(cube(l))

#       ^
#       |
# Both are same
#       |
#       v

newl = list(map(lambda x: x*x*x, l))



print(newl)


# filter is used to filter the objects

def filter_fun(x):
    return x>2

newnewl = list(filter(filter_fun, l))

print(newnewl)

from functools import reduce

# calculate the sum of numbers using reducing function

newlist2 = reduce(lambda x, y: x + y, l)
print(newlist2)