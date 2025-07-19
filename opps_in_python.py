class person:
    name = str()
    occupation = str()
    networth = int()

    def info(self):
        print(f"{self.name} is {self.occupation} with networth : {self.networth}")


a = person()
a.name = "Jassi"
a.occupation = "Software Developer"
a.networth = 10000
b = person()
b.name = "Karan"
b.occupation = "Software Developer"
b.networth = 12000

a.info()
b.info()


# constructors

class emp:
    def __init__(self, n, o):
        self.name = n
        self.occ = o
    
    def info(self):
        print(f"{self.name} is {self.occ}")
    

emp1 = emp("kartik", "Army officer")
emp2 = emp("kamal", "Solder")

emp1.info()
emp2.info()
