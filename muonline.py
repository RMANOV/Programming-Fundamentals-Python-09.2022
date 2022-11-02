

initial_health = 100
inintial_bitcoins = 0

rooms = input().split("|")

health = initial_health
bitcoins = inintial_bitcoins

for room in rooms:
    command, value = room.split()
    value = int(value)
    if command == "potion":
        if health + value > 100:
            value = 100 - health
        health += value
        print(f"You healed for {value} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {rooms.index(room) + 1}")
            break
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

# Path: muonline.py
