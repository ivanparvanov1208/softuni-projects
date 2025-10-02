text = input()

unique_chars = set(text)

sorted_chars = sorted(unique_chars)

for char in sorted_chars:
    count = text.count(char)
    print(f"{char}: {count} time/s")
