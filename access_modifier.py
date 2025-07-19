class emp:
    def __init__(self):
        self.name = "jassi"
        self.__name2 = "jass"

emp1 = emp()

print(emp1.name)

# protected variables can not be accesed through direct method

# print(emp1.__name2)

# indirect meythod
# name mangling

print(emp1._emp__name2)