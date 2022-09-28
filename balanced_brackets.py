

number_lines = int(input())
brackets = []
left_brackets = 0
right_brackets = 0
for i in range(number_lines):
    brackets.append(input())

for i in brackets:
    if i == "(":
        left_brackets += 1
    if i == ")":
        right_brackets += 1

if left_brackets == right_brackets:
    print("BALANCED")
else:
    print("UNBALANCED")
