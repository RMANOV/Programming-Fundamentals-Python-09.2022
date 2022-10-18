

initial_string = input().split()
palindrome = input()
palindrome_list = []
for i in initial_string:

    if i == palindrome:
        palindrome_list.append(i)

    if not i == i[::-1]:
        initial_string.remove(i)

   

print(initial_string)
palindrome_count = palindrome_list.count(palindrome)
print(f"Found palindrome {palindrome_count} times")