class Employee:

    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    @property    
    def email(self):
        return '{}.{}@email.com'.format(self.fname, self.lname)
        
    @property   
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
        
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    
emp_1 = Employee('Snex', 'Teddy')

emp_1.fullname = 'Corey Schafer'

print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

