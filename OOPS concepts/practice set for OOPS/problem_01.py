# create a class(2-D vector) and use it to create another class representing a 3-D vector
class twoD_vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"the 2D vector is {self.i}i + {self.j}j")

class threeD_vector(twoD_vector):
    def __init__(self, i, j ,k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"the 3D vector is {self.i}i + {self.j}j + {self.k}k")
                                                                        
obj1 = threeD_vector(2 , 3 , 8)
obj1.show()
obj2 = twoD_vector(3 , 9)
obj1.show() 