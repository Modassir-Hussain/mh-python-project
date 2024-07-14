import pytest

from src.main import my_func_add


@pytest.mark.parametrize("input_1, input_2, output", [(1, 2, 3), (1, 3, 4)])
def test_main_my_func(
    input_1,
    input_2,
    output,
):
    assert output == my_func_add(input_1, input_2)
    assert output == my_func_add(input_1, input_2)
