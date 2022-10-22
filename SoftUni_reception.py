

first_employee_efficiency_per_hour = int(input())
second_employee_efficiency_per_hour = int(input())
third_employee_efficiency_per_hour = int(input())

number_of_students = int(input())


total_efficiency_per_hour = first_employee_efficiency_per_hour + second_employee_efficiency_per_hour + third_employee_efficiency_per_hour
total_hours = 0

while number_of_students > 0:
    total_hours += 1
    if total_hours % 4 == 0:
        continue
    number_of_students -= total_efficiency_per_hour

print(f"Time needed: {total_hours}h.")