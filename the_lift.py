

# Write a program that finds a place for the tourist on a lift. 
# Every wagon should have a maximum of 4 people on it. 
# If a wagon is full, you should direct the people to the next one with space available.
# Input
# •	On the first line, you will receive how many people are waiting to get on the lift
# •	On the second line, you will receive the current state of the lift separated by a single space: " ".
# Output
# When there is no more available space left on the lift, or there are no more people in the queue, 
# you should print on the console the final state of the lift's wagons separated by " " and one of the following messages:
# •	If there are no more people and the lift have empty spots, you should print:
# "The lift has empty spots!
# {wagons separated by ' '}"
# •	If there are still people in the queue and no more available space, you should print:
# "There isn't enough space! {people} people in a queue!
# {wagons separated by ' '}"
# •	If the lift is full and there are no more people in the queue, you should print only the wagons separated by " "

numbers_of_people = int(input())
wagons = [int(x) for x in input().split()]

for i in range(len(wagons)):
    while wagons[i] < 4:
        wagons[i] += 1
        numbers_of_people -= 1
        if numbers_of_people == 0:
            break
        if wagons[i] == 4:
            break
    
if numbers_of_people == 0:
    print("The lift has empty spots!")
    print(*wagons)
elif numbers_of_people > 0:
    print(f"There isn't enough space! {numbers_of_people} people in a queue!")
    print(*wagons)
else:
    print(*wagons)
    
