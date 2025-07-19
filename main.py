import pandas
import hashlib
# print 
print("hi\nhow are you")


print("hello",5,6,7,sep="-",)


a = 10
print(a)

b = "jassi!!"
print(b)

print("type of a",type(a))
print("type of b",type(b))


st = '''hello
my name is jassi
age = 19
'''


print(st)
print(st[0],st[1],st[2])


for character in st:
    print(character)
    print(st[0:10])


print(b.upper())
print(b.lower())

print(b.rstrip("!"))
print(b.replace("jassi","parveen"))
print(st.split(" "))
print(b.capitalize())
