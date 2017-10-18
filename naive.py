import time
from queue import Queue

from input import read_test_cases
from utils import calculate_permutations, check_answer, tuplize


def main():
    test_cases = read_test_cases()

    for test_case in test_cases:
        start = time.time()
        answer = "This puzzle is not solvable."
        visited = set()
        queue = Queue()

        queue.put((0, test_case, ""))

        while not queue.empty():
            level, matrix, current_answer = queue.get()

            # A tuple is necessary for storing in a set since it is immutable
            matrix_tuple = tuplize(matrix)

            if matrix_tuple not in visited:
                visited.add(matrix_tuple)
            else:
                continue

            if level > 50:
                break

            if check_answer(matrix):
                answer = current_answer
                break

            permutations = calculate_permutations(matrix)

            for permutation, letter in permutations:
                permutation_tuple = tuplize(permutation)
                if permutation_tuple not in visited:
                    queue.put((level + 1,
                               permutation,
                               current_answer + letter
                               ))

        print(time.time() - start, answer)


if __name__ == "__main__":
    main()
