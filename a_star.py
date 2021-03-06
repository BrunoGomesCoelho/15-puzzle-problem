import time
from sys import argv, version_info
from queue import PriorityQueue

from input import read_test_cases, MATRIX_SIZE
from utils import calculate_permutations, check_answer, has_answer, tuplize, REQ_VERSION


def calculate_heuristic(matrix):
    """We use the Manhattan Distance between the given piece and where it should be on the bord
    It is a admissible heuristic.
    """
    cost = 0
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            num = matrix[i][j]
            if num != i*MATRIX_SIZE + (j+1) and num != 0:
                correct_row = (num - 1) // MATRIX_SIZE
                correct_col = (num - 1) % MATRIX_SIZE
                cost += abs(i - correct_row) + abs(j - correct_col)
    return cost


def main():

    if version_info < REQ_VERSION:
        print("Python version too low! Please use", REQ_VERSION, "or later.")

    test_cases = read_test_cases()

    for test_case in test_cases:
        start = time.time()
        answer = "This puzzle is not solvable."
        queue = PriorityQueue()
        visited = set()

        if len(argv) < 2 or argv[2].strip().to_lower() != "no_check=true":
            if not has_answer(test_case):
                print(time.time() - start, answer)
                continue

        """
        The queue follows the order
            total cost, level, matrix, answer
        for all elements """
        queue.put((0, 0, test_case, ""))

        while not queue.empty():
            _, level, matrix, current_answer = queue.get()

            if level > 50:
                break

            if check_answer(matrix):
                answer = current_answer
                break

            permutations = calculate_permutations(matrix)

            for permutation, letter in permutations:
                # A tuple is necessary for storing in a set since it is immutable
                permutation_tuple = tuplize(permutation)
                if permutation_tuple not in visited:
                    heuristic_cost = calculate_heuristic(permutation)
                    visited.add(permutation_tuple)
                    queue.put((heuristic_cost+level+1,
                               level+1,
                               permutation,
                               current_answer + letter
                               ))

        print(time.time() - start, answer)


if __name__ == "__main__":
    main()
