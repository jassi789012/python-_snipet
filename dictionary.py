# dictionary is a ordered data type

#syntax

# dic = {
    # "key" : "Value"
# }

dic = {
    1 : "jassi",
    2 : "karan",
    3 : "kartik",
    4 : "kamal"
}

print(dic[1])

# print(dic[1]) and print(dic.get(1))
# both are same but first one would through an error if element is not available but get fun will return none

print(dic.get((5)))

# to get all keys present in dic

print(dic.keys())

#to get all values pressent in dic

print(dic.values())


# to interate all keys present in dic

for key in dic.keys():
    print(key)


# to iterate all values present in dic

for val in dic.values():
    print(val)


# to print both keys and values

print(dic.items())

# to iterate both keys and values

for key,val in dic.items():
    print(key," : ",val)


#to add or update new value in a dictionary

s1 = { 1 : 99 , 2 : 77 , 3 : 88}
s2 = { 4 :89 , 5 : 88}
print(s1)
print(s2)
s1.update(s2)
print(s1)

# to clear dictionary
# s1.clear()
# print(s1)


# pop is used to remove key value pair

s1.pop(1)
print(s1)

# popitem remove last key value pair

s1.popitem()
print(s1)

# del keyword is used to del a dictionary

# del s1

# del through key value

del s1[3]
print(s1)