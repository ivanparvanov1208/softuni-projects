from string import punctuation

with open("input.txt") as input_file, open("output.txt", 'w') as output_file:
    result = []
    for row, line in enumerate(input_file):
        lettersCount = 0
        puncCount = 0
        for ch in line:
            if ch.isalpha():
                lettersCount += 1
            elif ch in punctuation:
                puncCount += 1

        result.append(f"Line {row + 1}: {line.strip()} ({lettersCount})({puncCount})")

    output_file.write("\n".join(result))
