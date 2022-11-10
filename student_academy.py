

number_of_commands = int(input())
students = {}
student_name = 0
student_grade = 0


for i in range(number_of_commands):
    command = input()
    if i % 2 == 0:
        student_name = command
        if student_name not in students:
            students[student_name] = []
        else:
            command = input()
            student_grade = float(command)
            students[student_name].append(student_grade)
    else:
        if float(command.isdigit()):
            student_grade = float(command)
            students[student_name].append(student_grade)
        else:
            student_name = command
            student_grade = float(command)
            students[student_name].append(student_grade)

for student, grades in students.items():
    if len(grades) > 1:
        average_grade = sum(grades) / len(grades)
        if average_grade >= 4.50:
            print(f'{student} -> {average_grade:.2f}')


# Path: student_academy.py
















# for i in range(pair_comand):
#     name, grade = input().split()
#     if name not in students:
#         students[name] = []
#     students[name].append(float(grade))
    
# for name, grades in students.items():
#     avg_grade = sum(grades) / len(grades)
#     if avg_grade < 4.50:
#         students.pop(name)
#     print(f'{name} -> {avg_grade:.2f}')
#     # print(f'{name} -> {" ".join(f"{grade:.2f}" for grade in grades)} (avg: {avg_grade:.2f})')