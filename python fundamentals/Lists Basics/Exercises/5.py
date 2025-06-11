cards_string = input()
shuffle_count = int(input())

deck = cards_string.split()

for _ in range(shuffle_count):
  n = len(deck)
  half = n // 2
  left = deck[:half]
  right = deck[half:]
  shuffled_deck = []
  for i in range(half):
    shuffled_deck.append(left[i])
    shuffled_deck.append(right[i])
  deck = shuffled_deck

print(deck)