
class Employee:
    raise_amount = 1.04 #This class variable applies to all instances
     
    #Use self for functions all the time
    def __init__(self, first, last, wage):#Constructor, initalizes values
        self.first = first
        self.last = last
        self.wage = wage
        self.email = first + '.' + last + '@gmail.com'
    
    def fullname(self): #This is a method
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.wage = int(int(self.wage) * self.raise_amount)
        
    @classmethod # This declares this method as a class method
    def set_raise_amount(cls, amount): #cls is what class we are assigned too
        cls.raise_amount = amount
    

emp_2 = Employee('Carlos', 'Garica', 5000)#Each unique instance of class, dont pass self
emp_1 = Employee('Vincent', 'Wren', '1000')

emp_str_1 = 'John-Doe-70000'
first, last, pay = emp_str_1.split('-')
emp_3 = Employee(first, last, pay)
emp_3.apply_raise()
print(emp_3.wage)

