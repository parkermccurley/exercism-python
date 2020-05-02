class School:
    def __init__(self):
        self.students = {}
        for i in range(0, 8):
            self.students[i] = []

    def add_student(self, name, grade):
        self.students[grade].append(name)
        self.students[grade].sort()

    def roster(self):
        students = []
        for grade in self.students.values():
            for student in grade:
                students.append(student)
        return students

    def grade(self, grade_number):
        return self.students[grade_number]
