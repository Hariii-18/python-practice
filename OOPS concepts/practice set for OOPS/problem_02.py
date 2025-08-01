# create a class Pets from a class Animals and further create a class Dog from Pets . add a method bark to class Dog
class Animals:
    def __init__(self):
        pass
class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod #if we use static method no need to declare the (self)
    def bark():
        print("boww boww")
a = Dog()
a.bark()    