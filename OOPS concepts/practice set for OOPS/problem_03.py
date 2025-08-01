'''create a class employee and add salary and increment properties to it
 write a method salaryafterincrement method with a @propert decorator with a setter which changes the value of increment based on the salary '''
class Employee:
    salary = 20000
    increment = 20
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100

e = Employee()
e.salaryAfterIncrement = 20
print(e.increment)