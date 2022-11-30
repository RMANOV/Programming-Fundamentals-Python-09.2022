

# You are now to create a program that prints a Josephus permutation, receiving two lines of code:
# •	the list itself - numbers separated by a single space representing the people in the circle
# •	a number k
# People are standing in a circle waiting to be executed. 
# Counting begins from the first one in the circle and proceeds from left to right. 
# After a specified number of people are skipped, the k person is executed. 
# The procedure is repeated with the remaining people, starting with the next person, going in the same direction, 
# and skipping the same number of people until no one remains.
# Print the people by order of executions in the format: "[{executed1},{executed2}, … {executedN}]"

initial_list = input().split()
step = int(input())
result = []
deleted_indexs = []

for i in range(len(initial_list)):
    initial_list[i] = int(initial_list[i])

for i in range(len(initial_list)):
    deleted_indexs.append((i + step - 1) % len(initial_list))

for i in range(len(initial_list)):
    result.append(initial_list[deleted_indexs[i]])

print(deleted_indexs)
