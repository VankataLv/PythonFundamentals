total_rooms = int(input())
free_chairs = 0
insufficient_chairs = 0
enough_chairs = True

for room_number in range(1, total_rooms + 1):
    current_room = list(input().split(" "))
    current_room[1] = int(current_room[1])
    if len(current_room[0]) >= current_room[1]:
        free_chairs += len(current_room[0]) - current_room[1]
    else:
        enough_chairs = False
        print(f"{current_room[1] - len(current_room[0])} more chairs needed in room {room_number}")

if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")
