''' Write a python program using funtion to convert celsius to fahreneit
 formula for the above problem 
C->F , C/5 = (f-32)/9 
C->F , C = 5*(f-32)/9 
F->C , F=(c*9/5)+32'''
#F-->C
def celsius_to_fahreneit():
    fahreneit = (celsius * 9/5)+32
    return fahreneit
celsius = float(input("Enter temperature in Celsius: "))
fahreneit=celsius_to_fahreneit()
print(f"{celsius}°C is equal to {fahreneit}°F")




