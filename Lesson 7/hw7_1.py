from itertools import zip_longest

class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n '.join((['\t '.join([str(i) for i in j]) for j in self.matrix])))

    def __add__(self, other):
        return Matrix([map(sum, zip_longest(*t, fillvalue=0))
                      for t in zip_longest(self.matrix, other.matrix, fillvalue=[])])

mat_1 = [[31, 22], [37, 43], [51, 86]]
mat_2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]

matr_1 = Matrix(mat_1)
matr_2 = Matrix(mat_2)

#print(matr_1)
print(matr_1+matr_2)
