with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = len(file_contents.split())
    print(file_contents)
    print("Word count = ", words)