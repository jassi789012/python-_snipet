x = 10

def my_fun():
    global x 
    x = 4

print(x)
my_fun()
print(x)
