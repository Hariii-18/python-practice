#write a program to calculate the factorial of a given number using for loop
# 5! = 5 X 4 X 3 X 2 X 1
n= int(input("Enter a number: "))
product = 1
for i in range (1 , n+1):
    product = product * i 
    print(product)
# Factorial using while loop
i = n
factorial = 1
while i > 1:
    factorial *= i
    i -= 1
print(f"The factorial of {n} using while loop is: {factorial}")
