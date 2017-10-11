from input import MATRIX_SIZE
from copy import deepcopy


def calculate_permutations(matrix):
    options = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]
    permutations = []
    row = col = -1
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            if matrix[i][j] == 0:
                row = i
                col = j

    for i, j, letter in options:
        if 0 <= row + i < MATRIX_SIZE and 0 <= col + j < MATRIX_SIZE:
            temp = deepcopy(matrix)  # creates a copy of the matrix so we dont change it
            temp[row][col], temp[row+i][col+j] = temp[row+i][col+j], temp[row][col]
            permutations.append((temp, letter))

    return permutations


def check_answer(matrix):
    answer = True
    for i in range(MATRIX_SIZE):
        for j in range(1, MATRIX_SIZE + 1):
            if matrix[i][j-1] != i*MATRIX_SIZE + j and (i != MATRIX_SIZE - 1 or j != MATRIX_SIZE):
                answer = False
    return answer
