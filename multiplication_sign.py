

# You will receive three integer numbers. 
# Write a program that finds if their multiplication (the result) is negative, positive, or zero. 
# Try to do this WITHOUT multiplying the 3 numbers.

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    if a == 0 or b == 0 or c == 0:
        print("zero")
    elif (a > 0 and b > 0 and c > 0) or (a < 0 and b < 0 and c > 0) or (a < 0 and b > 0 and c < 0) or (a > 0 and b < 0 and c < 0):
        print("positive")
    else:
        print("negative")

main()