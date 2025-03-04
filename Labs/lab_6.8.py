import os

file = "a.txt"

if os.path.exists(file):
    if os.access(file, os.W_OK):
        os.remove(file)
        print("Deleted successfully.")
    else:
        print("No permission to delete.")
else:
    print("File does not exist.")