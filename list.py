one = ["jassi",98,85,99]
two = ["kartik",97,99,100]

def printInfo(pr):
    print("Name of student : ",pr[0])
    print("Marks in Physics : ",pr[1])
    print("Marks in Chemistry : ",pr[2])
    print("Marks in Maths : ",pr[3])

printInfo(one)
printInfo(two)

if "jassi" in one:
    print("Yes")
else:
    print("No")

marks = 0,1,2,3,4,5,6,7,8,9,10

print(marks)
print(marks[::2])



# list comprehention


lst = [i for i in range(11)]
print(lst)

lst = [i*i for i in range(11)]
print(lst)

lst = [i for i in range(11) if i%2==0]
print(lst)

l = [5,4,3,1,2,3,4]
print(l)

#add element at the end of the list
l.append(5)
print("List after adding element at last")
print(l)

#sort a list
l.sort()
print("List after sorting")
print(l)

#sort in reverse order
l.sort(reverse = True)
print("List after sorting in reverse order")
print(l)

#reversing of present list
l.reverse()
print(l)

#return index of element n
# l.index(n)

print(l.index(3))

#return how many times n is in a list
# l.count(n)

print(l.count(3))


#copy one list to another
m = [1,2,3,4,5]
n = m
n[0] = 100
print(m)

#changes in n would also take place in m because n have refrence of m

#to copy one list to another withought passing its refrence

m = [1,2,3,4,5]
n = m.copy()
n[0] = 100
print(m)

#to insert value at a perticular index of list
#l.insert(index, value)
m.insert(1, 200)
print(m)


#to extend first list using second list
#first_list.extend(second_list)
e = [100,200,300,400]
m.extend(e)
print(m)

#to create a third list by adding first and second list
f = m + e
print(f)