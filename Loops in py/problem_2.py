#write a program to greet all the persons names stored in a list 'l' ans which starts with S
# l = ["Hari" , "Sohan" , "Sachin","Rahul"]

l = ["Hari" , "Sohan" , "Sachin","Rahul"]
for name in l:
    if(name.startswith("S")):
        print("good morning",name)
    else:
        print(name)




# print 1 yo 50 using while loop
'''
i=50
while(i>0):
    print(i)
    i-=1

j=1
while(j<51):
    print(j)
    j+=1      '''

l=["hari","suvvi","saroja","hariii"]
for i in l:
    if(i.startswith("s")):
        print("congratulatioins, ",i)
    else:
        print(i)