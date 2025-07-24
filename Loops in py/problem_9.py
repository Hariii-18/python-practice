'''write a program to print the following pattern
***
* *
*** for n = 3'''
n = int(input("enter a number: "))
for i in range (1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*" , end="")
        print(" "*(n-2),end="")
        print("*" , end="")
    print("  ")


n=int(input("enter digit : "))    
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n , end="")
    else:
        print("*" , end="")
        print(" "*(n-2) , end="")
        print("*" , end="")
    print("  ")