class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04 # class variable
    
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@snextech.com'
        
        Employee.num_of_emps += 1
        
    def fullName(self):
        return '{} {}'.format(self.fname, self.lname)
    
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Snex', 'Teddy', 50000)
emp_2 = Employee('Odhis', 'Lwande', 60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-5000'
emp_str_3 = 'Snex-Teddy-8000'

new_emp_1 = Employee.from_string(emp_str_2)

# print(emp_1.email)
print(new_emp_1.email)

import datetime
my_date = datetime.date(2023, 8, 11)

print(Employee.is_workday(my_date))


# print(emp_1.__dict__)
Employee.set_raise_amt(1.05)

print(emp_1.pay)
print(emp_2.raise_amount)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.num_of_emps)


# changing instance variable
# emp_2.lname = 'Ford'

# print(emp_2.fullName())

# Class variables are shared among all instances of the class, while instance variables are unique to each instance.
