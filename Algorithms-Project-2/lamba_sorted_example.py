class Employee:
    
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
        
    def __repr__(self):
        return self.__str__()
        
    def __str__(self):
        return "{0}: ${1}: {2}".format(self.name, self.salary, self.age)
        
e1 = Employee("Shehryar", 45000, 26)
e2 = Employee("Ali", 40000, 24)
e3 = Employee("Haris", 42000, 27)

emp_list = [e1, e2, e3]
print(emp_list)

print(sorted(emp_list, key=lambda x:x.name))