from collections import deque

potions = {
    110: "Brew of Immortality",
    100: "Essence of Resilience",
    90: "Draught of Wisdom",
    80: "Potion of Agility",
    70: "Elixir of Strength"
}

crafted = set()
crafted_list = []

substances = list(map(int, input().split(', ')))
crystals = deque(map(int, input().split(', ')))

while substances and crystals and len(crafted) < 5:
    sub = substances.pop()
    cry = crystals.popleft()
    total = sub + cry

    if total in potions and potions[total] not in crafted:
        crafted.add(potions[total])
        crafted_list.append(potions[total])
        continue

    found = False
    for energy in sorted(potions.keys(), reverse=True):
        if energy < total and potions[energy] not in crafted:
            crafted.add(potions[energy])
            crafted_list.append(potions[energy])
            cry -= 20
            if cry > 0:
                crystals.append(cry)
            found = True
            break

    if not found:
        cry -= 5
        if cry > 0:
            crystals.append(cry)

if len(crafted) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_list:
    print("Crafted potions: " + ", ".join(crafted_list))

if substances:
    print("Substances: " + ", ".join(map(str, substances[::-1])))

if crystals:
    print("Crystals: " + ", ".join(map(str, crystals)))
