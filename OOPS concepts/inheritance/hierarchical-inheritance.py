class Parent:
    def parentmethod(self):
        print("this is a parent class")

class Child1(Parent):
    def method1(self):
        print("this is a child 1 class")

class Child2(Parent):
    def method2(self):
        print("this is a child 2 class")

# from child1 class we can retrive the data of parent class
child1 = Child1()
child1.method1()
child1.parentmethod()

# from th child2 class also we can retrive the data of parent class
child2 = Child2()
child2.method2()
child2.parentmethod()