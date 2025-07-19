class emp:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for ch in self.name:
            i = i + 1
        
        return i
    
    def __str__(self):
        return (f"The name of emploee is {self.name}")
    
    def __repr__(self):
        return (f"Emploee : ('{self.name}')")
        
    
emp1 = emp("jassi")
print(len(emp1))

# this is possible due to __str__fun
print(emp1)

print(str(emp1))
print(repr(emp1))


