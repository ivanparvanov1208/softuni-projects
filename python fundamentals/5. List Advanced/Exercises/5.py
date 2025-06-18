def check(rooms):
    ready = False
    free_chairs = 0
    for i in range(1, rooms + 1):

        chairs, visitors = input().split()

        chairsCount = 0

        for _ in chairs:
            chairsCount += 1

        if chairsCount < int(visitors):
            diff = int(visitors) - chairsCount
            print(f"{diff} more chairs needed in room {i}")
            ready = False
        else:
            free_chairs += chairsCount - int(visitors)
            ready = True

    if ready:
        print(f"Game On, {free_chairs} chairs left")


roomsAmount = int(input())

check(roomsAmount)