# Write to file
with open("greetings.txt", "a+") as f:
    f.write("Hi Hari!\nWelcome to Python I/O \n")
    f.write("heyyy \n")
    f.write("heyyy suuupp \n    welcome to india ! \n")

# Read from file
    content = f.read()
    print(content)
    f.seek(0)


