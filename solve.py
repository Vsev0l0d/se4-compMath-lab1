from matrix import Matrix


class Solution:
    def __init__(self, x_vector, iterations, error_vector, digits_after_dot=None):
        self.digits_after_dot = digits_after_dot
        self.error_vector = error_vector
        self.iterations = iterations
        self.x_vector = x_vector

    def __str__(self):
        result = '  Vector of unknowns: '
        if self.digits_after_dot:
            formatted_vector = list(map(lambda x: round(x, self.digits_after_dot), self.x_vector))
            result += f'{formatted_vector}\n'
        else:
            result += f'{self.x_vector}\n'

        result += f'  Number of iterations: {self.iterations}\n'
        result += f'  Error vector: {self.error_vector}\n'
        return result


def solve(matrix: Matrix, precision: str):
    digits_after_dot = len(precision.split('.')[1].rstrip('0'))
    precision = float(precision)
    x_vector = [0] * matrix.size

    if not matrix.diagonally_dominant:
        print('Matrix has no diagonal dominance, attempted permutation ...')
        if not matrix.make_diagonally_dominant():
            print('Failed to achieve diagonal dominance: Calculation completed.')
            return None
        else:
            print('New matrix: ')
            print(matrix)

    c_matrix = []
    for row in range(matrix.size):
        a_ii = matrix.coefficients[row][row]
        row_vector = []
        for column in range(matrix.size):
            c = -matrix.coefficients[row][column] / a_ii if row != column else 0
            row_vector.append(c)
        c_matrix.append(row_vector)

    iterations = 0
    error_vector = [1] * len(x_vector)
    while max(error_vector) > precision:
        iterations += 1
        for i in range(len(x_vector)):
            a = matrix.coefficients[i][i]
            b = matrix.b[i]
            cx_array_sum = 0
            for j in range(len(x_vector)):
                cx_array_sum += c_matrix[i][j] * x_vector[j]

            prev = x_vector[i]
            x_vector[i] = cx_array_sum + b / a
            error_vector[i] = abs(x_vector[i] - prev)

    return Solution(x_vector, iterations, error_vector, digits_after_dot)
