class Parent:
    def method1(self):
        print("this is a main parent class")

class Child1(Parent):
    def method2(self):
        print("this is a child class derived from parent class")

class Child2(Child1,Parent):
    def method3(self):
        print("this calss can retrive the class child1 and parent class")

b = Child2()
b.method1()
b.method2()
b.method3()