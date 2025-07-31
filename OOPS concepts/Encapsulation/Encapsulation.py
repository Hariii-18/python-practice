# combination of abstraction and datahiding is encapsulation
#there are theree types of acceess specifiers in encapsulation
#to avoid collisons we use public, private , protected in python
''' 1.Public access specifier
any where in class we can use when we declare in public access specifier
we can access from subclass , by subclass object'''

class parent:
    PublicData = 25
    def method1(self):
        print(self.PublicData)

class child(parent):
    def method2(self):
        print(self.PublicData)

a = child()
a.method1()
a.method2()
