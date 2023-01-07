"""Tests for the second functional task."""
from task_2 import print_input_output


@print_input_output
def my_func(arg1, arg2=2, *, keyword_only=True):
    """A test function."""
    return arg1 + arg2


def test_prints_inputs_outputs(capsys):
    """Ensure expected string is printed."""
    expected_1 = "my_func(arg1=1, arg2=4, keyword_only=True) -> 5"
    my_func(1, 4)
    out = capsys.readouterr()
    assert expected_1 in str(out)
