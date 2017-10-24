import mock
import utils

from input import read_matrix


class TestInput(object):
    def test_read_matrix(self):
        with mock.patch('builtins.input', side_effect=['1 2 3 4\n', '5 6 7 8\n', "9 10 11 12 \n", "13 14 15 0\n"]):
            output = read_matrix()
            expected = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
            assert output == expected


class TestUtils(object):
    def test_check_answer_true(self):
        ans = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        assert utils.check_answer(ans)

    def test_check_answer_false(self):
        not_ans = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]
        assert not utils.check_answer(not_ans)

    def test_calculate_permutations(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 14, 15, 11]]
        permutations = [
            ([[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 7, 12], [13, 14, 15, 11]], "U"),
            ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 15, 12], [13, 14, 0, 11]], "D"),
            ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 10, 12], [13, 14, 15, 11]], "L"),
            ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 12, 0], [13, 14, 15, 11]], "R")
        ]
        assert utils.calculate_permutations(matrix) == permutations
