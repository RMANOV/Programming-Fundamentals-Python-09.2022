

bisquit_per_day_per_person = int(input())
count_of_persons = int(input())
number_of_bisquits_of_the_competitor_for_30_days = int(input())

bisquits_per_day = bisquit_per_day_per_person * count_of_persons
days = 0
bisquits_per_month = 0

while True:
    days += 1
    if days % 3 == 0:
        bisquits_per_day -= bisquits_per_day * 0.75
    
    if days == 30:
        break

print(f"You have produced {bisquits_per_day} biscuits for the past month.")

    
