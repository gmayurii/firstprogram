import pytest


class Test_002:

    @pytest.mark.group1
    @pytest.mark.skip
    def test_sum_004(self):
        a = 3
        b = 4
        sum = a + b
        if sum == 7:
            assert True
        else:
            assert False

# pytest -v
# pytest -m (markername) --> to run specific group's test cases

