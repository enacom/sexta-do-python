import pytest
import numpy as np


# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected


# numbers = np.random.randint(1, 10, int(1e4))
numbers = np.random.randint(1, 10, 10)
result = (numbers % 2) != 0  # True -> odd/ False -> even
result[-1] = not result[-1]
args_in = [(numbers[i], result[i]) for i in range(len(result))]


@pytest.mark.parametrize("input_number, output", args_in)
def test_odd_even_numbers(input_number, output):
    assert input_number % 2 == output


# pytest test_parametrize.py
# pytest -n 2 test_parametrize.py -vv


if __name__ == '__main__':
    pytest.main()
