"""
1. Classes and instances
    tip_1
2. instance vars vs. class vars
    tip_2
    tip_3
3.instance vs class vs static methods
    tip_4
    tip_5
    tip_6
4. subclasses
    tip_7
    tip_8
    tip_9
"""


import datetime


class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1 # check tip_3

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # self.raise_amount is different from Employee.raise_amount (check tip_2)
    
    @classmethod
    def set_raise_amt(cls, amount): # cannot use class keyword, so I use cls
        cls.raise_amount = amount

    # Alternative constructor / __init__ (starts from_*)
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # Is a normal function which does not depend on self or cls but has
    # logical connection with cls
    @staticmethod
    def is_workday(day):
        # 0: Monday, 1: Tuesday, ..
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # or: Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay) # or: Employee.__init__(self, first, last, pay)
        if employees == None:
            self.employees = []
        else:
            prog_lang


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# tip_1 (Classes and instances)
print('tip_1: ', emp_1.fullname())
print('tip_1: ', Employee.fullname(emp_1))

# tip_2 (instance vars vs. class vars)
emp_2.raise_amount = 1.06
Employee.raise_amount = 1.08
print('tip_2: ', Employee.raise_amount)
print('tip_2: ', emp_1.raise_amount)
print('tip_2: ', emp_2.raise_amount)
"""
Q: whz emp_2 does not change?
A: if you print(emp_2.__dict__) right after you create the object, the
raise_amount is not included, that means takes the value from class Employee
and not from instance (self). When you assign 'emp_2.raise_amount = 1.06'
and print(emp_2.__dict__) raise_amount is included
"""

# tip_3 (instance vars vs. class vars)
print('tip_3: ', Employee.num_of_emps)

# tips_4 (instance vs class vs static methods)
# classmethod
Employee.set_raise_amt(3)
print('tip_4: ', Employee.raise_amount)
print('tip_4: ', emp_1.raise_amount)
print('tip_4: ', emp_2.raise_amount)

# tip_5 (instance vs class vs static methods)
# Alternative constructor
emp_3 = Employee.from_string('John-Doe-70000')

# tip_6 (instance vs class vs static methods)
# staticmethod
print('tip_6: ', Employee.is_workday(datetime.date(2020, 7, 11)))

# tip_7 (subclasses)
print('tip_7: ', help(Developer))

# tip_8 (subclasses)
# change raise_amt does not affect Employee's parent var
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_1 = Developer('Test', 'User', 60000, 'Java')
print('tip_8: ', dev_1.pay)
dev_1.apply_raise()
print('tip_8: ', dev_1.pay)
print('tip_8: ', emp_1.pay)

# tip_9 (subclasses)
# change raise_amt does not affect Employee's parent var
print('tip_9: ', dev_1.prog_lang)

