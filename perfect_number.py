

def perfekt_number(number):
    """Return True if number is a perfect number, False otherwise."""
    return sum([i for i in range(1, number) if number % i == 0]) == number


positive_int = int(input())

if perfekt_number(positive_int):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")