import pytest
from swap import swap_without_temp

@pytest.mark.parametrize("a, b, expected_a, expected_b", [
    (5, 10, 10, 5),
    (0, 0, 0, 0),
    (-1, 1, 1, -1),
    (123, 456, 456, 123),
    (-5, -10, -10, -5),
])
def test_swap_without_temp(a, b, expected_a, expected_b):
    result_a, result_b = swap_without_temp(a, b)
    assert result_a == expected_a
    assert result_b == expected_b
