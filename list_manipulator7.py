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
even_list = []
odd_list = []
max_even = 0
min_even = 0
max_odd = 0
min_odd = 0

command = input()
while command != "end":
    command = command.split()
    if command[0] == "exchange":
        index = int(command[1])
        if index < 0 or index >= len(initial_list):
            print("Invalid index")
        else:
            initial_list = initial_list[index + 1:] + initial_list[:index + 1]
    elif command[0] == "max":
        if command[1] == "even":
            for i in range(len(initial_list)):
                if initial_list[i] % 2 == 0:
                    even_list.append(initial_list[i])
            if len(even_list) == 0:
                print("No matches")
            else:
                max_even = max(even_list)
                print(initial_list.index(max_even))
        elif command[1] == "odd":
            for i in range(len(initial_list)):
                if initial_list[i] % 2 != 0:
                    odd_list.append(initial_list[i])
            if len(odd_list) == 0:
                print("No matches")
            else:
                max_odd = max(odd_list)
                print(initial_list.index(max_odd))
    elif command[0] == "min":
        if command[1] == "even":
            for i in range(len(initial_list)):
                if initial_list[i] % 2 == 0:
                    even_list.append(initial_list[i])
            if len(even_list) == 0:
                print("No matches")
            else:
                min_even = min(even_list)
                print(initial_list.index(min_even))
        elif command[1] == "odd":
            for i in range(len(initial_list)):
                if initial_list[i] % 2 != 0:
                    odd_list.append(initial_list[i])
            if len(odd_list) == 0:
                print("No matches")
            else:
                min_odd = min(odd_list)
                print(initial_list.index(min_odd))
    elif command[0] == "first":
        count = int(command[1])
        if count > len(initial_list):
            print("Invalid count")
        else:
            if command[2] == "even":
                for i in range(len(initial_list)):
                    if initial_list[i] % 2 == 0:
                        even_list.append(initial_list[i])
                if len(even_list) == 0:
                    print("[]")
                else:
                    print(even_list[:count])
            elif command[2] == "odd":
                for i in range(len(initial_list)):
                    if initial_list[i] % 2 != 0:
                        odd_list.append(initial_list[i])
                if len(odd_list) == 0:
                    print("[]")
                else:
                    print(odd_list[:count])
    elif command[0] == "last":
        count = int(command[1])
        if count > len(initial_list):
            print("Invalid count")
        else:
            if command[2] == "even":
                for i in range(len(initial_list)):
                    if initial_list[i] % 2 == 0:
                        even_list.append(initial_list[i])
                if len(even_list) == 0:
                    print("[]")
                else:
                    print(even_list[-count:])
            elif command[2] == "odd":
                for i in range(len(initial_list)):
                    if initial_list[i] % 2 != 0:
                        odd_list.append(initial_list[i])
                if len(odd_list) == 0:
                    print("[]")
                else:
                    print(odd_list[-count:])
    command = input()

print('[' + ', '.join([str(x) for x in initial_list]) + ']')















# initial_list = [int(x) for x in input().split()]
# command = input()
# while command != "end":
#     command = command.split()
#     if command[0] == "exchange":
#         index = int(command[1])
#         if index < 0 or index >= len(initial_list):
#             print("Invalid index")
#         else:
#             initial_list = initial_list[index + 1:] + initial_list[:index + 1]
#     elif command[0] == "max":
#         if command[1] == "even":
#             even_list = [x for x in initial_list if x % 2 == 0]
#             if len(even_list) == 0:
#                 print("No matches")
#             else:
#                 print(initial_list.index(max(even_list)))
#         elif command[1] == "odd":
#             odd_list = [x for x in initial_list if x % 2 != 0]
#             if len(odd_list) == 0:
#                 print("No matches")
#             else:
#                 print(initial_list.index(max(odd_list)))
#     elif command[0] == "min":
#         if command[1] == "even":
#             even_list = [x for x in initial_list if x % 2 == 0]
#             if len(even_list) == 0:
#                 print("No matches")
#             else:
#                 print(initial_list.index(min(even_list)))
#         elif command[1] == "odd":
#             odd_list = [x for x in initial_list if x % 2 != 0]
#             if len(odd_list) == 0:
#                 print("No matches")
#             else:
#                 print(initial_list.index(min(odd_list)))
#     elif command[0] == "first":
#         count = int(command[1])
#         if count > len(initial_list):
#             print("Invalid count")
#         else:
#             if command[2] == "even":
#                 even_list = [x for x in initial_list if x % 2 == 0]
#                 if len(even_list) == 0:
#                     print("[]")
#                 else:
#                     print(even_list[:count])
#             elif command[2] == "odd":
#                 odd_list = [x for x in initial_list if x % 2 != 0]
#                 if len(odd_list) == 0:
#                     print("[]")
#                 else:
#                     print(odd_list[:count])
#     elif command[0] == "last":
#         count = int(command[1])
#         if count > len(initial_list):
#             print("Invalid count")
#         else:
#             if command[2] == "even":
#                 even_list = [x for x in initial_list if x % 2 == 0]
#                 if len(even_list) == 0:
#                     print("[]")
#                 else:
#                     print(even_list[-count:])
#             elif command[2] == "odd":
#                 odd_list = [x for x in initial_list if x % 2 != 0]
#                 if len(odd_list) == 0:
#                     print("[]")
#                 else:
#                     print(odd_list[-count:])
#     command = input()

