import time
from queue import Queue

from input import read_test_cases, MATRIX_SIZE
from utils import calculate_permutations, check_answer


def main():
    test_cases = read_test_cases()

    for test_case in test_cases:
        start = time.time()
        count = -1
        answer = "This puzzle is not solvable."
        visited = set()
        queue = Queue()

        queue.put((0, test_case, ""))

        while not queue.empty():
            level, matrix, current_answer = queue.get()

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
                    queue.put((heuristic_cost + level + 1,
                               level + 1,
                               permutation,
                               current_answer + letter
                               ))

                    # print(time.time() - start, answer)
    print(answer)


if __name__ == "__main__":
    main()
