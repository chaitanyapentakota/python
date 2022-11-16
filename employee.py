class Employee:
   
    def __init__(self,first_arg,second_arg,third_arg,fourth_arg):
        self.first_name = first_arg
        self.last_name = second_arg
        self.phone_number = third_arg
        self.email = fourth_arg

    def details(self):
        print("employee details are:",self.first_name,self.last_name,self.phone_number,self.email)
    

chaitanya = Employee('chaitanya','pentakota',9963640627,'chaitupentakota@gmail.com')
chaitanya.details()