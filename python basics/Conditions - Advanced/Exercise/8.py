exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute

time_difference = arrival_time - exam_time

if time_difference < -30:
    print("Early")
    time_difference = abs(time_difference)
    if time_difference < 60:
        print(f"{time_difference} minutes before the start")
    else:
        hours = time_difference // 60
        minutes = time_difference % 60
        print(f"{hours}:{minutes:02d} hours before the start")
elif time_difference <= 0:
    print("On time")
    if time_difference < 0:
        print(f"{abs(time_difference)} minutes before the start")
elif time_difference > 0:
    print("Late")
    if time_difference < 60:
        print(f"{time_difference} minutes after the start")
    else:
        hours = time_difference // 60
        minutes = time_difference % 60
        print(f"{hours}:{minutes:02d} hours after the start")