class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list



    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


matrix1 = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
matrix2 = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
print("Даны две матрицы. Матрица №1:  ")
print(matrix1)
print("Матрица №2: ")
print(matrix2)
print("Сумма матриц равна: ")
print(matrix1.__add__(matrix2))