#write a python program to print the contents of a directory using the os module
import os

def list_directory_contents(directory):
    try:
        # Get the list of files and directories
        contents = os.listdir(directory)
        
        # Print each item in the directory
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("Error: Directory not found")
    except PermissionError:
        print("Error: Permission denied")

# Example usage
directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)
