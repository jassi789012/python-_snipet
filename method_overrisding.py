class rec:
    def __init__(self ,x ,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class c(rec):
    def __init__(self, r):
        self.r = r
        super().__init__(r, r)

    def area(self):
        return 3.14 * super().area()
    

rectange = rec(4, 5)
print(rectange.area())

circle = c(5)
print(circle.area())

