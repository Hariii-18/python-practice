# write a program to find out whether a file is identical & mathches the content of another file
with open("file.txt") as f:
    file1 = f.read()

with open("file2.txt") as f:
    file2 = f.read()

if (file1==file2):
    print("Yes , these files are identical and matches")
else:
    (print("No , these files are not identical and not matches"))