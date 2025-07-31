# normal method in abstract class is concrete method

from abc import ABC, abstractmethod
class one(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("this is concrete method")
    @abstractmethod
    def method3(self):
        pass

class two(one):
    def method1(self):
        print("method 1 is implemented in sub class")
    def method3(self):
        print("method 3 is implemented in sub class")
    
a = two()
a.method1()
a.method2()
a.method3()