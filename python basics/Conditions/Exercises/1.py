firstTime = int(input())
secondTime = int(input())
thirdTime = int(input())

totalTime = firstTime + secondTime + thirdTime

minutes = totalTime // 60
seconds = totalTime % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")

