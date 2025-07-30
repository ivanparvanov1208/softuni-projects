def decipher_this(text):
    words = text.split()
    deciphered_words = []
    for word in words:
        i = 0
        while i < len(word) and word[i].isdigit():
            i += 1
        char_code = word[:i]
        letters = word[i:]

        first_letter = chr(int(char_code))

        if len(letters) >= 2:
            switched = letters[-1] + letters[1:-1] + letters[0]
        elif len(letters) == 1:
            switched = letters
        else:
            switched = ""

        deciphered_word = first_letter + switched
        deciphered_words.append(deciphered_word)

    return ' '.join(deciphered_words)

print(decipher_this(input()))
