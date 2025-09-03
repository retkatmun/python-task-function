class Employee:
    pass
emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = "corey"
emp_1.last = "schafer"
emp_1.email = "corey.schafer@company.com"
emp_1.pay = 50000

emp_2.first = "john"
emp_2.last = "scholar"
emp_2.email = "scholar.john@company.com"
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)
