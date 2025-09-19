total_food = int(input())
orders_list = list(map(int, input().split()))

if orders_list:
    biggest_order = max(orders_list)
    print(biggest_order)

while orders_list and total_food >= orders_list[0]:
    order_to_serve = orders_list.pop(0)
    total_food -= order_to_serve

if not orders_list:
    print("Orders complete")
else:
    orders_left = [str(o) for o in orders_list]
    print(f"Orders left: {' '.join(orders_left)}")
