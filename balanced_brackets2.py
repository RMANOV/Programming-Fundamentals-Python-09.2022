

number_of_lines = int(input())
brackets = []
is_balanced = True

for i in range(number_of_lines):
    brackets.append(input())

# list comprehension to remove non-bracket characters
brackets = [i for i in brackets if i in ["(", ")"]]

# for i in brackets:
#     if len(i) % 2 == 0:
#         for j in range(0, len(i), 2):
#             if i[j] == "(" and i[j + 1] == ")":
#                 is_balanced = True
#             else:
#                 is_balanced = False
#                 break
#     else:
#         is_balanced = False

    # if brackets[i] != "(" or brackets[i] != ")":
    #     brackets.remove(brackets[i])
    # else:
    #     brackets.append(input())


# for i in brackets:
#     if i[0] == ")":
#         is_balanced = False
#         break
#     elif i[-1] == "(":
#         is_balanced = False
#         break
#     elif i.count("(") != i.count(")"):
#         is_balanced = False
#         break

if brackets.count("(") != brackets.count(")"):
    is_balanced = False

    # if i[0] == "(" and i[-1] == ")":
    #     continue
    # else:
    #     is_balanced = False
    #     break

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
