#write a python function to print multiplication table of given number
def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
    
table(10)

