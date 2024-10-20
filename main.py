with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = len(file_contents.split())

    lowered_string = file_contents.lower()
    char_count = {}
    for char in lowered_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

    #print(file_contents)
    print("Word count = ", words)