rooms_number =  int(input())

spare_chairs = 0
needed_chairs = 0

for room in range(1, rooms_number + 1):
    filling_list = input().split(" ")
    chairs_number = len(filling_list[0])
    visitors = int(filling_list[1])
    current_needed_chairs = 0
    if visitors > chairs_number:
        current_needed_chairs += visitors - chairs_number
        print(f"{current_needed_chairs} more chairs needed in room {room}")
        needed_chairs += current_needed_chairs
    else:
        spare_chairs += chairs_number - visitors

if needed_chairs == 0:
    print(f"Game On, {spare_chairs} free chairs left")