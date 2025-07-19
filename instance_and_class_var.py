class emp:
    no_of_emp = 0
    company_name = "Apple"

    def __init__(self, name):
        self.name = name
        emp.no_of_emp += 1
    
    def disp(self):
        print(f"{self.no_of_emp}. {self.name} in {self.company_name}")
    
emp1 = emp("Harry")
emp1.company_name = "Apple india"
emp.disp(emp1)

emp2 = emp("jassi")
emp2.company_name = "Apple US"
emp.disp(emp2)

emp3 = emp("kartik")
emp3.company_name = "Apple Pakistan"
emp.disp(emp3)

print(f"Total no of emp in company : {emp.no_of_emp}")
