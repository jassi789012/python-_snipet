class emp:
    company_name = "Apple"

    def __init__(self, name):
        self.name = name
    
    def show(self):
        print(f"The name of emp is {self.name} and name of company is {self.company_name}")
    
    @classmethod
    def changeCompanyName(cls, new_name):
        cls.company_name = new_name


class employe:
    def __init__(self, name, salary):
        self.name  = name
        self.salary = salary

    def show(self):
        print(f"{self.name} gets {self.salary}")

    @classmethod
    def fromstri(cls, stri):
        return cls(stri.split("-")[0],stri.split("-")[1])    


emp1 = emp("jassi")
emp1.show()
emp1.changeCompanyName("Tesla")
emp1.show()

print(f"{emp.company_name}")

employe1 = employe("jassi",50000)
employe1.show()

stri = "harry-12000"

# before using classmethod
# employe2 = employe(stri.split("-")[0],stri.split("-")[1])

employe2 = employe.fromstri(stri)
employe2.show()

