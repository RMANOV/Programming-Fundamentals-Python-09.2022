# Write a program that helps you keep track of your shot targets.
# You will receive a sequence with integers, separated by a single space, representing targets and their value.
# Afterward, you will be receiving indices until the "End" command is given, and you need to print the targets and the count of shot targets.
# Every time you receive an index, you need to shoot the target on that index, if it is possible.
# Every time you shoot a target, its value becomes -1, and it is considered a shot.
# Along with that, you also need to:
# •	Reduce all the other targets, which have greater values than your current target, with its value.
# •	Increase all the other targets, which have less than or equal value to the shot target, with its value.
# Keep in mind that you can't shoot a target, which is already shot. You also can't increase or reduce a target, which is considered a shot.
# When you receive the "End" command, print the targets in their current state and the count of shot targets in the following format:
# "Shot targets: {count} -> {target1} {target2}… {targetn}"
# Input / Constraints
# •	On the first line of input, you will receive a sequence of integers, separated by a single space – the target sequence.
# •	On the following lines, until the "End" command, you be receiving integers each on a single line – the index of the target to be shot.
# Output
# Shot targets 3 -> -1 -1 130 -1
# Shot targets: 4 -> -1 120 -1 66 -1 -1

target_list = input().split()
target_list = [int(x) for x in input().split() if int(x) != ""]
shots_number = 0
current_state = 0

target_index = input()

while target_index != 'End':
    if target_index != 'End':
        target_index = int(target_index)
    if target_index >= len(target_list):
        target_index = input()
        continue
    current_state = target_list[target_index]
    target_list[target_index] = -1
    shots_number += 1

    for i in range(len(target_list)):
        if target_list[i] == target_list[target_index]:
            continue
        if target_list[i] > current_state:
            target_list[i] -= current_state
        else:
            target_list[i] += current_state
    current_state = 0
    target_index = input()


# print(f'Shot targets: {shots_number} -> {"".join(target_list)}')
print(shots_number)
print(*target_list)
