# create a class with a class attribute a ; create an object from it and set 'a' directly using object.a=o.Does this change the class attribute?
class one:
    a = 4
o = one()
print(o.a) #prints the class attribute because instance attribute is not present
o.a = 0 # instance attribute is set
print(o.a) #prints the instance attribute because instance attribute is present
print(one.a) #prints the class attribute
