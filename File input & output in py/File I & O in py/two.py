file_name = "demo_file.txt"

# 1️⃣ 'w' – Write (overwrites if file exists)
with open(file_name, "w") as f:
    f.write("Write mode: This will overwrite any existing content.\n")

# 2️⃣ 'r' – Read (fails if file doesn't exist)
try:
    with open(file_name, "r") as f:
        print("Read mode output:\n", f.read())
except FileNotFoundError:
    print("File not found while trying 'r' mode.")

# 3️⃣ 'r+' – Read and Write (file must exist)
try:
    with open(file_name, "r+") as f:
        content = f.read()
        print("Read+Write mode output:\n", content)
        f.seek(0)  # Reset pointer
        f.write("r+ mode updated this line.\n")  # Overwrites from beginning
except FileNotFoundError:
    print("File not found while trying 'r+' mode.")

# 4️⃣ 'w+' – Write and Read (file gets overwritten!)
with open(file_name, "w+") as f:
    f.write("w+ mode: This overwrites and allows reading.\n")
    f.seek(0)
    print("Write+Read mode output:\n", f.read())

# 5️⃣ 'a+' – Append and Read (adds to end, reads full file)
with open(file_name, "a+") as f:
    f.write("a+ mode: This gets appended at the end.\n")
    f.seek(0)  # Move pointer to beginning to read everything
    print("Append+Read mode output:\n", f.read())