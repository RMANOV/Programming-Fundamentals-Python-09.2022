

# In the Tribonacci sequence, every number is formed by the sum of the previous 3.
# Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space, starting from 1. 
# You will receive a positive integer number as input.

def tribonacci_sequence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return tribonacci_sequence(n - 1) + tribonacci_sequence(n - 2) + tribonacci_sequence(n - 3)

def main():
    n = int(input())
    for i in range(1, n + 1):
        print(tribonacci_sequence(i), end=" ")

main()