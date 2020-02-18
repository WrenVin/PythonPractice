
class Employee:
<<<<<<< HEAD

=======
    raise_amount = 1.04 #This class variable applies to all instances
     
>>>>>>> master
    #Use self for functions all the time
    def __init__(self, first, last, wage):#Constructor, initalizes values
        self.first = first
        self.last = last
        self.wage = wage
        self.email = first + '.' + last + '@gmail.com'
    
    def fullname(self): #This is a method
        return '{} {}'.format(self.first, self.last)
    
<<<<<<< HEAD
class Developer(Employee): #inherits everything from Emplyoee
    def __init__(self, first, last, wage, language):
        super().__init__(first, last, wage)# This calls and runs the parent init method
        self.language = language
        
class Manager(Employee): #inherits everything from Emplyoee
    def __init__(self, first, last, wage, employees=None):
        super().__init__(first, last, wage)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def add_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())

emp_1 = Employee('Vincent', 'Wren', '1000')
emp_2 = Developer('Carlos', 'Garica', 5000, 'Python')#Each unique instance of class, dont pass self
=======
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
>>>>>>> master

#Employee.fullname(emp_1) # similar to below, but passes instance through generic class, dont use
#print(emp_2.language, emp_2.first)
mgr = Manager('Sue', 'Smith', 90000, [dev_1])
