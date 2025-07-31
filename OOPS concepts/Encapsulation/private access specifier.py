'''
we can access data ifrom any derived class in private access specifier
put double __ underscore before the data/ method to declare as a private
'''

class parent:
    __privateData = 25
    def method1(self):
        print(self.__privateData)

class child(parent):
    def method2(self):
        print(self.__privateData)

a = child()
a.method1()
# a.method2()  throughs error , can retrive data if it is declared as private
# but we can access data by providing a method for sud class
class Parent:
    __privateData = 25

    def method1(self):
        print(self.__privateData)

    # Provide a method for subclasses (or anyone) to access it
    def get_private_data(self):
        return self.__privateData

class Child(Parent):
    def method2(self):
        # Access through the parent's public method
        print(self.get_private_data())

a = Child()
a.method1() # Output: 25
a.method2() # Output: 25

