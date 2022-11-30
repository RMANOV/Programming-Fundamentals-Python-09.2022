

# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
# Legend:
# •	0 - empty space
# •	1 - first player move
# •	2 - second player move
# Find out who the winner is. If the first player wins, print "First player won". 
# If the second player wins, print "Second player won". 
# Otherwise, print "Draw!".

first_line = input().split()
second_line = input().split()
third_line = input().split()

field = [first_line, second_line, third_line]
for row in field:
    if row[0] == row[1] == row[2] == '1' or row[2] == row[1] == row[0] == '1':
        exit()
    elif row[0] == row[1] == row[2] == '2' or row[2] == row[1] == row[0] == '2':
        print('Second player won')
        exit()
    else:
        print('Draw!')
