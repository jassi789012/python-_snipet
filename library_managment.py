class library:
    no_of_books = 0
    name = list()
    def __init__(self,name):
        self.name.append(name)
        library.no_of_books += 1
    def printInfo(self):
        print(f"Total Books : {self.no_of_books}")
        
        for i in range (self.no_of_books):
            print(f"{i+1} : {self.name[i]}")
        

lib1 = library("Ak dogra DSA")
lib1 = library("jassi coding classes")
lib1 = library("karan how to do nothing")

lib1.printInfo()
