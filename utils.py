from input import MATRIX_SIZE


def calculate_permutations(matrix):
    options = [(-1, 0, "L"), (1, 0, "R"), (0, -1, "U"), (0, 1, "D")]
    permutations = []
    row = col = -1
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            if matrix[i][j] == 0:
                row = i
                col = j

    for i, j, letter in options:
        if 0 <= row + i < MATRIX_SIZE and 0 <= col + j < MATRIX_SIZE:
            temp = matrix
            temp[row][col], temp[i][j] = temp[i][j], temp[row][col]
            permutations.append((temp, letter))

    return permutations


def check_answer(matrix):
    answer = True
    for i in range(MATRIX_SIZE):
        for j in range(1, MATRIX_SIZE + 1):
            if matrix[i][j-1] != i*MATRIX_SIZE + j and i != MATRIX_SIZE - 1 and j != MATRIX_SIZE:
                answer = False
    return answer
