

initial_string = input().split()
palindrome = input()
initial_list = [initial_list for initial_list in initial_string]
palindrome_list = []

initial_list =[palindrome_list[i] for i in initial_list if palindrome_list[i] == palindrome_list[i][::-1]]
print(palindrome_list.count())


print(initial_list)
