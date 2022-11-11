

initial_list = input().split()
result = ''

for word in initial_list:
    result += word * len(word)
print(result)

# Path: repeat_strings.py