# print('[' + ', '.join([str(x) for x in initial_list]) + ']')


# def exchange(lst, index):
#     if index < 0 or index >= len(lst):
#         print("Invalid index")
#         return lst
#     return lst[index + 1:] + lst[:index + 1]

# def max_even_odd(lst, even_odd):
#     max_even_odd = -1
#     max_even_odd_index = -1
#     for i in range(len(lst)):
#         if lst[i] % 2 == 0 and even_odd == "even" and lst[i] >= max_even_odd:
#             max_even_odd = lst[i]
#             max_even_odd_index = i
#         elif lst[i] % 2 != 0 and even_odd == "odd" and lst[i] >= max_even_odd:
#             max_even_odd = lst[i]
#             max_even_odd_index = i
#     if max_even_odd_index == -1:
#         print("No matches")
#     else:
#         print(max_even_odd_index)

# def min_even_odd(lst, even_odd):
#     min_even_odd = 1001
#     min_even_odd_index = -1
#     for i in range(len(lst)):
#         if lst[i] % 2 == 0 and even_odd == "even" and lst[i] <= min_even_odd:
#             min_even_odd = lst[i]
#             min_even_odd_index = i
#         elif lst[i] % 2 != 0 and even_odd == "odd" and lst[i] <= min_even_odd:
#             min_even_odd = lst[i]
#             min_even_odd_index = i
#     if min_even_odd_index == -1:
#         print("No matches")
#     else:
#         print(min_even_odd_index)

# def first_even_odd(lst, count, even_odd):
#     first_even_odd = []
#     for i in range(len(lst)):
#         if lst[i] % 2 == 0 and even_odd == "even" and len(first_even_odd) < count:
#             first_even_odd.append(lst[i])
#         elif lst[i] % 2 != 0 and even_odd == "odd" and len(first_even_odd) < count:
#             first_even_odd.append(lst[i])
#     if len(first_even_odd) == 0:
#         print("[]")
#     else:
#         print(first_even_odd)

# def last_even_odd(lst, count, even_odd):
#     last_even_odd = []
#     for i in range(len(lst) - 1, -1, -1):
#         if lst[i] % 2 == 0 and even_odd == "even" and len(last_even_odd) < count:
#             last_even_odd.append(lst[i])
#         elif lst[i] % 2 != 0 and even_odd == "odd" and len(last_even_odd) < count:
#             last_even_odd.append(lst[i])
#     if len(last_even_odd) == 0:
#         print("[]")
#     else:
#         print(last_even_odd[::-1])

# def main():
#     lst = [int(x) for x in input().split()]
#     command = input()
#     while command != "end":
#         command = command.split()
#         if command[0] == "exchange":
#             lst = exchange(lst, int(command[1]))
#         elif command[0] == "max":
#             max_even_odd(lst, command[1])
#         elif command[0] == "min":
#             min_even_odd(lst, command[1])
#         elif command[0] == "first":
#             first_even_odd(lst, int(command[1]), command[2])
#         elif command[0] == "last":
#             last_even_odd(lst, int(command[1]), command[2])
#         command = input()
#     print(lst)


# main()


# def aquire_input():
#     return [int(x) for x in input().split()]


