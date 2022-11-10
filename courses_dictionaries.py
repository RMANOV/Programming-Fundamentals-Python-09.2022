

courses = {}
command = input().split(" : ")

while not command[0] == "end":
    course = command[0]
    student = command[1]
    if course not in courses:
        courses[course] = []
    courses[course].append(student)
    command = input().split(" : ")
    
for course, students in sorted(courses.items(), key=lambda x: -len(x[1])):
    print(f"{course}: {len(students)}")
    for student in sorted(students):
        print(f"-- {student}")

