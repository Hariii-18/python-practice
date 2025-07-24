# write a program to find the greatest of four numbers entered by user
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))
d = int(input("Enter your fourth number: "))

if (a>b and a>c and a>d ):
    print(f"{a} is the greatest number")
elif(b>a and b>c and b>d):
    print(f"{b} is the greatest number")
elif(c>a and c>b and c>d):
    print(f"{c} is the greatest number")
else:
    print(f"{d} is the greatest number")    