#what will be the length of the follwing set S:
""""
s = set()
s.add(20)
s.add(20.0)
s.add('20')
"""
s = set()
s.add(20) #20 = 20.0
s.add(20.55) #if 20.0 = 20.5(any other value)
s.add('20')
print("the length of the set is: ",len(s)) #len = 3
print(s)
print(type(s))