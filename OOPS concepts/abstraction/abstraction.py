'''-Hiding unnecessary information from the user is called abstraction
 -if a class contain one or more than one abstract method then the class is known as abstract class
 -if the method is declared without implementation it is called abstract method
 '''
from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

# Concrete Class 1
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Concrete Class 2
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Usage
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!