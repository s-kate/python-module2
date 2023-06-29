class Student:
    total_students = 0

    def __init__(self, name):
        self.name = name
        Student.total_students += 1

    @classmethod
    def total_students_count(cls):
        return cls.total_students


student1 = Student('Alice')
student2 = Student('Josh')
student3 = Student('Beth')

print(f'Total students: {Student.total_students}')
