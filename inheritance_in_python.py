class Emp:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def printInfo(self):
        print(f"name of employe {self.id} : {self.name}")


class programmer(Emp):
    def show(self):
        print("This is inherited class")


e1 = Emp("jassi",409)
e1.printInfo()
e2 = programmer("Harry", 410)
e2.printInfo()
e2.show()
