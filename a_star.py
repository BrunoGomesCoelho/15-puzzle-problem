import time
from queue import PriorityQueue

from input import read_test_cases, MATRIX_SIZE
from utils import calculate_permutations, check_answer


def calculate_heuristic(matrix):
    cost = 0
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            num = matrix[i][j]
            if num != i*MATRIX_SIZE + (j+1) and num != 0:
                correct_row = (num - 1) / MATRIX_SIZE
                correct_col = (num - 1) % MATRIX_SIZE
                cost += abs(i - correct_row) + abs(j - correct_col)
    return cost


def main():
    test_cases = read_test_cases()

    for test_case in test_cases:
        start = time.time()
        count = -1
        answer = "This puzzle is not solvable."
        queue = PriorityQueue()
        visited = []
        found = False

        queue.put((0, test_case, ""))

        while not queue.empty() and not found:
            if count > 50:
                break

            count += 1
            cost, matrix, current_answer = queue.get()

            if check_answer(matrix):
                answer = current_answer
                break

            permutations = calculate_permutations(matrix)

            for permutation, letter in permutations:
                if permutation not in visited:
                    heuristic_cost = calculate_heuristic(permutation)
                    visited.append(permutation)
                    queue.put((heuristic_cost+cost,
                               permutation,
                               current_answer + letter
                               ))

        print(time.time() - start, answer)


if __name__ == "__main__":
    main()
