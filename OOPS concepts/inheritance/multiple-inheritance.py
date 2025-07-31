class Father:
    def method1(self):
        print("this is a parent 1 class")

class Mother:
    def method2(self):
        print("this is a parent 2 class")

class son(Father , Mother):
    def method3(self):
        print("this is a child class")

A = son()
A.method3()
A.method2()
A.method1()