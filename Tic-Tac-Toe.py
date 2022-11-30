

# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
# Legend:
# •	0 - empty space
# •	1 - first player move
# •	2 - second player move
# Find out who the winner is. If the first player wins, print "First player won". 
# If the second player wins, print "Second player won". 
# Otherwise, print "Draw!".

# def main():
#     field = []
#     for _ in range(3):
#         field.append(input().split())
#     for row in range(3):
#         if field[row][0] == field[row][1] == field[row][2] == '1':
#             print('First player won')
#             return
#         if field[row][0] == field[row][1] == field[row][2] == '2':
#             print('Second player won')
#             return
#     for col in range(3):
#         if field[0][col] == field[1][col] == field[2][col] == '1':
#             print('First player won')
#             return
#         if field[0][col] == field[1][col] == field[2][col] == '2':
#             print('Second player won')
#             return
#     if field[0][0] == field[1][1] == field[2][2] == '1':
#         print('First player won')
#         return
#     if field[0][0] == field[1][1] == field[2][2] == '2':
#         print('Second player won')
#         return
#     if field[0][2] == field[1][1] == field[2][0] == '1':
#         print('First player won')
#         return
#     if field[0][2] == field[1][1] == field[2][0] == '2':
#         print('Second player won')
#         return
#     print('Draw!')


# first_line = input().split()
# second_line = input().split()
# third_line = input().split()

# field = [first_line, second_line, third_line]
# for row in field:
#     if row[0] == row[1] == row[2] == '1' or row[2] == row[1] == row[0] == '1':
#         exit()
#     elif row[0] == row[1] == row[2] == '2' or row[2] == row[1] == row[0] == '2':
#         print('Second player won')
#         exit()
#     else:
#         print('Draw!')
