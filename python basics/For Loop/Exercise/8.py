from math import floor

tournaments = int(input())
points = int(input())

average = 0
winTour = 0

for i in range(tournaments):
    status = input()

    if status == "W":
        points += 2000
        average += 2000
        winTour += 1
    elif status == "F":
        points += 1200
        average += 1200
    elif status == "SF":
        points += 720
        average += 720

average = average / tournaments
average = floor(average)

percentWinTour = winTour / tournaments * 100

print(f"Final points: {points}\nAverage points: {average}\n{percentWinTour:.2f}%")

