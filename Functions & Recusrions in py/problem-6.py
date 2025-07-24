#write a python function which converts inches to cms
def inches_to_cms(inches):
    return inches * 2.54
n=int(input("Enter the value of inches: "))
print(f"the corresponding value in cms is: {inches_to_cms(n)} ")

