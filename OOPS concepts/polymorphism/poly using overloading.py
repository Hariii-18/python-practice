# if the class contians more than one method has same name & 
# the method contains different datatypes of parameters or different no of parameters or both is called method overloading
from multipledispatch import dispatch

class A:
    @dispatch (int,int)
    def add(self,a,b):
        print(a+b)
    
    @dispatch (int,int,int)
    def add(self,a,b,c):
        print(a+b+c)

    @dispatch (str , str)
    def add(self,a,b):
        print(a+b)
    
obj = A()
obj.add(1,2)
obj.add(5,6,4)
obj.add("hari","parsad")