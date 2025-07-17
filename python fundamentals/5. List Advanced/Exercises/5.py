def check(rooms):
    free_chairs = 0
    all_rooms_ready = True

    for i in range(1, rooms + 1):
        chairs, visitors = input().split()
        chairs_count = int(chairs)
        visitors_count = int(visitors)


        if chairs_count < visitors_count:
            diff = visitors_count - chairs_count
            print(f"{diff} more chairs needed in room {i}")
            all_rooms_ready = False
        else:
            free_chairs += chairs_count - visitors_count

    if all_rooms_ready:
        print(f"Game On, {free_chairs} free chairs left")


rooms_amount = int(input())
check(rooms_amount)
