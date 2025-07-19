def average(*number):
    sum = 0
    for i in number:
        sum = sum + i
    return sum/len(number)

c = average(1,2,3,4,5,6,7,8,9,10)

print(c)