class emp:
    def __init__(self, name):
        self.name = name 
    
    def __str__(self):
        return f"Name of emp: {self.name}"
    
class dancer:
    def __init__(self, dance_type):
        self.dance_type = dance_type

    def __str__(self):
        return f"Type of dance: {self.dance_type}"
    

class dancer_emp(emp, dancer):
    def __init__(self, name, dance_type):
        emp.__init__(self, name)
        dancer.__init__(self, dance_type)

    def __str__(self):
        return f"{super().__str__()}\n{super(emp, self).__str__()}"
    
o = dancer_emp("Harry", "Kathak")
print(o)
