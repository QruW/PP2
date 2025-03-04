def copy_content(file1, file2):
    try:
        with open(file1, 'r') as source, open(file2, 'w') as destination:
            destination.write(source.read())
    except FileNotFoundError:
        print("File not found.")

copy_content("a.txt", "B.txt")