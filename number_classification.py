

initial_list_of_numbers = [int(x) for x in input().split(", ")]
positives = [number for number in initial_list_of_numbers if number >= 0]
negatives = [number for number in initial_list_of_numbers if number < 0]
evens = [number for number in initial_list_of_numbers if number % 2 == 0]
odds = [number for number in initial_list_of_numbers if number % 2 != 0]

print(f"Positive: {', '.join([str(number) for number in positives])}")
print(f"Negative: {', '.join([str(number) for number in negatives])}")
print(f"Even: {', '.join([str(number) for number in evens])}")
print(f"Odd: {', '.join([str(number) for number in odds])}")

