amount = int(input())
for i in range(amount):
    entry = input()

    if ":" not in entry:
        print("Access denied!")
        continue
    bossName, title = entry.split(":", 1)
    stripped_boss_name = bossName.strip("|")
    stripped_title = title.strip("#")
    integerFound = any(char.isdigit() for char in stripped_title)
    if (len(bossName) >= 4 and
            bossName[0] == "|" and
            stripped_boss_name.isupper() and
            bossName[-1] == "|" and
            title[0] == "#" and
            title[-1] == "#" and
            len(stripped_title.split()) == 2 and
            not integerFound):

        print(
            f"{stripped_boss_name}, The {stripped_title}\n>> Strength: {len(stripped_boss_name)}\n>> Armor: {len(stripped_title)}")
    else:
        print("Access denied!")