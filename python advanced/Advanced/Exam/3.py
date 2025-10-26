def classify_books(*args, **kwargs):
    titleToISBN = {value: key for key, value in kwargs.items()}

    fiction = []
    non_fiction = []

    for genre, title in args:
        isbn = titleToISBN[title]
        if genre == "fiction":
            fiction.append((isbn, title))
        elif genre == "non_fiction":
            non_fiction.append((isbn, title))

    fiction.sort(key=lambda x: x[0])

    non_fiction.sort(key=lambda x: x[0], reverse=True)

    output = []
    if fiction:
        output.append("Fiction Books:")
        for isbn, title in fiction:
            output.append(f"~~~{isbn}#{title}")
    if non_fiction:
        output.append("Non-Fiction Books:")
        for isbn, title in non_fiction:
            output.append(f"***{isbn}#{title}")

    return "\n".join(output)