

# You are a world traveler, and your next goal is to make a world tour. 
# To do that, you have to plan out everything first. 
# To start with, you would like to plan out all of your stops where you will have a break.
# On the first line, you will be given a string containing all of your stops. 
# Until you receive the command "Travel", you will be given some commands to manipulate that initial string.
# The commands can be:
# •	"Add Stop:{index}:{string}":
# o	Insert the given string at that index only if the index is valid
# •	"Remove Stop:{start_index}:{end_index}":
# o	Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
# •	"Switch:{old_string}:{new_string}":
# o	If the old string is in the initial string, replace it with the new one (all occurrences)
# Note: After each command, print the current state of the string if it is valid!
# After the "Travel" command, print the following: "Ready for a world tour! Planned stops: {string}"
# Input / Constraints
# •	An index is valid if it is between the first and the last element index (inclusive) (0 ….. Nth) in the sequence.
# Output
# •	Print the proper output messages in the proper cases as described in the problem description

initial_string = input()
command = input().split(':')

while command != 'Travel':
    command = command[0]
    second_string = command[1]
    if command == 'Add stop':
        pass
    if command == 'Remove stop':
        pass
    if command == 'Switch stop':
        trird_string = command[2]
        pass
    
