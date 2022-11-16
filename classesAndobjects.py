class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idnumber)
    def display(self):
        print(self.name)
        print(self.idnumber)
        print(self.salary)
        print(self.post)
a = Employee('Rahul', 886012, 200000, "Intern")
a.display()