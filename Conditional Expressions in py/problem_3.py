'''a spam comment is defined as a text containing following keywords:
"make a lot of money" , "buy now" , "subscribe this" , "click this" .
write a program to detect these spams.
  '''

word1 = "make a lot of money "
word2 = "buy now" 
word3 = "subscribe this"
word4 = "click this"

comment = input("enter your comment: ")
if ((word1 in comment) or (word2 in comment) or (word3 in comment) or (word4 in comment) ):
    print("This comment is SPAM...")
else:
    print("this comment is NOT SPAM...")




'''
comment1 = input("comment here: ")
w="click this"
w1="make lot of money"
w2="buy now"
w3="subscribe this"
if(w in comment1 or w1 in comment1 or w2 in comment1 or w3 in comment1):
    print("this COMMENT is a SPAM...!!!!")
else:
    print("This COMMENT is NOT A SPAM..")

'''








