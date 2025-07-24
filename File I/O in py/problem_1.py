#write a program to read the text from the given file 'poems.txt' and find out whether it contains the word 'twinkel'
f = open("poem.txt")
content = f.read()
if ("twinkel" in content):
    print("the word twinkel present in file")
else:
    print("the word twinkel is not present in the file")

f.close()






f = open("fun.txtt")
content = f.read()
if ("Hariii" in content):
    print("the word hariii is present in file")
else:
    print("the word hariii is not present in file")
f.close()