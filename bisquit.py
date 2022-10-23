

bisquit_per_day_per_person = int(input())
count_of_persons = int(input())
number_of_bisquits_of_the_competitor_for_30_days = int(input())

bisquits_per_day = bisquit_per_day_per_person * count_of_persons
days1 = 20
days2 = 10
bisquits_per_month = (bisquits_per_day * days1) + (bisquits_per_day * days2 * 0.75).__round__()





my_factory_vs_competitor = (bisquits_per_month / number_of_bisquits_of_the_competitor_for_30_days * 100)-100
# my_factory_vs_competitor_rounded = my_factory_vs_competitor.__round__(2)


print(f"You have produced {bisquits_per_month:.0f} biscuits for the past month.")

if my_factory_vs_competitor > 1:
    print(f"You produce {my_factory_vs_competitor:.2f} percent more biscuits.")
else:
    print(f"You produce {abs(my_factory_vs_competitor):.2f} percent less biscuits.")
