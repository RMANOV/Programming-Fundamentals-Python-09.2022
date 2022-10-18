

nuber_of_rooms = int(input())
free_chairs = 0
enough_chairs = True

for room in range(1, nuber_of_rooms + 1):
    chairs, people = input().split()
    if len(chairs) >= int(people):
        free_chairs += len(chairs) - int(people)
    else:
        print(f"{int(people) - len(chairs)} more chairs needed in room {room}")
        enough_chairs = False

if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")

