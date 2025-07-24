#repeat program 4 for a list of such words to be censored
words = ["b***", "d*", "f**", "s*", "c**"]
try:
    with open("prblm.txt", "r") as infile:
        content = infile.read()
except FileNotFoundError:
    print("File Not Found")
    content = ""

newcontent = content
for word in words:
    newcontent = newcontent.replace(word, "*" * len(word))

with open("prblm.txt", "w") as outfile:
    outfile.write(newcontent)
