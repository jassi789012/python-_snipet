class Maths:
    def __init__(self, num):
        self.num = num
    
    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a+b
    
n = Maths(4)
print(n.num)
n.addtonum(6)
print(n.num)


print(n.add(3, 10))
     #  ^
     #  |
 # Both are same 
     #  |
     #  v
print(Maths.add(3, 10))