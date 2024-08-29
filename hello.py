import os

def delete_file(filename):
    os.system(f"rm {filename}")

# Example usage:
filename = input("Enter the name of the file to delete: ")
delete_file(filename)
