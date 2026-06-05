class Employee: 
    def __init__(self, name, salary, password): 
        self.name = name 
        self.__salary = salary 
        self.__password = password 
        
    def employe_details(self): 
        print(f"Employee name is {self.name}") 
        print(f"Employee salary is {self.__salary}") 
        print(f"Employee password is {self.__password}") 

employee1 = Employee("Saksham", 50000, "123456") 
employee1.employe_details()
