''' 
2. Protected access specifier
-if data is declare in protected acess specifier it can access only that class & derived class
-put _(single underscore) before data & method to declare as protected
'''
class parent:
    _protectedData = 25
    def method1(self):
        print(self._protectedData)

class child(parent):
    def method2(self):
        print(self._protectedData)

a = child()
a.method1()
a.method2()
b=parent()
b.method1()
b.method2() #shows error for this line cause we cant access the method2 from parent class