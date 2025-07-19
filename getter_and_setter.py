class val:
    def __init__(self,value):
        self.value = value
    
    def show(self):
        print(f"Value is : {self.value}")


    # getter
        
    @property
    def ten_value(self):
        return 10* self.value
    

    # setter
    @ten_value.setter
    def ten_value(self, new_val):
        self.value = new_val/10






obj = val(10)
obj.show()
obj.ten_value = 67
print(obj.ten_value)
obj.show()

