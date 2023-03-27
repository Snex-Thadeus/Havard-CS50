class Employee:

    raise_amount = 1.04 # class variable
    
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@snextech.com'
        
        
    def fullName(self):
        return '{} {}'.format(self.fname, self.lname)
    
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
        
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.fname, self.lname, self.pay)
    
    
    def __str__(self):
        return '{} - {}'. format(self.fullName(), self.email)
    
    
    def __add__(self, other):
        return self.pay + other.pay
    
    
    def __len__(self):
        return len(self.fullName())
        
        
emp_1 = Employee('Snex', 'Teddy', 50000)
emp_2 = Employee('Odhis', 'Lwande', 60000)

print(emp_1 + emp_2)

print(len(emp_1))

print(repr(emp_1))
print(str(emp_1))

