class parent:
    def method1(self):
        print("this is a parent class")

class child(parent):
    def method2(self):
        print("this is a child class")

child = child()
child.method2()
child.method1()

parent = parent()
parent.method1()