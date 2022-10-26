

number_of_lines = int(input())
brackets = []
is_balanced = True

for i in range(number_of_lines):
    brackets.append(input())

# list comprehension to remove non-bracket characters
brackets = [i for i in brackets if i in ["(", ")"]]

if brackets.count("(") != brackets.count(")"):
    is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
