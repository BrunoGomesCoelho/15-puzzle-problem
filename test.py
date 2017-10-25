import mock
import utils

from input import read_matrix, read_test_cases


class TestInput(object):

    @classmethod
    def setup_class(cls):
        cls.array = ['1 2 3 4\n\r', '5 6 7 8\n\r', "9 10 11 12 \n\n", "13 14 15 0\n"]

    def test_read_matrix(self):
        with mock.patch('builtins.input', side_effect=self.array):
            output = read_matrix()
            expected = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
            assert output == expected

    def test_read_test_cases(self):
        with mock.patch('builtins.input', side_effect=["1\n"] + self.array):
            output = read_test_cases()
            expected = [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]]
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
