terminatedPlayers = []

playersACount = 11
playersBCount = 11

cardsList = input().split(" ")

terminated = False

for card in cardsList:
    player = card

    if player in terminatedPlayers:
        continue
    else:
        terminatedPlayers.append(card)
        if card.split("-")[0] == "A":
            playersACount -= 1
        elif card.split("-")[0] == "B":
            playersBCount -= 1

        if playersACount < 7 or playersBCount < 7:
            terminated = True
            break;

print(f"Team A - {playersACount}; Team B - {playersBCount}")
if terminated:
    print("Game was terminated")