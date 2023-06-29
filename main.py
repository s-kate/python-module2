# class Student

class Student:

    def __init__(self, name: str, surname: str, grades: list):
        self.name = name
        self.surname = surname
        self.grades = grades

    def __len__(self):
        return len(self.grades)


students_list = [
    Student('Joseph', 'Filip', [10, 9, 8, 10, 12, 2, 5, 6, 7]),
    Student('Elizabeth', 'Filip', [12, 4, 10, 11]),
    Student('Rich', 'Pumpum', [7, 6, 5, 2, 6, 6, 7]),
    Student('Beth', 'Riucert', [10, 12, 8, 9, 10, 11, 5, 6])
]

sorted_students = sorted(students_list, key=lambda s: len(s))

for student in sorted_students:
    print(f'{student.surname, student.name} - number of grades: {len(student)}')