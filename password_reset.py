

# Write a password reset program that performs a series of commands upon a predefined string. 
# First, you will receive a string, and afterward, until the command "Done" is given, you will be receiving strings with commands split by a single space. 
# The commands will be the following:
# •	"TakeOdd"
# o	 Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
# •	"Cut {index} {length}"
# o	Gets the substring with the given length starting from the given index from the password and removes its first occurrence, then prints the password on the console.
# o	The given index and the length will always be valid.
# •	"Substitute {substring} {substitute}"
# o	If the raw password contains the given substring, replaces all of its occurrences with the substitute text given and prints the result.
# o	If it doesn't, prints "Nothing to replace!".
# Input
# •	You will be receiving strings until the "Done" command is given.
# Output
# •	After the "Done" command is received, print:
# o	"Your password is: {password}"

initial_password = input()
command = input()

while not command == "Done":
    command = command.split()
    if command[0] == "TakeOdd":
        initial_password = initial_password[1::2]
        print(initial_password)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        initial_password = initial_password[:index] + initial_password[index + length:]
        print(initial_password)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in initial_password:
            initial_password = initial_password.replace(substring, substitute)
            print(initial_password)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {initial_password}")
