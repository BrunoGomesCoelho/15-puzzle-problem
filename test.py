from utils import check_answer


class TestInput(object):
    """
    A basic test class
    """

    def test_check_answer_true(self):
        ans = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        assert check_answer(ans)

    def test_check_answer_false(self):
        not_ans = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]
        assert not check_answer(not_ans)
