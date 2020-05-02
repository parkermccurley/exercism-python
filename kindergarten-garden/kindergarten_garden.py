import textwrap

class Garden:
    def __init__(self, diagram, students=[
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Fred",
            "Ginny",
            "Harriet",
            "Ilean",
            "Joseph",
            "Kincaid",
            "Larry"]):
        self.plant_names = {
            'g': 'Grass',
            'c': 'Clover',
            'r': 'Radishes',
            'v': 'Violets'
        }
        self.diagram = diagram
        self.students = students
        self.students.sort()


    def plants(self, student):
        student_row = self.students.index(student)
        garden = self.diagram.split('\n')
        row = ''
        for i in range(len(garden)):
            garden[i] = textwrap.wrap(garden[i], 2)
            row += garden[i][student_row].lower()

        return [self.plant_names[plant] for plant in row]
