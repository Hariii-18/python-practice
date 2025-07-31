# already created a method in superclass then implementing same method in subclass . if it overrides superclass method then it is called method overriding
class parent:
    def method1(self):
        print("this is a parent method")

class child(parent):
    def method1(self):
        print("this is a child method")

a = child()
a.method1()  #child class method is over riding the parent class method
