

# Input
# •	The possible commands are:
# o	"End"
# o	"Translate {char} {replacement}"
# o	"Includes {substring}"
# o	"Start {substring}"
# o	"Lowercase"
# o	"FindIndex {char}"
# o	"Remove {startIndex} {count}"
# Output
# •	The possible outputs are:
# o	"True"
# o	"False"


initial_string = input()

while True:
    line = input()
    if line == "End":
        break
    command = line.split()[0]
    if command == "Translate":
        char, replacement = line.split()[1:]
        initial_string = initial_string.replace(char, replacement)
        print(initial_string)
    elif command == "Includes":
        substring = line.split()[1]
        if substring in initial_string:
            print("True")
        else:
            print("False")
    elif command == "Start":
        substring = line.split()[1]
        if initial_string.startswith(substring):
            print("True")
        else:
            print("False")
    elif command == "Lowercase":
        initial_string = initial_string.lower()
    elif command == "FindIndex":
        char = line.split()[1]
        print(initial_string.rfind(char))
    elif command == "Remove":
        start_index, count = line.split()[1:]
        initial_string = initial_string[:int(start_index)] + initial_string[int(start_index) + int(count):]


print(initial_string)
