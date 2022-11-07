

students_names_and_ids = {}
students_names_and_course = {}
searched_course = 0

command = input().split(":")

while len(command) > 1:
    student_name = command[0]
    student_id = command[1]
    students_course = command[2]
    
    students_names_and_ids[student_name] = student_id
    students_names_and_course[student_name] = students_course
    
    command = input().split(":")

searched_course = input()

for key, value in students_names_and_course.items():
    if searched_course[1] in value:
        print(f"{key} - {students_names_and_ids[key]}")
        
# print(students_names_and_ids)






    
# if len(students_data) == 3:
#     for student in students_data:
#         students_names_and_ids[student[0]] = student[1]
#         students_names_and_course[student[0]] = student[2]
# else:
#     searched_course = input().split("_")[1]
    
#     for student in students_data:
#         if student[2] == searched_course:
#             print(f"{student[0]} - {student[1]}")
            
#     exit()



        
        
        
#     for student in students:
#         print(f"{student} -> {', '.join(students[student])}")
# else:
#     searched_student = students_data[0]
#     searched_course = students_data[1].split("_")
#     searched_course.pop()
    
#     if searched_student not in students:
#         students[searched_student] = []
#     students[searched_student].extend(searched_course)
    
#     for student in students:
#         print(f"{student} -> {', '.join(students[student])}")
        


    
