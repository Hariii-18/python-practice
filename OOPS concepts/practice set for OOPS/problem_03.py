'''create a class employee and add salary and increment properties to it
 write a method salaryafterincrement method with a @propert decorator with a setter which changes the value of increment based on the salary '''
class Employee:
    def salary(self , salary , increment):
        self.salary = salary
        self.increment = increment
        print(f"your current salary is: {self.salary}")
         
