
class Employee:
    #Use self for functions all the time
    def __init__(self, first, last, wage):#Constructor, initalizes values
        self.first = first
        self.last = last
        self.wage = wage
        self.email = first + '.' + last + '@gmail.com'
    
    def fullname(self): #This is a method
        return '{} {}'.format(self.first, self.last)
    

emp_1 = Employee('Vincent', 'Wren', '1000')
emp_2 = Employee('Carlos', 'Garica', '5000')#Each unique instance of class, dont pass self

Employee.fullname(emp_1) # similar to below, but passes instance through generic class, dont use
print(emp_2.fullname())

