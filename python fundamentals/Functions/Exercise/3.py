def characters_in_between(char1 = input(), char2 = input()):
    start = ord(char1)
    end = ord(char2)
    if start > end:
        start, end = end, start
    characters = [chr(i) for i in range(start + 1, end)]
    return ' '.join(characters)

result = characters_in_between()
print(result)
