def find_dominant_index(coefficients: []) -> (int, bool):
    for i in range(len(coefficients)):
        coefficient_abs_sum = sum(list(map(abs, coefficients)))
        diff = 2 * abs(coefficients[i]) - coefficient_abs_sum
        if diff >= 0:
            return i, diff != 0
    return None, False


class Matrix:
    def __init__(self, size: int, A: [], b=None):
        self.coefficients = A
        self.size = size
        self.b = b

    def __str__(self):
        result = []
        for i in range(self.size):
            left = ''
            for j in range(self.size):
                left += f'{self.coefficients[i][j]:7.2f}'
            right = '  |' + f"{self.b[i]:7.2f}" if self.b is not None else ''
            result.append(left + right)
        return '\n'.join(result)

    @property
    def diagonally_dominant(self) -> bool:
        at_least_one_strict = False
        for row_number in range(self.size):
            (dominant_index, strict) = find_dominant_index(self.coefficients[row_number])
            if dominant_index != row_number:
                return False
            if strict:
                at_least_one_strict = True
        return at_least_one_strict

    def make_diagonally_dominant(self) -> bool:
        new_A = [None] * self.size
        new_b = [0] * self.size
        for row_number in range(self.size):
            (dominant_index, _) = find_dominant_index(self.coefficients[row_number])
            if (dominant_index is not None) and (new_A[dominant_index] is None):
                new_A[dominant_index], new_b[dominant_index] = self.coefficients[row_number], self.b[row_number]
            else:
                return False
        self.coefficients, self.b = new_A, new_b
        return True