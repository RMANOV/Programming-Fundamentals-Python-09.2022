

employe_happiness = [int(x) for x in input().split()]
factor = int(input())

employe_happiness = [x * factor for x in employe_happiness]
average_happiness = sum(employe_happiness) / len(employe_happiness)
happy_employees = [x for x in employe_happiness if x >= average_happiness]

if len(happy_employees) >= len(employe_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(employe_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employe_happiness)}. Employees are not happy!")
