import os
def generateTable(n):
    """
    Generates a multiplication table for the given number n (from 1 to 10)
    and writes it twice to a file named 'tables/tables_n.txt'.

    Parameters:
    n (int): The number for which the multiplication table is generated.
    """
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    os.makedirs("tables",exist_ok=True)
    with open(f"tables/tables_{n}.txt", "w") as f:
        f.write(table)



for j in range(2,21):
    generateTable(j)