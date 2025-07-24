#check that a type cannot be changed in python
a = (33, 44.56, "hari")
#a[2] = 33.33
#tuples are immutable (cant change the data type)
a[2] == 33.33
print(a)

b=["hariii","prasad"]
# b.replace("prasad","bunnyyy") this , method is used in only strings 
# print(b.replace("prasad","bunnyyy")) #list cannot use .replace in python
b = [x.replace("hariii", "hari") for x in b]
print(b)