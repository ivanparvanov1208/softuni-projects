with open("text1.txt") as f:
    for row, line in enumerate(f):
        if row % 2 == 0:
            for ch in {"-", ",", ".", "!", "?"}:
                line = line.replace(ch, "@")
            print(" ".join(reversed(line.split())))