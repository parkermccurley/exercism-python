import math

class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split('\n')

        for i in range(len(self.matrix)):
            self.matrix[i] = self.matrix[i].split()
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = int(self.matrix[i][j])

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [int(row[index - 1]) for row in self.matrix]
