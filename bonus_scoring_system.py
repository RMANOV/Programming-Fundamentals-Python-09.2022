

number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
count_of_attendances_for_each_student = []

for i in range(number_of_students):
    count_of_attendances_for_each_student.append(int(input()))

max_bonus = 0
max_bonus_attendances = 0

for attendances in count_of_attendances_for_each_student:
    bonus = attendances / total_number_of_lectures * (5 + additional_bonus)
    if bonus > max_bonus:
        max_bonus = bonus
        max_bonus_attendances = attendances

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_bonus_attendances} lectures.")

# Path: bonus_scoring_system.py