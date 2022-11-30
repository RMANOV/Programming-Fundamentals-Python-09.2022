

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

number_of_skips = int(input())
result = []

while initial_list:
    # index = (number_of_skips - 1) % len(initial_list)
    # index = number_of_skips % len(initial_list)
    index = number_of_skips
    result.append(initial_list.pop(index))
    index += number_of_skips
    if index >= len(initial_list):
        index = index % len(initial_list)


print(f"[{','.join(result)}]")


# for i in range(0,len(initial_list),number_of_skips):
#     # index = (number_of_skips-1)%len(initial_list)
#     # result.append(initial_list.pop(number_of_skips-1))
#     # result.append(initial_list.pop(index))
#     if i > len(initial_list):
#         i=0
#     result.append(initial_list.pop(i))


# def josephus_permutation(items, k):
#     #your code here
#     if len(items) == 0:
#         return []
#     else:
#         k = k - 1
#         idx = k % len(items)
#         return [items[idx]] + josephus_permutation(items[:idx] + items[idx+1:], k+1)

# def print_josephus_permutation(items, k):
#     print(josephus_permutation(items, k))

# def main():
#     print_josephus_permutation([1,2,3,4,5,6,7],3)
#     print_josephus_permutation([1,2,3,4,5,6,7],4)
#     print_josephus_permutation([],3)
#     print_josephus_permutation([1,2,3,4,5,6,7],-1)
#     print_josephus_permutation([1,2,3,4,5,6,7],0)
#     print_josephus_permutation([1,2,3,4,5,6,7],1)
#     print_josephus_permutation([1,2,3,4,5,6,7],2)
#     print_josephus_permutation([1,2,3,4,5,6,7],8)
#     print_josephus_permutation([1,2,3,4,5,6,7],9)
#     print_josephus_permutation([1,2,3,4,5,6,7],10)

# main()

# initial_list = input().split()
# step = int(input())
# result = []
# deleted_indexs = []

# for i in range(len(initial_list)):
#     initial_list[i] = int(initial_list[i])

# for i in range(len(initial_list)):
#     deleted_indexs.append((i + step - 1) % len(initial_list))

# for i in range(len(initial_list)):
#     result.append(initial_list[deleted_indexs[i]])

# print(deleted_indexs)
