# create a class "Programmer" for storing the information of few programmers working at microsoft
class Programmer:
    company="Microsoft"
    def __init__(self , name,salary,pin):
        self.name=name
        self.salary = salary
        self.pin = pin
p = Programmer("hari",50000,500100)
print(p.name,p.salary,p.pin,p.company)
q = Programmer("prasad",70000,500100)
print(q.name,q.salary,q.pin,q.company)