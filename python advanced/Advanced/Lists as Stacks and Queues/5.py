number_of_pumps = int(input())

petrol_pumps = []
for _ in range(number_of_pumps):
    petrol_pumps.append(list(map(int, input().split())))

current_petrol = 0
start_index = 0

for i in range(number_of_pumps):
    petrol, distance = petrol_pumps[i]
    current_petrol += petrol - distance

    if current_petrol < 0:
        start_index = i + 1
        current_petrol = 0

print(start_index)
