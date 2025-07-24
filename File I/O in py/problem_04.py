#a file conrains a word "donkey" multiple times , you need to write a program which replace this word with #### by updating the same file

with open("donkey.txt" , "r") as f:
    content =f.read()

contentupdate = content.replace("donkeyyy","####")

with open("donkey.txt" , "w") as f:
    f.write(contentupdate)