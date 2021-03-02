from matrix import Matrix
from solve import solve
import sys


def create_filled_matrix(size: int, get_line) -> Matrix:
    A = []
    b = []
    for line in range(0, size):
        equation = list(map(float, get_line().split()))
        b.append(equation.pop())
        A.append(equation)
    return Matrix(size, A, b)


def validate_size(size: int):
    if not 0 < size <= 20:
        print('Matrix size must be in the range [1, 20].')
        exit(-1)
    return size


if len(sys.argv) < 2:
    precision = input('Precision: ')
    size = validate_size(int(input('Matrix size: ')))
    print('Matrix coefficients: ')
    matrix = create_filled_matrix(size, input)
else:
    try:
        f = open(sys.argv[1], "r")
        precision = f.readline()
        size = validate_size(int(f.readline()))
        matrix = create_filled_matrix(size, f.readline)
        f.close()
    except FileNotFoundError:
        print('File not found.')
        exit(-1)

print('Source matrix:')
print(matrix)

solution = solve(matrix, precision)

if solution:
    print('\nSolution:')
    print(solution)

