colors = ["red:" ,"green" ,"white" ,"black"]

for color in colors:
    print(color)

    for i in color:
        print(i)


for k in range(5):
    print(k+1)

for k in range(1,5):
    print(k)

# for k in range(1,20001):
#     print(k)

for k in range(0,11,2):
    print(k)


for i in range(0,5):
    for j in range(0,5):
        print("*",end = " ")
    print(" ")


i = 0 
while(i<5):
    print(i)
    i = i + 1

i = 5
while(i>0):
    print(i)
    i = i - 1
else:
    print("Now the condition is false")


for i in range(13):
    print("5 X ",i,"=",5*i)
    if(i==10):
        break

for i in range(11):
    if(i%2 != 0):
        continue
    print(i,end=" ")

# if loop is breaked else would not be executed

for i in range(4):
    print(i)
    if i == 2:
        break
else:
    print("Loop is completed")



# use of enumerate in for loop

marks = [23, 56, 78, 45]

for index,mark in enumerate(marks):
    print(index,mark)
    if(index == 2):
        print("Weldone jassi")

