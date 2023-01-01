"""
Tests for function registration.
"""

from task_1 import register, REGISTERED_FUNCTIONS


def test_function_registered():
    """Ensure the function shows up in the list."""

    name = '_test_func'

    @register(name)
    def ok_function():
        ...

    assert name in REGISTERED_FUNCTIONS
    assert REGISTERED_FUNCTIONS[name] is ok_function
