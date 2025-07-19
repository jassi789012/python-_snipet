class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name : {self.name}\nAge : {self.age}"

class Employee(Human):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def __str__(self):
        return f"{super().__str__()}\nSalary : {self.salary}"
    

class programmer(Employee):
    def __init__(self, name, age, salary, lan):
        super().__init__(name, age, salary)
        self.lan = lan 

    def __str__(self):
        return f"{super().__str__()}\nLanguage : {self.lan}"
    



o = programmer("jassi", 19, 1200000, "Python")
print(o)

