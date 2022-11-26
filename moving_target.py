

# You are at the shooting gallery again, and you need a program that helps you keep track of moving targets. 
# On the first line, you will receive a sequence of targets with their integer values, split by a single space. 
# Then, you will start receiving commands for manipulating the targets until the "End" command. 
# The commands are the following:
# •	"Shoot {index} {power}"
# o	Shoot the target at the index if it exists by reducing its value by the given power (integer value). 
# o	Remove the target if it is shot. A target is considered shot when its value reaches 0.
# •	"Add {index} {value}"
# o	Insert a target with the received value at the received index if it exists. 
# o	If not, print: "Invalid placement!"
# •	"Strike {index} {radius}"
# o	Remove the target at the given index and the ones before and after it depending on the radius.
# o	If any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
#  Example:  "Strike 2 2"
# 	{radius}	{radius}	{strikeIndex}	{radius}	{radius}		

# •	"End"
# o	Print the sequence with targets in the following format and end the program:
# "{target1}|{target2}…|{targetn}"
# Input / Constraints
# •	On the first line, you will receive the sequence of targets – integer values [1-10000].
# •	On the following lines, until the "End" will be receiving the command described above – strings.
# •	There will never be a case when the "Strike" command would empty the whole sequence.
# Output
# •	Print the appropriate message in case of any command if necessary.
# •	In the end, print the sequence of targets in the format described above.


target_list = [int(x) for x in input().split()]

command_list = input().split()

while len(command_list) > 1:
    command = command_list[0]
    index = int(command_list[1])
    if command == "Shoot":
        power = int(command_list[2])
        if index in range(len(target_list)):
            target_list[index] -= power
            if target_list[index] <= 0:
                target_list.pop(index)
    elif command == "Add":
        value = int(command_list[2])
        if index in range(len(target_list)):
            target_list.insert(index, value)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        radius = int(command_list[2])
        if index in range(len(target_list)) and index - radius in range(len(target_list)) and index + radius in range(len(target_list)):
            del target_list[index - radius: index + radius + 1]
        else:
            print("Strike missed!")
    command_list = input().split()


print('|'.join([str(x) for x in target_list]))