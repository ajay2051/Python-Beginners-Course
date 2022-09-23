class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod
    def emp(cls,emp_str):
        first,last,pay = emp_str.split('_')
        return cls(first,last,pay)

emp_str_1 = 'John_Doe_5000'
new_emp =  Employee.emp(emp_str_1)
print(new_emp.first)


