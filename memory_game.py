

# Memory game
# Write a program that recreates the Memory game.
# On the first line, you will receive a sequence of elements. 
# Each element in the sequence will have a twin. 
# Until the player receives "end" from the console, you will receive strings with two integers separated by a space, representing the indexes of elements in the sequence.
# If the player tries to cheat and enters two equal indexes or indexes which are out of the bounds of the sequence, you should add two matching elements at the middle of the sequence in the following format:
# "-{number of moves until now}a" 
# Then print this message on the console:
# "Invalid input! Adding additional elements to the board"
# Input
# •	On the first line, you will receive a sequence of elements
# •	On the following lines, you will receive integers until the command "end"
# Output
# •	Every time the player hit two matching elements, you should remove them from the sequence and print on the console the following message:
# "Congrats! You have found matching elements - ${element}!"
# •	If the player hit two different elements, you should print on the console the following message:
# "Try again!"
# •	If the player hit all matching elements before he receives "end" from the console, you should print on the console the following message: 
# "You have won in {number of moves until now} turns!"
# •	If the player receives "end" before he hits all matching elements, you should print on the console the following message:
# "Sorry you lose :({the current sequence's state}"

initial_sequence = input().split()
command = input().split()

while command[0] != "end":
    if int(command[0]) == int(command[1]) or int(command[0]) > len(initial_sequence) or int(command[1]) > len(initial_sequence):
        initial_sequence.insert(len(initial_sequence) // 2, f"-{len(initial_sequence)}a")
        initial_sequence.insert(len(initial_sequence) // 2, f"-{len(initial_sequence)}a")
        print("Invalid input! Adding additional elements to the board")
    elif initial_sequence[int(command[0])] == initial_sequence[int(command[1])]:
        print(f"Congrats! You have found matching elements - {initial_sequence[int(command[0])]}!")
        initial_sequence.pop(int(command[0]))
        initial_sequence.pop(int(command[1]) - 1)
    else:
        print("Try again!")
    if len(initial_sequence) == 0:
        print(f"You have won in {len(command)} turns!")
        break
    command = input().split()
if len(initial_sequence) > 0:
    print(f"Sorry you lose :(")
    print(" ".join(initial_sequence))
