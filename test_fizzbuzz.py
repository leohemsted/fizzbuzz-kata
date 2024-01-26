import pytest

from fizzbuzz import fizzbuzz_a_num


@pytest.mark.parametrize(
    "input, expected",
    [
        (1, 1),
        (2, 2),
        (3, "fizz"),
    ],
)
def test_fizzbuzz(input, expected):
    assert fizzbuzz_a_num(input) == expected
