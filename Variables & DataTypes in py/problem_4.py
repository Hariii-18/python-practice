# use comparision operator to find out whether a given variable a is greater than b or not . take a= 34 and b=80
a = int(input("enter first number: "))
b = int(input("enter second number: "))
if (a>b):
    print(f"{a} is greater than {b}")
elif (a==b):
    print(f"{a} is equal to {b}")
else:
    print(f"{a} is less than{b}")