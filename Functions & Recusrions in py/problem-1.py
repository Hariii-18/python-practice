# write a program using functions to find greatest of three numbers
def greatest():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    if (a>b and a>c):
        print(a, "is the greatest number")
    elif (b>a and b>c):
        print(b, "is the greatest number")
    elif(c>a and c>b):
        print(c,"is the greatest number")
greatest()





def least_value():
    a=int(input("enter first number: "))
    b=int(input("enter first number: "))
    c=int(input("enter first number: "))
    if(a<b and a<c):
        print(f"{a} is the least number")
    elif(b<c and b<a):
        print(f"{b} is the least number")
    elif(c<b and c<a):
        print(f"{c} is the least number")
least_value()












