class Matrix:
    def __init__(self, a: int, b: int, matrix: list[list]) -> None:
        self.a = a
        self.b = b
        self.matrix = matrix # self.check_matrix(matrix)
        
    def check_matrix(self, matrix):
        if len(matrix[0]) == self.b and len(matrix) == self.a:
            return matrix
        raise AttributeError("Не верный формат матрицы")
    
    def display_matrix(self) -> str:
        for i in self.matrix:
            print(i)
            
    def __add__(self, other):
        if isinstance(other, Matrix) and (self.a == other.a and self.b == other.b):
            result_matrix = []
            for i in range(len(self.matrix)):
                time_matrix = []
                for j in range(len(self.matrix[0])):
                    time_matrix.append(self.matrix[i][j] + other.matrix[i][j])
                result_matrix.append(time_matrix)
            return Matrix(self.a, self.b, result_matrix)
        else:
            raise AttributeError("Не возможно выполнить сложение, разная размерность матриц")
        
    def __sub__(self, other):
        if isinstance(other, Matrix) and (self.a == other.a and self.b == other.b):
            result_matrix = []
            for i in range(len(self.matrix)):
                time_matrix = []
                for j in range(len(self.matrix[0])):
                    time_matrix.append(self.matrix[i][j] - other.matrix[i][j])
                result_matrix.append(time_matrix)
            return Matrix(self.a, self.b, result_matrix)
        else:
            raise AttributeError("Не возможно выполнить вычитание, разная размерность матриц")
        
    def __mul__(self, other):
        if isinstance(other, Matrix) and (self.b == other.a):
            result_matrix = [[0 for i in range(self.a)] for j in range(other.b)]
            for i in range(self.a):
                for j in range(other.b):
                    for k in range(self.b):
                        result_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(self.a, other.a, result_matrix)
        else:
            raise AttributeError("Не возможно выполнить сложение, разная размерность матриц")
        
    def transpose(self):
        new_matrix = []
        for i in range(len(self.matrix[0])):
            time_list = []
            for j in range(len(self.matrix)):
                time_list.append(self.matrix[j][i])
            new_matrix.append(time_list)
        return Matrix(self.b, self.a, new_matrix)
        
    def __repr__(self) -> str:
        return f"Matrix({self.a}, {self.b}, {self.matrix})"
    
    def __str__(self):
        res = '\n'.join([' '.join(map(str, a)) for a in self.matrix])
        return res
    
    
if __name__ == "__main__":
    matrix = Matrix(2, 3, [[1, 2, 3,], [4, 5, 6]])
    matrix.display_matrix()
    # matrix_3 = Matrix(2, 3, [[1, 2, 3,], [4, 5, 6]])
    # matrix_2 = Matrix(3, 3, [[1, 2, 3,], [4, 5, 6], [7, 8, 9]])
    # matrix.display_matrix()
    # matrix_2.display_matrix()
    # matrix_4 = matrix - matrix_3
    # print(matrix_4)
    # matrix_4.display_matrix()
    # matrix_5 = matrix + matrix_2
    matrix_6 = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
    matrix_6.display_matrix()
    print(matrix * matrix_6)
    
    print(matrix.transpose())
    
    
    