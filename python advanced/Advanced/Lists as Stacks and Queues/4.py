clothes_values = list(map(int, input().split()))
rack_capacity = int(input())

racks_used = 1
current_rack_sum = 0

while clothes_values:
    current_clothing = clothes_values[-1]

    if current_rack_sum + current_clothing <= rack_capacity:
        current_rack_sum += clothes_values.pop()
    else:
        racks_used += 1
        current_rack_sum = clothes_values.pop()

print(racks_used)