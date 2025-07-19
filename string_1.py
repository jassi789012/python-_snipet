names = "jassi sigh"
print("length of string ",len(names))
print(names[0:5])
print(names[:5])
print(names[:])

#print(names[-3:-1])  and  print(names[len(names)-3:len(names)-1])  both are same


#strings are immutable

a = "!!!! Jassi !!!!"
print(a)
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Jassi","jaswinder"))
print(a.split(" "))

head = 'my name is jaswinder singh'
print(head.capitalize())
print(head.center(50))
print(a.count("!"))
print(a.endswith("!"))
print(a.endswith("!",2,4))
#find return -1 if string is not found
print(head.find("is"))
#index return error if string is not found
print(head.index("is"))
#return false if string contains only (a-z,A-Z,0-9)
print(head.isalnum())
print(head.islower())
print(head.isprintable())
print(head.isspace())
print(head.istitle())
print(head.startswith("my"))
print(head.swapcase())
print(head.title())