#write a program to find whether the given number is prime or not
n = int(input("Enter a number: "))
for i in range(2, n):
        if n % i == 0:
            print("number is not prime")
            break
        else:
         print("number is prime")



# for i in range(1,50,2):     2 is step size   o/p:- 1,4,7








#write a program to find wether a number is prime or not 
n=7
for i in range(1,n):
    if(i%2==0):
        print("prime number")
    else:
        print("not a prime")