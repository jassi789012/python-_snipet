class emp:

    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary




# use of dir

x = list()
print(dir(x))
print(x.__add__)



# use of __dict__

p = emp("jassi", 1200)
print(p.__dict__)


# use of help

print(help(emp))