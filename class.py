

class Class:
    __students_count = 22
    students = []
    grades = []

    def __init__(self, name):
        self.name = name

    def add_student(self, name: str, grade: float):
        self.students.append(name)
        self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        # result = f'Class name: {self.name}'

        for i in range(len(self.students)):
            result += f'{self.students[i]} - {self.grades[i]}'

        result += f'The students in {self.name}: {self.students}. Average grade: {self.get_average_grade():.2f}'
        return result




    