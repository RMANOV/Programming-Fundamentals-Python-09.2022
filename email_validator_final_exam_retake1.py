# Input
# •	The possible commands are:
# o	"Complete"
# o	"Make Upper"
# o	"Make Lower"
# o	"GetDomain {count}"
# o	"GetUsername"
# o	"Replace {char}"
# o	"Encrypt"
# Output
# Print the result of every command on a new line.
# •	The possible outputs are:
# o	"The email {email} doesn't contain the @ symbol."

inirial_string = input()

while True:
    command = input()
    if command == "Complete":
        break
    command = command.split()
    if command[0] == "Make":
        if command[1] == "Upper":
            inirial_string = inirial_string.upper()
            print(inirial_string)
        elif command[1] == "Lower":
            inirial_string = inirial_string.lower()
            print(inirial_string)
    elif command[0] == "GetDomain":
        count = int(command[1])
        print(inirial_string[-count:])
    elif command[0] == "GetUsername":
        if "@" in inirial_string:
            print(inirial_string[:inirial_string.index("@")])
        else:
            print(f"The email {inirial_string} doesn't contain the @ symbol.")
    elif command[0] == "Replace":
        inirial_string = inirial_string.replace(command[1], "-")
        print(inirial_string)
    elif command[0] == "Encrypt":
        for i in inirial_string:
            print(ord(i), end=" ")