# def exchange_list(lst, index):
#     if index < 0 or index >= len(lst):
#         print("Invalid index")
#         return lst
#     if index == 0:
#         return lst
#     # slice the list and concatenate the two parts
#     return lst[index + 1:] + lst[:index + 1]
#     # exchange first part with second part and then concatenate them
#     # lst[index + 1:], lst[:index + 1] = lst[:index + 1], lst[index + 1:]
#     # return lst


# def get_max_min(lst, even_odd):
#     max_min = None
#     max_min_index = None
#     for i in range(len(lst)):
#         # if i == 0:
#         #     max_min = 0
#         #     max_min_index = i
#         if (even_odd == "even" and lst[i] % 2 == 0) or (even_odd == "odd" and lst[i] % 2 != 0):
#             if max_min is None or lst[i] >= max_min:
#                 max_min = lst[i]
#                 max_min_index = i
#     return max_min_index


# def get_first_last(lst, count, even_odd):
#     result = []
#     for i in range(len(lst)):
#         if (even_odd == "even" and lst[i] % 2 == 0) or (even_odd == "odd" and lst[i] % 2 != 0):
#             result.append(lst[i])
#             if len(result) == count:
#                 break
#     return result


# def print_list(lst):
#     print("[" + ", ".join([str(x) for x in lst]) + "]")


# def main():
#     lst = aquire_input()
#     while True:
#         command = input()
#         if command == "end":
#             break
#         command = command.split()
#         if command[0] == "exchange":
#             lst = exchange_list(lst, int(command[1]))
#         elif command[0] == "max" or command[0] == "min":
#             max_min_index = get_max_min(lst, command[1])
#             if max_min_index is None:
#                 print("No matches")
#             else:
#                 print(max_min_index)
#         elif command[0] == "first" or command[0] == "last":
#             if int(command[1]) > len(lst):
#                 print("Invalid count")
#             else:
#                 print_list(get_first_last(lst, int(command[1]), command[2]))
#     print_list(lst)


# main()


# initial_list = [int(x) for x in input().split()]
# while True:
#     command = input().split()
#     if command[0] == "end":
#         break
#     elif command[0] == "exchange":
#         if int(command[1]) not in range(len(initial_list)):
#             print("Invalid index")
#         else:
#             initial_list = (
#                 initial_list[int(command[1]) + 1 :]
#                 + initial_list[: int(command[1]) + 1]
#             )
#     elif command[0] == "max":
#         if command[1] == "even":
#             max_even = max(
#                 [x for x in initial_list if x % 2 == 0], default="No matches"
#             )
#             if max_even == "No matches":
#                 print("No matches")
#             else:
#                 print(initial_list.index(max_even))
#         elif command[1] == "odd":
#             max_odd = max([x for x in initial_list if x % 2 != 0], default="No matches")
#             if max_odd == "No matches":
#                 print("No matches")
#             else:
#                 print(initial_list.index(max_odd))
#     elif command[0] == "min":
#         if command[1] == "even":
#             min_even = min(
#                 [x for x in initial_list if x % 2 == 0], default="No matches"
#             )
#             if min_even == "No matches":
#                 print("No matches")
#             else:
#                 print(initial_list.index(min_even))
#         elif command[1] == "odd":
#             min_odd = min([x for x in initial_list if x % 2 != 0], default="No matches")
#             if min_odd == "No matches":
#                 print("No matches")
#             else:
#                 print(initial_list.index(min_odd))
#     elif command[0] == "first":
#         if int(command[1]) > len(initial_list):
#             print("Invalid count")
#         elif command[2] == "even":
#             first_even = [x for x in initial_list if x % 2 == 0][: int(command[1])]
#             print(first_even)
#         elif command[2] == "odd":
#             first_odd = [x for x in initial_list if x % 2 != 0][: int(command[1])]
#             print(first_odd)
#     elif command[0] == "last":
#         if int(command[1]) > len(initial_list):
#             print("Invalid count")
#         elif command[2] == "even":
#             last_even = [x for x in initial_list if x % 2 == 0][-int(command[1]) :]
#             print(last_even)
#         elif command[2] == "odd":
#             last_odd = [x for x in initial_list if x % 2 != 0][-int(command[1]) :]
#             print(last_odd)

# print(initial_list)
