class grandparent:
    def method1(self):
        print("this is a grand parent class")

class parent1:
    def method2(self):
        print("this is a parent 1 class")

class parent2:
    def method3(self):
        print("this is a parent 2 class")

class child(grandparent,parent1,parent2):
    def method4(self):
        print("this is a child class")
    
child = child() #from child class we are getting the data of all the classes
child.method4()
child.method3()
child.method2()
child.method1()