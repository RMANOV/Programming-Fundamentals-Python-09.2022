

# The list may be manipulated by one of the following commands:
# •	"exchange {index}" – splits the list after the given index and exchanges the places of the two resulting sub-lists. E.g., [1, 2, 3, 4, 5] -> "exchange 2" -> result: [4, 5, 1, 2, 3]
# o	If the index is outside the boundaries of the list, print "Invalid index"
# o	A negative index is considered invalid
# •	"max even/odd"– returns the INDEX of the max even/odd element. E.g., [1, 4, 8, 2, 3] -> "max odd" -> print: 8
# •	"min even/odd" – returns the INDEX of the min even/odd element. E.g. [1, 4, 8, 2, 3] -> "min even" -> print: 2
# o	If there are two or more equal min/max elements, return the index of the rightmost one
# o	If a min/max even/odd element cannot be found, print "No matches"
# •	"first {count} even/odd" – returns the first count even/odd elements. E.g. [1, 8, 2, 3] -> "first 2 even" -> print [8, 2]
# •	"last {count} even/odd" – returns the last count even/odd elements. E.g. [1, 8, 2, 3] -> "last 2 odd" -> print [1, 3]
# o	If the count is greater than the list length, print "Invalid count"
# o	If there are not enough elements to satisfy the count, print as many as you can. 
# If there are zero even/odd elements, print an empty list "[]"
# •	"end" - stop taking input and print the final state of the list
# Input
# •	The input data should be read from the console.
# •	On the first line, the initial list is received as a line of integers, separated by a single space.
# •	On the following lines, until the command "end" is received, you will receive the list manipulation commands.
# •	The input data will always be valid and in the format described. There is no need to check it explicitly.
# Output
# •	The output should be printed on the console.
# •	On a separate line, print the output of the corresponding command.
# •	On the last line, print the final list in square brackets with its elements separated by a comma and a space.
# •	See the examples below to get a better understanding of your task.
# Constraints
# •	The number of input lines will be in the range [2 … 50].
# •	The list elements will be integers in the range [0 … 1000].
# •	The number of elements will be in the range [1 .. 50].
# •	The split index will be an integer in the range [-231 … 231 – 1].
# •	The first/last count will be an integer in the range [1 … 231 – 1].
# •	There will not be redundant whitespace anywhere in the input.

initial_list = [int(x) for x in input().split()]

while True:
    command = input().split()
    if command[0] == "end":
        break
    elif command[0] == "exchange":
        if int(command[1]) not in range(len(initial_list)):
            print("Invalid index")
        else:
            initial_list = initial_list[int(command[1]) + 1 :] + initial_list[: int(command[1]) + 1]
    elif command[0] == "max":
        if command[1] == "even":
            max_even = max([x for x in initial_list if x % 2 == 0], default="No matches")
            if max_even == "No matches":
                print("No matches")
            else:
                print(initial_list.index(max_even))
        elif command[1] == "odd":
            max_odd = max([x for x in initial_list if x % 2 != 0], default="No matches")
            if max_odd == "No matches":
                print("No matches")
            else:
                print(initial_list.index(max_odd))
    elif command[0] == "min":
        if command[1] == "even":
            min_even = min([x for x in initial_list if x % 2 == 0], default="No matches")
            if min_even == "No matches":
                print("No matches")
            else:
                print(initial_list.index(min_even))
        elif command[1] == "odd":
            min_odd = min([x for x in initial_list if x % 2 != 0], default="No matches")
            if min_odd == "No matches":
                print("No matches")
            else:
                print(initial_list.index(min_odd))
    elif command[0] == "first":
        if int(command[1]) > len(initial_list):
            print("Invalid count")
        elif command[2] == "even":
            first_even = [x for x in initial_list if x % 2 == 0][: int(command[1])]
            print(first_even)
        elif command[2] == "odd":
            first_odd = [x for x in initial_list if x % 2 != 0][: int(command[1])]
            print(first_odd)
    elif command[0] == "last":
        if int(command[1]) > len(initial_list):
            print("Invalid count")
        elif command[2] == "even":
            last_even = [x for x in initial_list if x % 2 == 0][-int(command[1]) :]
            print(last_even)
        elif command[2] == "odd":
            last_odd = [x for x in initial_list if x % 2 != 0][-int(command[1]) :]
            print(last_odd)

print(initial_list)
