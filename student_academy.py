

pair_comand = int(input())
students = {}

for i in range(pair_comand):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))
    
for name, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade < 4.50:
        students.pop(name)
    print(f'{name} -> {avg_grade:.2f}')
    # print(f'{name} -> {" ".join(f"{grade:.2f}" for grade in grades)} (avg: {avg_grade:.2f})')