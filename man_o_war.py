

status_of_pirates_ship = [input().join(">") for _ in range(10)]
status_of_warship = [input().join(">") for _ in range(10)]
max_health = int(input())

while True:
    command = input().split()
    if command[0] == "Retire":
        break
    elif command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(status_of_warship):
            status_of_warship[index] -= damage
            if status_of_warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < len(status_of_pirates_ship) and 0 <= end_index < len(status_of_pirates_ship):
            for i in range(start_index, end_index + 1):
                status_of_pirates_ship[i] -= damage
                if status_of_pirates_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(status_of_pirates_ship):
            status_of_pirates_ship[index] += health
            if status_of_pirates_ship[index] > max_health:
                status_of_pirates_ship[index] = max_health
    elif command[0] == "Status":
        count = 0
        for i in status_of_pirates_ship:
            if i < max_health * 0.2:
                count += 1
        print(f"{count} sections need repair.")