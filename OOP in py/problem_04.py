# add a static method in problem 2 , to greet the user with hello
class calculator:
    def __init__(self,n):
        self.n = n 
    def square(self):
        print(f"the square is {self.n*self.n}")
    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"the square root is {self.n**1/2}")
    @staticmethod # we add staticmethod cause , no need to add self 
    def greet():
        print("good morning..!")

a = calculator(2)
a.greet()
a.square()
a.cube()
a.squareroot()