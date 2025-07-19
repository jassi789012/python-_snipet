str = [1,2,3,4,5,6,7,8,9]

for i in range(0,3):
    str.remove(str[0])


for i in range(0,3):
    str.remove(str[-1])

print(str)
print(len(str))