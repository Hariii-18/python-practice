# write a program to rename a file to "renamed_by_python.txt"
with open("old_file.txt") as f:
    content = f.read()

with open("renamed_by_python" , "w") as f:
    f.write(content)

import shutil
print(dir(shutil))