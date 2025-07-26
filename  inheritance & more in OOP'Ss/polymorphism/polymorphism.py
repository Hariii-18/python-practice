# if a function handles more than one datatype & different parameter size then it is a polymorphism
class A:
    def fun(self):
        print("This is class A")

class B:
    def fun(self):
        print("This is class B")

class C:
    def fun(self):
        print("This is class C")

def poly(obj):
    obj.fun()

obj1 = A()
obj2 = B()
obj3 = C()

poly(obj1)
poly(obj2)
poly(obj3)