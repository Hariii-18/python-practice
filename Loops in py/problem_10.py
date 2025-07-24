#write a program to print multiplication table of n in reverse order
n = int(input("enter a number: "))
for i in range (1,11):
    multiplication=(f"{n} X {11-i} = {n*(11-i)}")
    print(multiplication)









n=5
for i in range(10,0,-1):
    print(f"{n} X {i}= {n*i}")