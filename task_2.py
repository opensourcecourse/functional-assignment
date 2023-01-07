"""A task for creating a logging decorator."""
import inspect


def bind_args_kwargs(func, output, *args, **kwargs):
    """Return a string for printing logging."""
    sig = inspect.signature(func)
    bound = sig.bind(*args, **kwargs)
    bound.apply_defaults()
    args = [f"{i}={v}" for i, v in bound.arguments.items()]
    out = f"{func.__name__}({', '.join(args)}) -> {output}"
    return out


def print_input_output(func):
    """
    A decorator to print function inputs and outputs.

    Examples
    --------
    >>> @print_input_output
    ... def my_func(param_1, param_2)
    ...     return param_1 + param_2
    >>> my_func(1, param_2=2)
    >>> # prints "my_func(param_1=1, param_2=2) -> 3"
    """

    # hints: use bind_args_kwargs to format print string.
    # also https://realpython.com/python-kwargs-and-args/ if you are new to
    # *args and **kwargs


if __name__ == "__main__":
    # tests for bind_args_kwargs
    def test_func(a, b=2):
        """A test function for bing_args_kwargs."""
        return a + b

    expected = "test_func(a=1, b=2) -> 3"
    assert bind_args_kwargs(test_func, 3, a=1) == expected
    assert bind_args_kwargs(test_func, 3, a=1, b=2) == expected
    expected_2 = "test_func(a=3, b=3) -> 6"
    assert bind_args_kwargs(test_func, 6, a=3, b=3) == expected_2
