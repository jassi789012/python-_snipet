tup = (1,)
print(tup)

#tuples are immutable

first = (1,2,3,4,5)

for i in first:
    print(i)

tup1 = (1,2,3,4,5)
tup2 = (6,7,8,9,0)

tup3 = tup1 + tup2
print(tup3)

#to find how many time an element is in a tuple
# tuple.count(element)

tup4 = (0,1,1,1,2,2,2,3,3)
print(tup4.count(1))

#to get the index of any element present in the tuple
# tuple.index(element)

print(tup4.index(1))

# to get index of element through slicing
# tuple.index(element, starting index, ending index +1)

print(tup4.index(1, 3, 9))


#to get length of tuple

print(len(tup4))

# to make changes in tuple convert it into list first

tup4 = list(tup4)
tup4[0] = 100
tup4 = tuple(tup4)
print(tup4) 