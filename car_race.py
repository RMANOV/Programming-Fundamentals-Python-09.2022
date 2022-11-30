

# Write a program that announces the winner of a car race. 
# You will receive a sequence of numbers. 
# Each number represents the time needed for the car to pass through that step (the index). 
# There will be two cars. The first one starts from the left side, and the other one starts from the right side. 
# The middle index of the sequence is the finish line. 
# Calculate the total time each racer needs to reach the finish line and print the winner with his total time (the racer with less time). 
# If you have a zero in the list, you should reduce the racer's time that reached it by 20% (from his current time).
# The number of elements in the sequence will always be odd.
# Print the result in the following format "The winner is {left/right} with total time: {total_time}".

initial_sequence = [float(i) for i in input().split()]

left_car_time = 0
right_car_time = 0

for i in range(len(initial_sequence) // 2):
    if initial_sequence[i] == 0:
        left_car_time *= 0.8
    else:
        left_car_time += initial_sequence[i]
    if initial_sequence[-i - 1] == 0:
        right_car_time *= 0.8
    else:
        right_car_time += initial_sequence[-i - 1]

print(f"The winner is {'left' if left_car_time < right_car_time else 'right'} with total time: {min(left_car_time, right_car_time):.1f}")