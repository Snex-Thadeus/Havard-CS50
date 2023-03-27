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
        
        
class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang 
        
class Manager(Employee):
    
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
            
    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullName())
        
        
        
dev_1 = Developer('Snex', 'Teddy', 50000, 'Python')
dev_2 = Developer('Odhis', 'Lwande', 60000, 'Javascript')

mngr_1 = Manager('Odhis', 'Teddy', 9000, [dev_1])

print(isinstance(mngr_1, Developer))

print(issubclass(Developer, Employee))

print(mngr_1.email)

mngr_1.add_emp(dev_2)
mngr_1.remove_emp(dev_1)

mngr_1.print_emps()

print(dev_1.email)
print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)