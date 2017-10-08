MATRIX_ROW = 4


def read_matrix():
    matrix = []

    for _ in range(MATRIX_ROW):
        matrix.append([int(x) for x in input().split()])

    return matrix


def read_test_cases():
    n = int(input())
    test_cases = []

    for _ in range(n):
        test_cases.append(read_matrix())

    return test_cases
