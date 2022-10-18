

initial_string = input().split()
palindrome = input()
palindrome_list = []


palindrome_list = [x for x in initial_string if x == palindrome]



    
filtered_list = [i for i in initial_string if i == i[::-1]]
    



print(filtered_list)
palindrome_count = palindrome_list.count(palindrome)
print(f"Found palindrome {palindrome_count} times")