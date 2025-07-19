class parent_class:
    def parent_method(self):
        print("This is parent method")

class child_class(parent_class):

    def parent_method(self):
        print("called from child class obj ")

        #super keyword is used to call parent class methods 

        super().parent_method()


    def child_method(self):
        print("This is child method")


obj_parent = parent_class()
obj_parent.parent_method()
obj_child = child_class()
obj_child.child_method()
obj_child.parent_method()


class emp:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def show(self):
        print(f"{self.id} id emp name is {self.name}")


class programmer(emp):
    def __init__(self, name, id, lan):

        # super is also used to call parent class constructor

        super().__init__(name, id)
        self.lan = lan

    def show(self):
        print(f"{self.id} id programmer name is {self.name} and have speciality in {self.lan} language")



jassi = emp("jassi",140)
jassi.show()
harry = programmer("harry", 420, "python")
harry.show()

