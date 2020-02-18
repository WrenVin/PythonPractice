
class Employee:

    #Use self for functions all the time
    def __init__(self, first, last, wage):#Constructor, initalizes values
        self.first = first
        self.last = last
        self.wage = wage
        self.email = first + '.' + last + '@gmail.com'
    
    def fullname(self): #This is a method
        return '{} {}'.format(self.first, self.last)
    
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

#Employee.fullname(emp_1) # similar to below, but passes instance through generic class, dont use
#print(emp_2.language, emp_2.first)
mgr = Manager('Sue', 'Smith', 90000, [dev_1])
