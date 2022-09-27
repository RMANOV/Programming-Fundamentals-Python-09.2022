

people = int(input())
capacity = int(input())

print(people // capacity + (people % capacity > 0))