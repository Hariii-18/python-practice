'''write a program to find out whether a student has passed or failed if it requires a total of 40% and atleat 33% in each subject to pass. 
assume 3 subjects and take marks as a =n input from the user'''
m1=int(input("Enter marks of subject 1: "))
m2=int(input("Enter marks of subject 2: "))
m3=int(input("Enter marks of subject 3: "))

percentage = (100*(m1+m2+m3)/300)
if(percentage>=40 and m1>33 and m2>33 and m3>33):
    print("you are passed ",percentage)
else:
    print("you failed ",percentage)    


''' total_marks = subject1 + subject2 + subject3
max_total = 300  # Assuming each subject is out of 100
percentage = (total_marks / max_total) * 100
 '''