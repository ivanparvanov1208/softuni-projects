name = input()

count = 0
loss_count = 0
total_sum = 0
failed_year = 0

while count < 12:
    grade = float(input())

    if grade >= 4:
        total_sum += grade
        count += 1
    else:
        loss_count += 1
        if loss_count == 2:
            failed_year = count + 1
            print(f"{name} has been excluded at {failed_year} grade")
            break
        continue

else:
    average = total_sum / 12
    print(f"{name} graduated. Average grade: {average:.2f}")