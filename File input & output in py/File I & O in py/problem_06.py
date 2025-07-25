# write a program to mine a log file and find out whether it contains 'python'
word="python"
with open("log.txt") as f:
    content = f.read()

if (word in content):
    print("YES Python is present in file")
else:
    print("NO the word python is not present in file")